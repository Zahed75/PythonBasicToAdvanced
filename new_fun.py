def add(y):
    x = 10
    c = x + y
    return c


sum = add(30)
print(sum)


# multiple value returns
def add_sub(y):
    x = 10
    c = x + y
    d = x - y

    return c, d


sum, sub = add_sub(20)
print(sum)
print(sub)
