myList = list(range(1, 10))
print(myList)

for x in range(2, 10, 2):
    print(x)

programming_lanugaue = ["C", "C++", "JAVA", "Python", "Ruby", "Pascal", "KotLin"]

for y in range(len(programming_lanugaue)):
    print(f"Programming Language:{programming_lanugaue[y]}")  # range ber kora

fruits = ["Apple", "Mango", "Litchi", "Banana", "PineApple", "BlueBerry", "JackFruit"]

if "Apple" in fruits:
    print("Yes got it",fruits)
else:
    print("Nothing")

for x, fruit in enumerate(fruits):  # range and index ber kora
    print(f"{x} index of {fruit}")

for x, y in zip(programming_lanugaue, fruits):  # Parallel 2ta list access kora
    print(f"{x} like =>{y}")

    for i in sorted(fruits):
        print(i)
        print("break==============")
        for x in reversed(sorted(fruits)):
            print(x)


