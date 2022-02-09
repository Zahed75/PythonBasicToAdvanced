from array import *

stu_roll = array('i', [])
n = int(input("Enter The Values="))

for i in range(n):
    stu_roll.append(int(input('Please Enter The Elements=')))

for i in range(n):
    print(stu_roll[i])
