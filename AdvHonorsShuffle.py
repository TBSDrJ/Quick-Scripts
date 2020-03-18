#!/usr/bin/python3
# Written in Python 3.7.4, but should be broadly compatible

from random import shuffle

classList = ["RJ", "Evan", "Colter", "Sabrina", "Elisabeth", "Pranav", "Wesley", "Caroline", "Audrey"]
shuffle(classList)
for index, student in enumerate(classList):
    print("Block " + str(index // 3) + ", Meeting " + str(index % 3) + ": " + student)
