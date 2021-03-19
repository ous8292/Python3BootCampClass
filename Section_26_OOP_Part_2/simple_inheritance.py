class Animal:
	cool = True

	def make_sound(self, sound):
		print(f"this animal says {sound}")


# Cat class inherits from Animal
class Dog(Animal):
	pass

# Make a new dog instance
Odin = Dog()

# Because of inheritance, a dog has access to:
Odin.make_sound("Woof")
print(Odin.cool)

#odin is both a dog and Animal (and base object)
print(isinstance(Odin, Dog))
print(isinstance(Odin, Animal))
print(isinstance(Odin, object))