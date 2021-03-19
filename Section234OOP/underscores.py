# _name
# a convention, means private methods please don't mess with this bascially
# __name
# this is used for "name mangling", behind the scenes python mangles the name/changes the attribute. It makes this method/attribute particular to the class
# __name__
# should not use a lot, this is used for python specific methods like init


class Person:
    def __init__(self):
        self.name = "Tony"
        _secret = "Hi!"
        self.__msg = "I like turtles!"


p = Person()
print(p.name)
print(p.secret)
print(p.__msg)  # this wont print anything
