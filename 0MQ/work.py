from __future__ import division, print_function
import zmq
import sys
from lxml.html.clean import Cleaner
import requests
import nltk
import re

context = zmq.Context()

# PULL FROM VENTILATEUR
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5678")

# PUSH TO SINK
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5688")

# RECEIVE KILL SIGNAL FROM SINK
killswitch = context.socket(zmq.SUB)
killswitch.connect("tcp://localhost:5666")

# DEFINE FUNCTIONS
def makeurl(title, base='https://en.wikipedia.org/wiki/'):
    url = base+title
    return(url)

def url2count(title):
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    cleaner.html= True
    
    r = requests.get(makeurl(title), timeout=5) #r.text
    lxclean = cleaner.clean_html(r.text.replace('\t',' ').replace('\n',' ').replace('\r',' '))
    text = nltk.clean_html(lxclean)
    collapsewhitespace = re.sub(r'\s{2,}', ' ', text)
    nonPunct = re.compile('.*[A-Za-z0-9].*') 
    article_list = [w for w in collapsewhitespace.split(' ') if nonPunct.match(w)]
    article_length = len(article_list)
    return(article_length)

print("Worker ready to work.")

while True:
    # while not killswitch.recv()?
    # test whether first thing is the "0" sync command...?
    title = receiver.recv()
    ct = url2count(title)
    print("{}: {}".format(title,str(ct)))
    sender.send(str(ct))
