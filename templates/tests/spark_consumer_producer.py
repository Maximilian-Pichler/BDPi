import findspark
findspark.init()

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1" pyspark-shell'

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

geoEventProcessing = spark.readStream\
                          .format("kafka") \
                          .option("kafka.bootstrap.servers", "localhost:9092") \
                          .option("subscribe", "doge") \
                          .option("startingOffsets", "latest") \
                          .load() \
                          .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
                          .writeStream \
                          .format("kafka") \
                          .option("kafka.bootstrap.servers", "localhost:9092") \
                          .option("checkpointLocation", "/tmp/spark_checkpoint") \
                          .option("topic", "doge_echo") \
                          .start() \
                          .awaitTermination()