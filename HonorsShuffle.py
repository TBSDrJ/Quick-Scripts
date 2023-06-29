#!/Library/Frameworks/Python.framework/Versions/Current/bin/python3
# Written in Python 3.7.4, but should be broadly compatible

from random import shuffle

def shuffleAndPrint(classList):
    # break list in half, round up
    breakPoint = len(classList) // 2 + len(classList) % 2
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


per5classList = ["Nicholas", "Eli", "Matthew", "Annie", "Athena",
    "Nicole", "Dax", "Ashir", "Chiara", "Will", "Justin", "Hewitt",
    "Daniel", "Shirley"]
shuffleAndPrint(per5classList)
per7classList = ["Sasha", "Sydney", "George", "James", "Alex", "Aiden",
    "William", "Emma", "Eddie", "Isabel", "Hausen", "Emily", "Andrew"]
shuffleAndPrint(per7classList)
combinedList = ["Nicholas", "Eli", "Andrew", "Matthew", "Annie", "Athena",
    "Nicole", "Dax", "Ashir", "Chiara", "Will", "Justin", "Hewitt",
    "Daniel", "Shirley", "Sydney", "George", "James", "Alex", "Aiden",
    "William", "Emma", "Eddie", "Isabel", "Hausen", "Emily"]
