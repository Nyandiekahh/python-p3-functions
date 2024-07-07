#!/usr/bin/env python3

# Define a method greet_programmer() that takes no arguments. 
# It should output the string "Hello, programmer!" to the terminal with print().
def greet_programmer():
    print("Hello, programmer!")

# Define a method greet() that takes one argument, a name. 
# It should output the string "Hello, name!" (with "name" being whatever value was passed as an argument) to the terminal with print().
def greet(name):
    print(f"Hello, {name}!")

# Define a method greet_with_default() that takes one argument, a name. 
# It should output the string "Hello, name!" (with "name" being whatever value was passed as an argument) to the terminal with print(). 
# If no arguments are passed in, it should output the string "Hello, programmer!".
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Define a method add() that takes two numbers as arguments and returns the sum of those two numbers.
def add(num1, num2):
    return num1 + num2

# Define a method halve() that takes one number as an argument and returns that number's value, divided by two.
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
