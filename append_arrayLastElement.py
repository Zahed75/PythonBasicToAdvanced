from array import *

stu_roll = array('i', [101, 102, 103, 104])
n = len(stu_roll)

i = 0
while i < n:
    print(stu_roll[i])
    i += 1
print("2nd loop start")
stu_roll.append(105)
n = len(stu_roll)

i = 0
while i < n:
    print(stu_roll[i])
    i += 1
