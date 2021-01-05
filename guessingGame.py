import random

random_number = random.randint(1, 10) # numbers 1 -10

'''
user_guess = input('Guess the number: ')

## handle user guesses

# first attempt, was stuck on working the while loop in
if int(user_guess) == random_number:
    print('Correct!') # if they guess correct, tell them they win
elif int(user_guess) > random_number:
    print('Wrong, try a lower number')
else:
    print('Wrong, try a higher number')

    #otherwise tell them they are too high or too low

print(random_number)
'''

#BONUS - let player play again if they want

#using solution as help to work forwards
'''
user_guess = ''
while user_guess != random_number:
    user_guess = input('Guess the number between 1 to 10: ')
    if int(user_guess) < random_number:
        print('Try a lower number')
    elif int(user_guess) > random_number:
        print('Try a higher number')
    else:
        print('You won')
    print(random_number)
'''


#this version asks if the player wants to play agauser_guess = ''
while True:
    user_guess = input('Guess the number between 1 to 10: ')
    if int(user_guess) > random_number:
        print('Try a lower number')
    elif int(user_guess) < random_number:
        print('Try a higher number')
    else:
        print('You won')
        play_again = input('Do you want to play again? (y/n)')
        if play_again == 'y':
            random_number = random.randint(1, 10)
            giess = None
        else:
            print('Thanks for playing!')
            break
    print(random_number)







          
