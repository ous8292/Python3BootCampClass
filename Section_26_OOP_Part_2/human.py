
class Human:
    def __init__(self,first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

        # the other way
        # def get_age(self):
        #     return self._age
        #
        # def set_age(self, new_age):
        #     if new_age >= 0:
        #         self._age = new_age
        #     else:
        #         self._age = 0
        #

        #using properties
        @property #this is a Declorator
        def age(self): #Getter
            return self._age

        @age.setter #setter
        def age(self, value):
            if value >= 0:
                    self._age = value
            else:
                raise ValueError("age can't be negative!")

        @property
        def full_name(self):
            return f"{self.first} {self.last}"


jane = Human("Jane", "Goodall", 34)
# print(jane.get_age())
#jane.set_age(45)
#print(jane.get_age())
print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)



