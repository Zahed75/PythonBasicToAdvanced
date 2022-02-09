from array import *

stu_roll = array('i', [102, 103, 403, 204, 102])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1
print("after reverse")

stu_roll.reverse()
for x in range(len(stu_roll)):
    print(x, "=", stu_roll[x])
