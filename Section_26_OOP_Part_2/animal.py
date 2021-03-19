class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"this animal says {sound}")


# class Cat(Animal):
#     def __init__(self,name, species, breed, toy):
#         self.name = name
#         self.species = species
#         self.breed = breed
#         self.toy = toy

class Cat(Animal):
    def __init__(self,name, breed, toy):
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")




Kita = Cat("Kita", "Grey Tabby", "String")

Kita.play()


# print(Kita.species)
# print(Kita.breed)
# print(Kita.toy)