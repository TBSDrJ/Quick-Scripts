#!/usr/bin/python3
# Written in Python 3.7.4, but should be broadly compatible

from random import shuffle

classList = ["Mohamed", "Evan", "Nick Chen", "Eric", "Drew", "Michelle", "Claire", "Rolan", "Matthew", "Nick Liu", "Ethan", "Michael", "Stanley"]
shuffle(classList)
for index, student in enumerate(classList):
    if index < 12:
        print("Block " + str(index // 3) + ", Meeting " + str(index % 3) + ": " + student)
    else:
        print("Block 3, Meeting 3: " + student)
