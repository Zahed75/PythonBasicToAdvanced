from hashlib import new
from re import T


name=['Zahed Hasan',434,"Rakib Ullah","Mariam Binte","shahed","Jisan"]
print(name)
print(name[1])
print(name[-1])
print(type(name))

name[1]="Shihab" #put the value of index to replace value
print(name)
#list can be modify but tuple cannot modify

data=(343,545,3456,233)
print(data)


#replace value in list

# Use str. replace() to replace a string in a list
strings = ["a", "ab", "aa", "c"]
new_strings = []
for string in strings:
    new_string = string. replace("a", "1") #Modify old string.
    new_strings. append(new_string)# Add new string to list.

print(new_strings)

#make a algo to replace all R to Z

data=["Shihab Hasan","Rakib Ullah","Rahed Hasan"]


new_data=[]

for x in data:
    new_datas=x.replace("R","Z")
    new_data.append(new_datas)
print(new_data)
    
#set data types basically unorder data types which means you can put the any kind of data
#no duplicate value dosen't exist

# data={"Zahed","Sass",43,434,434} #unordered Collections
# print(data)
# for x in data:
#     print(x)


