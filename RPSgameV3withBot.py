




## MY SOLUTION


#randint needs to be imported
import random

print("Rock")
print("Paper")
print("scissors")

player1 = input("Player 1, make your move: ") #player input

#randint generates random number 0 - 2
# conditional that says if 0 pick rock, if 1 pick paper if, 2 pick scissor
bot_choice = random.randint(0,2)
if bot_choice == 0:
    print('Bot chooses Rock')
elif bot_choice == 1:
    print('Bot chooses Paper')
elif bot_choice == 2:
    print('Bot chooses scissors!')
else:
    print('I broke') #not nescessary, I just put it here incase of errors.



if player1 == bot_choice: 
    print("It's a tie!") 
elif player1 == 'rock':
    if bot_choice == 1:
        print('bot wins!')
    elif bot_choice == 2:
        print('player 1 wins!')
elif player1 == 'paper':
    if bot_choice == 0:
        print('player 1 wins!')
    elif bot_choice == 2:
        print('bot wins!')
elif player1 == 'scissor':
    if bot_choice == 0:
        print('bot wins!')
    elif bot_choice == 2:
        print('player 1 wins!')
else:
    print("Something went terribly wrong")







"""
#COURSE SOLUTION
import random

player = input("Player 1, make your move: ")

rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(computer)


if player == computer: 
    print("It's a tie!") 
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
            print("computer wins")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissors":
            print("computer wins")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    elif computer == "rock":
            print("computer wins")



"""






