# Instance Attributes and Methods

# anything with double __ __ put on top, for convention


class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    # These are "instance methods"

    def full_name(self):  # anytime we define a instance method, we need to pass self as the first parameters
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user2.full_name())
print(user1.initials())
print(user1.likes("Ice Cream"))
