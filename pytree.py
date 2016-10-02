#!/usr/bin/env python3
import subprocess
import sys, os
from os import listdir, walk
from os.path import isdir, isfile, dirname, abspath
# -*- coding: utf-8 -*-

# YOUR CODE GOES here

INTERMEDIATE_LEVEL = '│   '.encode('utf-8').decode('latin-1')# "|   "
LAST_LEVEL = '├── '.encode('utf-8').decode('latin-1')#|-- "
LAST_LEVEL_AND_ITEM = '└── '.encode('utf-8').decode('latin-1')#`--"

def getDir():
	#1 additional arguments passed in -> use it as directory if it is one
	if len(sys.argv) == 2 and isdir(sys.argv[1]):
		return abspath(sys.argv[1])
	#other wise print from current path
	else:
		#return dirname(os.path.realpath(__file__))
		return os.getcwd()

def tree(dir_path = getDir(), count = 0):
	if(count == 0):
		print (dir_path)
	numEntries = len(listdir(dir_path))
	subCount = 0
	for item in listdir(dir_path):
		subCount = subCount + 1
		if not item.startswith('.'): #ignore hidden files
			if(isdir(dir_path+'/'+item)):
				s = ""
				for i in range(count):
					s = s + INTERMEDIATE_LEVEL
				s = s + LAST_LEVEL + item
				print(s)
				tree(dir_path+'/'+item, count = count+1)
			else:
				s = ""
				for i in range (count):
					s = s + INTERMEDIATE_LEVEL
				if(subCount == numEntries):
					s = s + LAST_LEVEL_AND_ITEM + item
				else:
					s = s + LAST_LEVEL + item
				print(s)

if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])
    tree()

'''references:
http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html
http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
http://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
http://stackoverflow.com/questions/26938252/converting-utf-8-to-latin-1-in-python
'''