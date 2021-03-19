
# a function with a name
def square(num):
    return num * num


print(square(9))

# lambda/anon functions.. function with no name
# Lambdas can only be 1 line/single expression
# typically not stored in a variable


def square2(num): return num * num


def square2(num): return num * num


print(square(9))


def add(a, b): return a + b


def add(a, b): return a + b


print(add(3, 10))


# why use this?
# Use case: When you have some code that you need to pass a function into another function as a parameter, and that function will never be used again.
