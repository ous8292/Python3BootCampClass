
# Higher Order Function is just a function that either returns another function from inside
# or accepts one or more function as an argument


def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(3, square))
print(sum(3, cube))
