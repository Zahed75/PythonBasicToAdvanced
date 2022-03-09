mydict={"Key1":"Zahed","Key2":"Hasan"}
print(mydict)
print(mydict["Key1"])

del mydict["Key1"]
print(mydict)


# Dictionaries
# key -> value
# dict()
a = dict(key1 = 'Simanta', key2 = 'Bohubrihi', key3 = 25)
b = {'key1': 'Simanta', 'key2': 'Bohubrihi', 'key3': 25}
c = dict(zip(['key1', 'key2', 'key3'], ['Simanta', 'Bohubrihi', 25]))
d = dict([('key1', 'Simanta'), ('key2', 'Bohubrihi'), ('key3', 25)])
e = dict({'key1': 'Simanta', 'key2': 'Bohubrihi', 'key3': 25})
f = dict({'key1': 'Simanta', 'key2': 'Bohubrihi'}, key3 = 25)
#print(e.pop('key2'))
x = list(f)
print(x)

# https://docs.python.org/3/library/stdtypes.html#typesmapping
# https://docs.python.org/3/tutorial/datastructures.html#the-del-statement