#!/usr/bin/env python3
import subprocess
import sys
import os
from os import listdir, walk
from os.path import isdir, isfile, dirname, abspath

# YOUR CODE GOES here

INTERMEDIATE_LEVEL = '│   '.encode('utf-8').decode('latin-1')
LAST_LEVEL = '├── '.encode('utf-8').decode('latin-1')
LAST_LEVEL_AND_ITEM = '└── '.encode('utf-8').decode('latin-1')

# INTERMEDIATE_LEVEL = "|   "
INTERMEDIATE_LEVEL2 = "    "
# LAST_LEVEL = "|-- "
# LAST_LEVEL_AND_ITEM = "`-- "


def getDir():
    # 1 additional arguments passed in -> use it as directory if it is one
    if len(sys.argv) == 2 and isdir(sys.argv[1]):
        # return abspath(sys.argv[1])
        return sys.argv[1]
    # other wise print from current path
    else:
        # return dirname(os.path.realpath(__file__))
        # return os.getcwd()
        return "."


# put spacing into string:
def stringify(spc):
    s = ""
    for elt in spc:
        s = s + elt
    return s


def tree(dirs=0, files=0, dir_path=getDir(), spc=[]):
    if(len(spc) == 0):
        print(dir_path)
    numEntries = len(listdir(dir_path))
    subCount = 0
    for item in sorted(listdir(dir_path)):
        subCount = subCount + 1
        if not item.startswith('.'):  # ignore hidden files
            s = stringify(spc)  # put spacing into string:

            # process directories:
            if(isdir(dir_path + '/' + item)):
                dirs = dirs + 1
                # Add an intermediate level spacing
                spc.append(INTERMEDIATE_LEVEL)
                # If this is the last item in this level list
                if(subCount == numEntries):
                    # replace last spacing with intermediate level 2 spacing (no more lines under last item)
                    spc[-1] = INTERMEDIATE_LEVEL2
                    print(s + LAST_LEVEL_AND_ITEM + item)
                else:
                    print(s + LAST_LEVEL + item)
                dirs, files = tree(dirs=dirs, files=files, dir_path=dir_path + '/' + item, spc=spc)
                del spc[-1]  # When return from recursive tree call, delete last spacing element

            # process files:
            else:
                files = files + 1
                if(subCount == numEntries):
                    print(s + LAST_LEVEL_AND_ITEM + item)
                else:
                    print(s + LAST_LEVEL + item)

    return dirs, files

if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    dirs, files = tree()
    print('\n' + str(dirs) + " directories, " + str(files) + " files")


'''references:
http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html
http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
http://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
http://stackoverflow.com/questions/26938252/converting-utf-8-to-latin-1-in-python
https://wiki.python.org/moin/HowTo/Sorting
'''
