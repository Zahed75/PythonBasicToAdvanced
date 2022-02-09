from array import *
stu_roll=array('i',[100,101,102,103,104,105])
n=len(stu_roll)

for x in range(n):
    print(x,"=",stu_roll[x])

print("array after append")
stu_roll.append(106)
i=0
while i<=n:
    print(stu_roll[i])
    i+=1
print("End")