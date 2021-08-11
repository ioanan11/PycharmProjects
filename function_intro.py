def addition (a, b):
    return (a + b)

print(addition(3,5))
print(addition(165,194))

def subtraction (a, b):
    return (a-b)

print(subtraction(423, 2))
print(subtraction(5725, 6))

def calculator(instruction, a, b):
    if instruction == "addition":
        return addition(a, b)
    elif instruction == "subtraction":
        return subtraction(a, b)
print(calculator("addition", 3, 7))

import requests



