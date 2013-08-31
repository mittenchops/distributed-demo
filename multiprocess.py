from __future__ import division, print_function
from lxml.html.clean import Cleaner
from multiprocessing import Pool
import requests
import nltk
import re
import csv

# DEFINE CONSTANTS
page = 'AccessibleComputing'

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

# INPUT CONNECTION
pages = []
with open('wikipedia.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile,dialect='excel')
    for row in reader:
        pages.append(''.join(row))

# PERFORM MAP OPERATION
p = Pool(16)
results = []
results = p.map(url2count,pages[0:20])

# PERFORM REDUCE/AGGREGATION
ave = sum(results)/len(results)
