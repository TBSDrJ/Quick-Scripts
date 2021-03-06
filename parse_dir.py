#!/usr/bin/python3
import os

MY_HOME_FOLDER = os.environ['HOME']
dirFile = open(MY_HOME_FOLDER + '/Downloads/dir.txt', 'r')

bigFiles = []
# For testing, look at only the first chunk of files
# tmpCounter = 0
for line in dirFile:
    # tmpCounter += 1
    # if tmpCounter > 10:
    #     break
    # To separate out files from other lines
    entry = line.split()
    # If this is true, we probably have a line with a file
    if len(entry) > 8:
        # Field [4] will have the file size
        # But sometimes maybe not, skip the others
        # Right now, print lines with files over 10M
        try:
            if int(entry[4]) > 10000000:
                print(entry)
        except:
            pass
