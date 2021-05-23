source ~/archiconda3/etc/profile.d/conda.sh && conda activate streaming && python3 /home/ubuntu/projects/tests/producer.py & \
source ~/archiconda3/etc/profile.d/conda.sh && conda activate streaming && python3 /home/ubuntu/projects/tests/spark_consumer_producer.py & \
source ~/archiconda3/etc/profile.d/conda.sh && conda activate streaming && python3 /home/ubuntu/projects/tests/kafka_consumer.py & \
exit 0