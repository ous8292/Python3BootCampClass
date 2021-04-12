from random import choice


#nest functions inside one another


def greet(person): #function called greet, takes in an argument called person, and calls another function get_mood
    def get_mood(): #returns msg
        msg = choice(('Hello ', 'go way ', 'I love you '))
        return msg

    results = get_mood() + person #calls get_mood and concatinate person
    return results

print(greet("Peter"))
