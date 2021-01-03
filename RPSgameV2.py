


print("Rock")
print("Paper")
print("scissors")

#Player one enters a choice
player1 = input("Player 1, make your move: ") # asking for input with a print statement
print("***NO CHEATING!!\n" *20) #creates shield by multiplying the string by 20 ona new line each time
#player two enters a choice
player2 = input("Player 2, make your move: ") # asking for input with a print statement

#choice logic
#nested if statements
    # the reason for this is so we dont have to rewrite if player 1 == rock multiple times

if player1 == player2: #not at the bottom so the code does not have to run if it is a tie
    print("It's a tie!")
elif player1 == 'rock':
    if player2 == 'scissors':
        print('player1 wins!')
    elif player2 == 'paper':
        print('player 2 wins!')
elif player1 == 'paper':
    if player2 == 'rock':
        print('player1 wins!')
    elif player2 == 'scissor':
        print('player 2 wins!')
elif player1 == 'scissor':
    if player2 == 'paper':
        print('player1 wins!')
    elif player2 == 'rock':
        print('player 2 wins!')
else:
    print("Something went terribly wrong")







