name = "Peter" #iterable
#next(name) #type error str object is not an iterator
x = iter(name)

next(x) #iterates through the object