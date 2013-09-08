#!/usr/bin/env bash

echo "put files on HDFS"
cd distributed-demo/hadoop
hadoop fs -put ./wikipedia-mini.csv .

echo "running mapreduce on the 20-item sample"
hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar 
-jobconf mapred.reduce.tasks=4 \
-file ./mapper.py \
-mapper mapper.py \
-file ./reducer.py \
-reducer reducer.py \
-input wikipedia-mini.csv

