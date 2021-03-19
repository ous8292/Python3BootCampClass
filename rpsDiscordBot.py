import random

player_wins = 0  # sets a player wins variable
computer_wins = 0  # sets a computer wins variable


def displayer_header():
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")


def pick_computer_move():
    rand_num = random.randint(0, 2)
    if (rand_num == 0):
        move = "rock"
    elif (rand_num == 1):
        move = "paper"
    else:
        move = "scissors"
    print(f"The computer plays: {move}")
    return move


def calculate_winner(player, computer):
    global player_wins
    global computer_wins
    if player == computer:
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


def start_game(winning_score):
    while player_wins < winning_score and computer_wins < winning_score:
        displayer_header()

        player = input("(Enter your choice): ").lower()
        if player == "quit" or player == "q":
            break

        computer = pick_computer_move()
        calculate_winner(player, computer)


def display_winner():
    if player_wins > computer_wins:
        print("You've won!")
    elif player_wins == computer_wins:
        print("It's a tie")
    else:
        print("THE BOTS ARE TAKING OVER")


start_game(3)
display_winner()
