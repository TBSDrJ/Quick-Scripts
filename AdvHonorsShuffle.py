#!/usr/bin/python3
# Written in Python 3.7.4, but should be broadly compatible

from random import shuffle

def shuffleAndPrint(classList):
    # break list in half, round up
    if len(classList) > 10:
        breakPoint = len(classList) // 2 + len(classList) % 2
    else:
        breakPoint = 10
    # shuffle re-orders the existing list in place
    shuffle(classList)
    for index, student in enumerate(classList):
        # If it is the beginning of a day, add a header
        if index == 0:
            print("Today's Class:")
        elif index == breakPoint:
            print("Next Class:")
        # Print the students in order with their meeting slot
        if index < breakPoint:
            print("\tBlock " + str(index // 3) + ", Meeting " + str(index % 3) + ": " + student)
        else:
            print("\tBlock " + str((index - breakPoint) // 3) + ", Meeting " + str((index -breakPoint) % 3) + ": " + student)


per1classList = ["Nick Chen", "Ethan", "Evan Coats", "Rolan", "Elisabeth",
    "Drew", "Grace", "Matthew", "Nick Liu", "Audrey", "Eric", "Kyle", "Evan Ren",
    "Michelle", "Stanley", "Michael", "Claire"]
shuffleAndPrint(per1classList)
juniors = ["Ethan", "Rolan", "Matthew", "Nick Liu", "Kyle", "Michelle", "Stanley", "Michael", "Claire", ]
seniors = ["Nick Chen", "Evan Coats", "Elisabeth", "Drew", "Grace", "Audrey", "Eric", "Evan Ren", ]
