#!/usr/local/bin/python

# Opens a file, grabs its filename - appends it to the top of the file and inserts ENDTITLE after it.
# Appends ENDPAGE at the end of the page.

import inspect, os
from sys import argv

def line_prepender(filename,line):
    with open(filename,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)
def line_appender(filename,line):
	with open(filename, "a") as f:
		f.write(line)

script, filename = argv
filetoOpen = open(filename)
fileName = filetoOpen.name
file = fileName.split("_")[0]
lineattop = file + "\n" + "--ENDTITLE--"
lineatend = "\n"+"--ENDPAGE--"+"\n"
line_prepender(filename,lineattop)
line_appender(filename,lineatend)
