import os

password = "admin123"

def calculate(a,b):
    unused = 10
    return a/b

def login(username,password_input):
    if username == "admin" and password_input == password:
        print("Login successful")
    else:
        print("Login failed")

numbers = [1,2,3,4,5]

for i in range(len(numbers)):
    print(numbers[i])

x = calculate(10,0)
print(x)
