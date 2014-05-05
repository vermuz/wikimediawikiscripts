#!/usr/local/bin/python

# Opens a file, grabs its filename - appends it to the top of the file and inserts ENDTitle after it.

import inspect, os
from sys import argv

def line_prepender(filename,line):
    with open(filename,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)
script, filename = argv
filetoOpen = open(filename)
fileName = filetoOpen.name
file = fileName.split("_")[0]
line = file + "\n" + "--ENDTITLE--"
line_prepender(filename,line)