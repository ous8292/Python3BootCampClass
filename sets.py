# Tuples and Sets


# What is a Tuple? It is an ordered collection or grouping of items

# syntax --

# numbers = (1, 2, 3, 4) # () instead of []

# these are immutable! They cannot be changed after being defined

# Example
'''
    x = (1,2,3)
    3 in x #true
    x[0] = "change me" #TypeError
     '''

# Why use a Tuple? They are faster then lists.
# It can make your code safer from bugs and errors popping up
# We can use tuples as valid keys in a dictionary
# some methods return them to you - like.items() when working with diconaries!

# Creating/Accessing
# Creating using () or the tuple function
# accessing is just like a list!

'''
   first_tuple = (1, 2, 3, 3, 3)
   first_tiple[1] #2
   first_tuple[2] #3
   first_tuple[-1] #3

   second_tuple = tuple(5, 1, 2)

   second_tuple[0] #5
   second_tuple[01] #2
'''

# Tuples can be used as keys in dictonaries:
'''
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office"
    }


locations[(35.6895, 39.6917)] #'San Francisco Office'
'''

# You can not use a list as a key, BUT you CAN use a tuple


# Looping Tuples
'''
    # We can use a for loop to iterate over a tuple just like a list!

    name = ('Colt'), 'Blue', 'Rusty', 'Lassie')

    for name in names:
        print(name)
# colt, Blue Rusty, Lassie

    i=len(name) - 1  # starting at the end
    while i >= 0:
        print(name[i])
        i -= 1  # since we are going backwards



# Tuple Methods


# Count, returns the number of times a value appears in a tuple:
    x=(1, 2, 3, 3, 3)
    x.count(1)  # 1
    x.count(3)  # 3

# Index, returns the index at which a value is found in a tuple

t=(1, 2, 3, 3, 3)
t.index(1)  # 0
t.index(5)  # valueError
t.index(3)  # 2, only thefirst matching index is returned
'''


# Sets
# Sets are like formal mathematical sets
# Sets do not have duplicate values
# Elements in sets aren't ordered
# You cannot access items in a set by index
# Sets can be useful if you need to keep track of a collection of elements, but dont care about order, keys or values and duplicates
'''
# Creating/accessing

# Sets cannot have duplicates
s = set({1, 2, 3, 4, 5, 5, 5})  # {1, 2, 3, 4, 5}

# creatinga new set
s = set({1, 4, 5})
4 in s  # True

8 in s
# False

# Accessing all values in a set
# A good old forloop!

for thing in s:
    print(thing)

# You can turn lists into a set, to elimate the doubles, and then turn it back into a list of unique only.
    # print(set(x)) turns into a set
    # print(list(set(x))) #turns into a list


# Set Methods

# add, adding an element to a set. If the element is already in the set, the set doesn't change

s = set([1, 2, 3])
s.add(4)  # {1, 2, 3, 4}
s.add(4)  # {1, 2, 3, 4} doesnt add another 4


# remove, removes a value from the set - returns a  KeyError if value is not found

set1 = {1, 2, 3, 4, 5, 6}
set1.remove(3)
print(set1)  # {1, 2, 4, 5, 6}

# if you need to avoid KeyErrors use .discard()


# copy, Creates a copy of the set
s = set([1, 2, 3])
another_s = s.copy()
another_s  # {1,2,3}
another_s is s  # False


# clear, removes the contents of the set
s = set([1, 2, 3])
# s.clear()
# set()

# Set Math

# set union
# example_set1 | example_set2
# combines a unique list of the two lists, no duplicates

# set intersection
# example_set1 & example_set2
# shows elements that is in both sets only
'''


# CODING EXERCISE FOR TUPLES AND SETS

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.

nums = (1, 2, 3, 4)


# 2 - Create a variable called value which is a tuple with the the value 1 inside.

value = nums[0]
# 3 - Given the following variable:

values = [10, 20, 30]

# Create a variable called static_values which is the result of the values variable converted to a tuple

static_values =

# 4 - Given the following variable

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
