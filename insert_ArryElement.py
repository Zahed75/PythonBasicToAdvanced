from array import *

stu_roll = array('i', [])
n = int(input("Enter the values="))

for i in range(n):
    stu_roll.append(int(input("please enter the value=")))

i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("after insert the value:")
stu_roll.insert(1, 22)
for x in stu_roll:
    print(x)
