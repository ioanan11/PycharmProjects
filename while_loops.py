
list = range (1, 101)

for i in list:
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%5 == 0:
        print("buzz")
    elif i%3 == 0:
        print("fizz")
    else: print(i)



