#!/usr/bin/python3
import os
os.environ['SPARK_HOME']="/home/ubuntu/spark"
os.environ['JAVA_HOME']="/usr/lib/jvm/java-11-openjdk-arm64"
os.environ['PATH']="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/ubuntu/kafka/bin:/home/ubuntu/spark/bin:/home/ubuntu/archiconda3/envs/streaming/bin"

import findspark
findspark.init("/home/ubuntu/spark")


os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1" --jars "/usr/share/java/mariadb-java-client.jar" pyspark-shell'
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, col, window, concat, lit, from_json, regexp_extract, regexp_replace
from pyspark.sql.types import TimestampType, StructField, StructType, StringType, IntegerType, ArrayType


def foreach_batch_function(df, epoch_id):
    print ("Batch %d received" % epoch_id)
    df.show()

    url = 'jdbc:mysql://localhost:3306/crypto'
    table = 'trades'
    mode = "append"
    props = {"user":'ubuntu',
             "password":'abcd', 
             "driver":'org.mariadb.jdbc.Driver'}
    
    df.write \
      .jdbc(url,table,mode,props)



if __name__ == '__main__':

    #sc = SparkContext.getOrCreate()
    #spark = SparkSession(sc)
    spark = SparkSession.builder\
    .master('local')\
    .appName('groupassignment')\
    .getOrCreate()
    
    raw_events_df = spark.readStream \
                          .format("kafka") \
                          .option("kafka.bootstrap.servers", "localhost:9092") \
                          .option("subscribe", "crypto") \
                          .option("startingOffsets", "latest") \
                          .load() \
                          .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING) as value")


    events_df = raw_events_df.select(split("value",'\|').alias("values_split")) \
                                .withColumn("stream",col("values_split").getItem(0)) \
                                .withColumn("e",col("values_split").getItem(1)) \
                                .withColumn("s",col("values_split").getItem(2)) \
                                .withColumn("t",col("values_split").getItem(3)) \
                                .withColumn("p",col("values_split").getItem(4)) \
                                .withColumn("q",col("values_split").getItem(5)) \
                                .withColumn("b",col("values_split").getItem(6)) \
                                .withColumn("a",col("values_split").getItem(7)) \
                                .withColumn("T",col("values_split").getItem(8)) \
                                .withColumn("m",col("values_split").getItem(9)) \
                                .select(col("stream").alias("stream"), 
                                        col("e").alias("event_type"), 
                                        col("s").alias("symbol"), 
                                        col("t").alias("trade_id"), 
                                        col("p").alias("price"), 
                                        col("q").alias("quantity"), 
                                        col("b").alias("buyer_order_id"), 
                                        col("a").alias("seller_order_id"), 
                                        col("T").alias("trade_time"), 
                                        col("m").alias("buyer_market_maker")
                                           )
 

    
    # 3. Configure the sink to send the results of the processing and start the streaming query    
    print ("   - Configuring the foreach sink to handle batches by ourselves.")
    events_df.printSchema()
    streamingQuery = events_df.writeStream \
                                 .foreachBatch(lambda df,epochId:foreach_batch_function(df, epochId))\
                                 .start()
    
    
    # 4. Await for the termination of the Streaming Query (otherwise the SparkSession will be closed)
    print ("The streaming query is running in the background (Ctrl+C to stop it)")
    streamingQuery.awaitTermination()
    
    
    
    
    
