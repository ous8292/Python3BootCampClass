

# List Comprehension is a shorthand syntax that allows us to generate new lists to make new lists that are direct bopies of other lists, or tweaked versions


# the syntax
#[___ for ____ in ____]

# example
nums = [1, 2, 3]
# for every x in nums it will multiply by 10, and put it into a new list
[x*10 for x in nums]
#[10, 20,30]
