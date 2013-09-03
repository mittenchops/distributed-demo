import zmq
import csv

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5678")

#jobsizer = context.socket(zmq.REQ)
#jobsizer.bind("tcp://*:5551")

print("Make a bunch of workers, then press enter to start the job...")
junk = raw_input()

#print("Creating workers...")
# numworkers = 10
# [subprocess("python ./work.py &", shell=True) for range(0,numworkers)]

print("Ventillating tasks to workers.")

# This syncs everything.
sender.send('0')

# READ ALL AT ONCE
pages = []
with open('wikipedia-mini.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile,dialect='excel')
    for row in reader:
        pages.append(''.join(row))

for p in pages:
    print("Sending: {}".format(p))
    sender.send(p)

# DISTRIBUTE LINE BY LINE
"""
with open('wikipedia-mini.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile,dialect='excel')
    for row in reader:
        l = ''.join(row)
        try:
            sender.send(l)
        except:
            print("Failed to send line l")
"""

#message = jobsizer.recv()
#print("Answer: *** {} ***".format(message))
