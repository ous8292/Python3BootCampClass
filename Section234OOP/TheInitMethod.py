
# Classes in Python can have a special__init__ method, which gets called everytimne you create an instance of the class (instantiate)
# Special cases, You might define a class that only hold methods and no data. You wouldn't need an __init__ method in that case

# Example:
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
'''


class User():
    def __init__(self, first, last, age):  # always calling self first
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last)
print(user2.first, user2.last)


# instantiating a class
# creating an object that is an instance of a class is caleld instantiating a class
# v = Vehicle("Honda","Civic", 2017)


# self keyworkd
# self refers to the current class instance
# Remeber: the parameter doesn't have to be called self, but its the stand and pretty much the only thing you'll see


# Example
'''
class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
      
'''
