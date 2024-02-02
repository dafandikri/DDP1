import random

# Define the game options
options = ['rock', 'paper', 'scissors']

# Get the player's choice
player_choice = input("Choose rock, paper, or scissors: ")

# Get the computer's choice
computer_choice = random.choice(options)

# Print the choices
print("You chose:", player_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print("You win!")
elif player_choice == 'paper' and computer_choice == 'rock':
    print("You win!")
elif player_choice == 'scissors' and computer_choice == 'paper':
    print("You win!")
else:
    print("Computer wins!")