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

"""
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
"""

"""
Spatamana 2: Cursu 3 => Data structures in Python
"""

# Ex 1
def num_count():
    for i in range(1, 11):
        print(i)

num_count()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def num_count1(list):
    for i in list:
        print(i)

num_count1(my_list)

# Ex 2

n = int(input("Enter your number: "))

def calc_num(n):
    sum = 0
    for i in range (1, n + 1):
        sum += i
    return sum

sum = calc_num(n)
print(sum)

# Ex 3

def even_num(list):
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

even_list = even_num(my_list)
print(even_list)

# Ex 4

word = input("Enter your word: ")

def reverse_string(sir):
    rev_str = []

    index = len(sir)
    while index:
        index -= 1
        rev_str.append(sir[index])
    return rev_str

print(reverse_string(word))

# Ex 5

vowels = ["a", "e", "i", "o", "u"]

def check_vowel(word):
    sum = 0
    for i in range(len(word)):
        if word[i] in vowels:
            sum += 1
    return sum

print(check_vowel(word))

# Ex 6
def search_max(my_list):
    return max(my_list)

def max_search(my_list):
    max = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
print(search_max([3, 7, 2, 9, 1]))
print(max_search([3, 7, 2, 9, 1]))

# Ex 7

def return_index(my_list, value):
    my_list.sort()
    if value not in my_list:
        return -1
    else:
        return my_list.index(value)

print(return_index([1, 3, 5, 7, 9, 11], 7))

# Ex 8

multiplay_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def multiplication_table(n):
    for i in range(1, len(multiplay_values) + 1):
        print(f"{3} x {i} = {i * n}")

multiplication_table(3)

# Ex 9
def factorial_number(n):
    if n == 1:
        return 1
    else:
        return n * factorial_number(n - 1)

print(factorial_number(5))

# Ex 10
def check_prime(n):
    if n < 2:
        print(False)
    else:
        prime = True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        print(prime)

check_prime(4)

# Ex 11

def remove_duplicates(my_list):
    return set(my_list)


print(remove_duplicates(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']))

# Ex 12

def caeser(text, s):
    result = ""

    for i in range (len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


print(caeser("abc", 2))

# Ex 13
fib = int(input("Enter a number: "))

def fibonnacci(n):
    if n <= 1:
        return n
    return fibonnacci(n - 1) + fibonnacci(n - 2)

my_list = []
for i in range(fib):
    my_list.append(fibonnacci(i))
print(my_list)

# Ex 14

text = input("Enter your text: ")
print(text)

def check_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    my_list = []
    for i in text:
        my_list.append(i)
    print(my_list)
    rev_str = []
    index = len(my_list)
    while index:
        index -= 1
        rev_str.append(my_list[index])
    if my_list == rev_str:
        return True
    else:
        return False

print(check_palindrome(text))

# Ex 15
def count_appearance(text):
    text = text.lower().replace(" ", "")

    for char in set(text):
        print(f"{char}: {text.count(char)}")

count_appearance(text)

# Ex 16

import random
import math
from itertools import combinations

points = set()

while len(points) < 1000:
    x = random.randint(-90, 90)
    y = random.randint(-180, 180)
    points.add((x, y))

points = list(points)

print(points)

min_dist = float('inf')
max_dist = 0

closest_pair = None
farthest_pair = None

for p1, p2 in combinations(points, 2):
    dist = math.dist(p1, p2)
    # print(dist)

    if dist < min_dist:
        min_dist = dist
        closest_pair = (p1, p2)

    if dist > max_dist:
        max_dist = dist
        farthest_pair = (p1, p2)

print(closest_pair)
print(farthest_pair)

science_club = {"Alice", "Bob", "Charlie", "Diana", "Eva"}
sports_club = {"Charlie", "Diana", "Frank", "George", "Alice"}

both_students = []
