from array import *

# basic array

stu_roll = array('i', [101, 102, 103, 104, 105])
length = len(stu_roll)

for x in range(length):
    print(x, "=", stu_roll[x])

print("2nd loop is start")
i = 0
while i <= length:
    print(i, "=", stu_roll[i])
    i += 1
