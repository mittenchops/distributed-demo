from __future__ import division, print_function
import sys
import zmq
import time

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5688")

killswitch = context.socket(zmq.PUB)
killswitch.connect("tcp://localhost:5666")

#jobsizer = context.socket(zmq.REP)
#jobsizer.connect("tcp://localhost:5551")

s = receiver.recv()
LENGTH = 20
#LENGTH = jobsizer.recv()

results = []
for task in range(0,LENGTH):
    s = int(receiver.recv())
    print("[ ] Received: {}".format(s))
    results.append(s)

total = sum(results)
n = len(results)
print("Sum: {}\tn: {}\tAverage: {}".format(total,n,total/n))

killswitch.send("0")
