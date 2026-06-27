import os
import pathlib
import re
from pathlib import Path
# Problema 1 => Password Checker

def check_password_strength(password):
    if len(password) > 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong"
    else:
        return "Weak"

verify = check_password_strength("Python123")
print(verify)
verify = check_password_strength("weakpass")
print(verify)
verify = check_password_strength("Francesco.12G")
print(verify)


# Problema 2 => Guess the number(With Exception)

secret_number = 8  # Secret number between 1 and 10
"""
while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You win!")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")
"""
# Problema 3 => Temperature Logger (Read/Write file)

def log_temperatures(temp):
    try:
        with open("log.txt", "a") as log:
            log.write(f"{temp}\n")
            print("Temp appended")
    except IOError as e:
        print(f"Error: {e}")

log_temperatures(32)
log_temperatures(24)

def read_temperatures():
    try:
        with open("log.txt", "r") as log:
            temperatures = []
            for line in log:
                temperatures.append(float(line))
            average = sum(temperatures) / len(temperatures)
            print(f"Average: {average}")
    except IOError as e:
        print(f"Error: {e}")

read_temperatures()

# Problema 4 => FizzBuzz with a twist (Functions & Loops)
"""
def custom_fizzBuzz(n):

    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num)

custom_fizzBuzz(15)
"""
# Problema 5 => Search name from directory recursively

search_name = input("Enter your search name: ")
start_directory = input("Enter your start directory: ").strip()
path = f"C:\\Users\\franc\\Desktop\\An3_Sem2\\PNS\\{start_directory}"
print(path)
if not os.path.exists(path):
    print("Path does not exist")

def find_files(pattern, path):
    results = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if re.search(pattern, name, re.IGNORECASE):
                results.append(os.path.join(root, name))
    return results

result = find_files(search_name, path)
for file in result:
    print(file)


