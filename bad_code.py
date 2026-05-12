import os
import subprocess
import random

password = "admin123"
API_KEY = "myapikey123"

def calculate(a,b):
    unused = 100
    return a/b

def login(username,password_input):
    if username == "admin" and password_input == password:
        print("Success")
    else:
        print("Fail")

def execute_command(cmd):
    os.system(cmd)

def dangerous_subprocess(user_input):
    subprocess.call(user_input, shell=True)

def weak_random():
    otp = random.random()
    print(otp)

numbers=[1,2,3,4,5]

for i in range(len(numbers)):
    print(numbers[i])

x = calculate(10,0)
print(x)

eval("print('Hello')")

temp = 5

if temp == 5:
    print("Temp is 5")
else:
    print("Temp is not 5")

try:
    value = 10 / 0
except:
    pass

query = "SELECT * FROM users WHERE name = '" + input("Enter name: ") + "'"
print(query)

long_variable_name_that_is_not_needed_and_makes_code_bad = 123

def duplicate_code():
    print("duplicate")

def duplicate_code_again():
    print("duplicate")
