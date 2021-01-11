#Tuples and Sets


#What is a Tuple? It is an ordered collection or grouping of items

#syntax --

   # numbers = (1, 2, 3, 4) # () instead of []

#these are immutable! They cannot be changed after being defined

#Example
   '''
   x = (1,2,3)
   3 in x #true
   x[0] = "change me" #TypeError
    '''

#Why use a Tuple? They are faster then lists.
#It can make your code safer from bugs and errors popping up
#We can use tuples as valid keys in a dictionary
#some methods return them to you - like.items() when working with diconaries!

#Creating/Accessing
   #Creating using () or the tuple function
   #accessing is just like a list!

'''
   first_tuple = (1, 2, 3, 3, 3)
   first_tiple[1] #2
   first_tuple[2] #3
   first_tuple[-1] #3

   second_tuple = tuple(5, 1, 2)

   second_tuple[0] #5
   second_tuple[01] #2
'''

#Tuples can be used as keys in dictonaries:
'''
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office"
    }


locations[(35.6895, 39.6917)] #'San Francisco Office'
'''

#You can not use a list as a key, BUT you CAN use a tuple



#Looping Tuples
    
    #We can use a for loop to iterate over a tuple just like a list!

    name = ('Colt'), 'Blue', 'Rusty', 'Lassie')

    for name in names:
        print(name)
#colt, Blue Rusty, Lassie

    i = len(name) - 1 #starting at the end
    while i >= 0:
        print(name[i])
        i -= 1 # since we are going backwards



#Tuple Methods


#Count, returns the number of times a value appears in a tuple:
    x = (1, 2, 3, 3, 3)
    x.count(1) #1
    x.count(3) #3

#Index, returns the index at which a value is found in a tuple

t = (1, 2, 3, 3, 3)
t.index(1) #0
t.index(5) #valueError
t.index(3) #2, only thefirst matching index is returned

    

        
        
        


