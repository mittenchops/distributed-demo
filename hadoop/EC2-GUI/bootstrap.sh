#!/usr/bin/env bash

sudo apt-get -y install python-pip libxml2 libxml2-dev libxslt1.1 libxslt1-dev build-essential python-libxslt1 python-dev
sudo easy_install -U distribute
sudo pip install requests nltk lxml
