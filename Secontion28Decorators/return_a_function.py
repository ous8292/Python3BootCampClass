from random import choice

#we can return functions from other functions

def make_laugh_func():
    def get_laugh():
        l = choice(('Haha', 'lol', 'rofl'))
        return l
    return get_laugh()

laugh = make_laugh_func()
print(laugh())