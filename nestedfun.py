# nested function
def disp():
    def show():
        print("Show Function")

    print("Disp Function")
    show()


disp()


def disp():
    def show():
        return "Show Function"

    result = show() + " Disp Fun"
    return result
    show()

a=disp()
print(a)
