
'''

Limitations of lists
	good for storing information, but you'll unsure about what each item stands for

A dictionary
	a data structure that consists of key value pairs
	we use the keys to describe our data and the values to represent the data
	
	
	Dictionary example:
	instructor = {
		"name" : "colt",
		"owns_dog" : True,
		"num_courses" 4,
		"favorite_language" : "Python",
		"is_hilarious" : False,
		44 : "my favorite number!"
	}
	
		Keys and values separated by a colon
		Keys are almost always numbers or strings
		Values can be anything
			lists, dictionary's, strings, ints, ect
			

	Another approach is to use the dict function
		You assign values to keys by passing in keys and values 
		seperated by an =
		
		another_dictionary = dict(key = 'value')
		#another_dictionary = dict('key' : 'value')


'''


#EXERCISE
#Create a dictionary called user_info and add 3 key value pairs
'''
user_info = {
    "Name" : "Peter",
    "Nationality" : "German",
    "Age" : 28,
}



user_info = dict(name = "Peter", nationality = "German", age = 28)

print(user_info)
'''






#Accessing Individual Values

'''

To get the value out, you pass in a key

	Example:
	instructor = {
		"name" : "colt",
		"owns_dog" : True,
		"num_courses" 4,
		"favorite_language" : "Python",
		"is_hilarious" : False,
		44 : "my favorite number!"


		instructor["name"] #"Colt"
		instructor["thing"] # KeyError



'''




#Access Data in Dictionary Exercise
'''
artist = {
    "first": "Neil",
    "last": "Young",
}

#Declare a variable called full_name that is equal to arist's first and last name with a space between them


full_name = artist["first"] + ' ' + artist["last"]

print(full_name)
'''











#Iterating Dictionaries
'''
#Example:
instructor = {
        "name" : "colt",
        "owns_dog" : True,
        "num_courses" : 4,
        "favorite_language" : "Python",
        "is_hilarious" : False,
        44 : "my favorite number!"
        }



#for loop method
for v in instructor.values(): # prints values out
    print(v)

for k in instructor.keys(): # prints keys out
    print(k)


for key,value in instructor.items(): # prints all keys and values.
    print(key,value)




# dict.item() returns a list of tuplets. 

'''








'''
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)



# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

#total_donations = for v in donation.values()

total_donations = 0 #creates variable sets it to 0
 
for donation in donations.values():
 total_donations += donation #adds the next itteration of the loop to the varible

 print(total_donations)


'''





#checking if a dictionary has a key
'''
#Example:
instructor = {
        "name" : "colt",
        "owns_dog" : True,
        "num_courses" : 4,
        "favorite_language" : "Python",
        "is_hilarious" : False,
        44 : "my favorite number!"
        }
#keys
"name" in instructor #True
"awesome" in instructor #False

#values
"Colt" in instructor.values() # True
"Nope!" in instructor.values() #False
'''








#Dictonary Methods
'''
#clear, clears all the keys and values in a dictionary
d = dict(a=1, b=2,c=3)
d.clear()


#copy, makes a copy of a dictionary
d = dict(a=1, b=2,c=3)
c = d.copy()
c # {'a' : 1, 'b' : 2, 'c' : 3}
c is d #False

#fromkeys, creates key value pairs from comma separated values. called in an empy dictionary
{}.fromkeys("a", "b") #{'a': 'b'}

#get, retrieves a key in an object and return None instead of an key error if they does not exist
d = dict(a=1, b=2, c=3)
d['a'] #1
d.get('a') #1
d['no_key'] #KeyError
d.get('no_key') #None
'''



###Dictionary Access Practice####
# This code picks a random food item:
from random import choice

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We dont have that")

quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("We dont have that")










