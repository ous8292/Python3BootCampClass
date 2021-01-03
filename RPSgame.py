


print("Rock")
print("Paper")
print("scissors")

#Player one enters a choice
player1 = input("Player 1, make your move: ") # asking for input with a print statement
#player two enters a choice
player2 = input("Player 2, make your move: ") # asking for input with a print statement

#choice logic
if player1 == 'rock' and player2 == 'scissors':
    print('Player 1 wins')
elif player1 == 'rock' and player2 == 'paper':
        print('Player 2 wins')
elif player1 == 'Paper' and player2 == 'scissor':
        print('Player 1 wins')
elif player1 == 'Paper' and player2 == 'rock':
        print('Player 1 wins')
elif player1 == 'scissor' and player2 == 'paper':
        print('player 1 wins')
elif player1 == 'scissor' and player2 == 'rock':
        print('player 2 wins')
elif player1 == player2:
        print("It's a tie!")
else:
    print('SOMETHING WENT TERRIBLY WRONG')








