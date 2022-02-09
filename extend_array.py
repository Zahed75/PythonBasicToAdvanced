from array import *
stu_roll=array('i',[102,103,104,105,106])
new_stu_roll=array('i',[105,105,555,506])

n=len(stu_roll)

i=0
while i<n:
    print(stu_roll[i])
    i+=1


print("after extend array")

stu_roll.extend(new_stu_roll)
n-len(stu_roll)

for x in stu_roll:
    print(x)