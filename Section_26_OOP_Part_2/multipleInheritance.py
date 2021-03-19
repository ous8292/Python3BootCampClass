class Aquatic:
    def __init__(self,name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"



class Penguine(Aquatic, Ambulatory):
    def __init__(self, name):
        super().__init__(name = name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguine("Captain Cook")

#Jaws methods
print(jaws.swim())
print(jaws.greet())


#Lassie Methods
print(lassie.walk())
print(lassie.greet())

#Captain Cook gets Swim and Walk from parents
print(captain_cook.swim())
print(captain_cook.walk())

#Captain Cook only one of the parents not both (Ambulatory)
print(captain_cook.greet())

