# Objectives

# using the * and ** operators as parameters to a function and outside of a function
# leverage dictionary and tuple unpacking to create more flexible function


# *args are special operators we can pass to a function as a parameter.
# Gathers remaining arguments as a tuple
# this is just a parameter - you can call it whatever you want


# Example
'''
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


sum_all_nums(1, 2, 3)  # 6
sum_all_nums(1, 2, 3, 4, 5)  # 15


def ensure_correct_info(*args):
    if "Peter" in args and "Steyer" in args:
        return "Welcome back!"

    return "Not sure who you are..."


ensure_correct_info()  # not sure who you are...
ensure_correct_info(1, True, "Steyer", "Peter")


# Excercise
def contains_purple(*args):
    if "purple" in args:
        return True  # Dont need else part of the condition, since we are returnbing out of the function on the line before. Soo the only way the return False line runs is if the above line didnt run. It's an implicit else.
    return False
'''


# **kwargs keyword args
# A special operator we can pass to functions
# Gathers remaining keyword arguments as a dictionary
# Just a parameter - call it whatever

def fav_colors(**kwargs):
    print(kwargs)  # prints it as a dictionary


# {'peter': 'Purple', 'ruby': 'red', 'ethel': 'teal'}
fav_colors(peter="Purple", ruby="red", ethel="teal")


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorit color is {color}")


fav_colors(peter="Purple", ruby="red", ethel="teal")
fav_colors(peter="Purple", ruby="red", ethel="teal", ted="blue")
fav_colors(peter="forest deep amazing green")


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not sure who this is"


print(special_greeting(David='Hello'))  # Hello David!
print(special_greeting(Bob='hello'))  # Not sure who this is...
print(special_greeting(David='special'))  # you get a special greeting David!


# Parameter Ordering
# 1. Parameters
# 2. *args
# 3. default parameters
# 4. **kwargs
