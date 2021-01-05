
'''



## MY SOLUTION


#randint needs to be imported
import random

print("Rock")
print("Paper")
print("scissors")

player1 = input("Player 1, make your move: ") #player input

#randint generates random number 0 - 2
# conditional that says if 0 pick rock, if 1 pick paper if, 2 pick scissor


bot_choice = random.randint(0,2) #bot chooses random int 0 -2


if bot_choice == 0: #if choice is 0 then print
    bot_choice = str('rock')
    print('Bot chooses Rock')
elif bot_choice == 1: # if choice is 1 then print
    bot_choice = str('paper')
    print('Bot chooses Paper')
elif bot_choice == 2:# if choice is 2 then print
    bot_choice = str('scissor')
    print('Bot chooses scissors!')
else:
    print('I broke') #not nescessary, I just put it here incase of errors.

if player1 == bot_choice: # player 1 inputs a string and it compares to a int.. which will not work
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


'''




#SOLUTION USING COURSE VIDEO

import random

player_wins = 0 # sets a player wins variable 
computer_wins = 0 # sets a computer wins variable

while player_wins < 2 and computer_wins <2: # conditional statement for wins
#for time in range(3): can use a simple for loop that repeats the game 3 times( another example of doing it)
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("Player 1, make your move: ")
    
    if player == "quit" or player == "q": # allows player to get out
        break
    
    rand_num = random.randint(0, 2) #picks a random number
    if rand_num == 0: # if random number is 0, then set computer to the string rock
        computer = "rock"
    elif rand_num == 1: # if random number is 0, then set computer to the string paper
        computer = "paper"
    else: # if random number is not 0 or 1, then only thing left is 2. Then it chooses scissors
        computer = "scissors"
    print(computer)


    if player == computer: # player choice (string) gets compared to choice of computer (string)
        print("It's a tie!") 
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        elif computer == "paper":
                print("computer wins")
                computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        elif computer == "scissors":
                print("computer wins")
                computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        elif computer == "rock":
                print("computer wins")
                computer_wins += 1

if player_wins > computer_wins:
    print("You've won!")
elif player_wins == computer_wins:
    print("It's a tie")
else:
    print("THE BOTS ARE TAKING OVER")

print('Player Score: ' + str(player_wins) + '  ' + 'Computer Score: ' + str(computer_wins)) #wins need to be converted to str to print out










