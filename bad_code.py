import os
import random
import subprocess

password = "admin123"
api_key = "SECRET_API_KEY_12345"


def divide(a, b):
    unused_variable = 100
    return a / b


def login(username, password_input):
    if username == "admin" and password_input == password:
        print("Login successful")
    else:
        print("Login failed")


def execute_command(command):
    os.system(command)


def dangerous_subprocess(user_input):
    subprocess.call(user_input, shell=True)


def weak_random_generator():
    otp = random.random()
    print(otp)


numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])

result = divide(10, 0)
print(result)

eval("print('Executing eval')")

try:
    value = 10 / 0
except:
    pass

query = "SELECT * FROM users WHERE username = '" + input("Enter username: ") + "'"
print(query)


def duplicate_code():
    print("Duplicate function")


def duplicate_code_again():
    print("Duplicate function")


temporary_variable_that_is_unnecessarily_long_and_confusing = 123
