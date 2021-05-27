#!/bin/bash
/home/ubuntu/archiconda3/envs/streaming/bin/python3 -u /home/ubuntu/projects/demo/producer.py & \
/home/ubuntu/archiconda3/envs/streaming/bin/python3 -u /home/ubuntu/projects/demo/spark_consumer_sink.py & exit 0
