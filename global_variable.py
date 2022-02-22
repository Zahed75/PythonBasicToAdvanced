x = 10


def add():
    xy = 10
    print(xy)
    print(x)


add()

i = 0


def my_fun():
    a = i + 1
    print("My Function", a)


my_fun()

x = 50


def show():
    a = 10
    print("Local Variables", a)
    y = globals()['x']
    print('X:', y)
    y = 40
    print("Y", y)


show()
print("Global Variable", x)
