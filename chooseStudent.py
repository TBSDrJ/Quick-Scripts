#!/Library/Frameworks/Python.framework/Versions/Current/bin/python3

from random import choice

def chooseOne(myList):
  student = choice(myList)
  print(student)
  myList.remove(student)

students = [
    'Nicholas',
    'Andrew']
for i in range(len(students)):
  chooseOne(students)
  input('Press [Return] to make the next choice:')
