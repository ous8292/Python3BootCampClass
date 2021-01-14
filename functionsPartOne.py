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
