#!/usr/bin/env bash

echo "starting mapper test"
cat wikipedia-mini.csv | ./mapper.py 

echo "\nstarting mapper + reducer test"
cat wikipedia-mini.csv | ./mapper.py | sort -k1,1 | ./reducer.py 
