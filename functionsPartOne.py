from random import random

# What is a Function?
# A process for executing a task
# It can accept input and return an output
# Useful for executing similar procedures over and over
# some need inputs some dont


# Why use Functions?
# Stay DRY - Don't Repeat Yourself!


# DEFINING FUNCTIONS

# Function structure

#  def name_of_function():
# block of runnable code
'''
def say_hi():
    print('hi!')


say_hi()  # you must envoke/call the function for it to work
'''

# Returning Values from functions

'''
def print_square_of_7():
    return 7**2


result = print_square_of_7()
print(result)


def say_hi():
    return 'Hi!'  # ends the function., Nothing afterwards runs


greeting = say_hi()
print(greeting)

# Return
# exists the function
# outputs whatever value is placed after the return keyword
# pops the function of the call stack
'''


# FLIP_COUNT Function

'''
def flip_coin():
    # generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())

# could also do


def flip_coin_shorter():
    # generate random number 0-1
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin_shorter())

'''


# Parameters
# Are variables that are passed to a function, like a placeholder that gets assigned when functiopn is called
# parameters for functions ONLY are in that function. You cannot call them anywhere else


# def function_name(paramter_name)
'''
def square(num):
    return num * num


print(square(4))
'''

# Two parameters
# def add(a,b):
# return a+b


# Parameters vs Arguments
# a parameter is a variable in the method definition
# When a method is called, the arguments are the data you pass into the methods parameters
# parameter is variable in the declaration of function
# Argument is the actual value of this variable that gets passed to function


# Yell Function Exercise
'''
def yell(noise):
    return noise.upper() + '!'
'''

# Animal sound functions

# solution 1
'''

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
'''

# Other solutions
# Mapping noises to a dictionary
'''
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
''''


# KEYWORD ARGUMENTS
# keywords let us specify the parameters if we know them
# example
'''
def full_name(first, last):
    return "Your name is {first} {last}"


full_name(fist='Peter', last='Steyer')  # Your name is Peter Steyer
full_name(last='Steyer', first='Peter')  # Your name is Peter Steyer
# Order does not matter!!
'''

'''
def exponent(num, power=2)
    return num ** 2

print(exponent(power=3, num=4))
print(exponent(num=4, power=3))
'''

# Why use keyword Arguments?
# Useful when passing a diuctionary to a function and unpoacking it's values

# Different from Default Params
# When you define a function and use = you are setting a default parameter
# When you invoke a function and use an = yopu are making a keyword argument


# SCOPE
# variables and properties are not awlays available in every single part of the project
# Variables created in function are scoped in that function!
# global scope lets us reference variables that were  orginally assigned on the global scope
# nonlocal lets us modify a parent's variables in a child(aka nested) function


# Documenting Functions
# use """ """ to document what each function does
'''
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

say_hello._doc #access the message above
'''


######RECAP#########
# Functions are procedures for executing code. They accept inputs and return outputs when the return keyword is used
# To create inputs, we make parameters which can have default values, we call those default parameters
# Variables defined inside of functions are scoped to that function - watch for that
# When invoking a function we can pass in keyword arguments in any order


# Exercises

# Write a function call product that accepts two parameters and returens the product of the two parameters
'''
def product(a, b_):
    return a * b
'''


# Wrrite
# Write a function called return_day. This function takes in one parameter (a number from 1-7) and returns the day of the week (1 is sunday, 2 is monday, ect). If the number is less than 1 or greater than 7, the function should return none

def return_day(day):  # defines function
    week_day = [Sunday, Monday, Tuesday, Wednesday,
                Thursday, Friday, Saturday]  # defines list
    # if day is geater then 0 AND less than or equal to the length of week_day
    if day > 0 and day <= len(week_day):
        return week_day[day - 1]  # return the index of week_day - 1
    return None  # return none if any other value


# Write a function called last_element. This function takes on parameter (a list) and returns the last value in the the list. It should return None if list is empty

def last_element(x):  # defines x
    if x:
        return x[-1]
    return None

    def last_element(item):
        last = items[-1]
        if last:
            return last
        return None


def number_compare(a, b):
    if a > b:
        print('First is greater')
    elif a < b:
        print('Second is greater')
    else:
        print('Numbers are equal')
    pass


number_compare(3, 1)
