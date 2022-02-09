from array import *

stu_roll = array('i', [])
n = int(input("Enter The Value:"))

for i in range(n):
    stu_roll.append(int(input("Enter the element:")))

for x in range(len(stu_roll)):
    print(stu_roll[x])


print("2nd Loop start")
number = array('i', [])
n = int(input("Enter the value="))
for i in range(n):
    number.append(int(input('Enter the element=')))
for x in range(len(number)):
    print(stu_roll[x])
