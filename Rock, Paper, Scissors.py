import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
rounds = int(input("Enter the number of rounds you want to play: "))

for i in range(rounds):
    player_choice = input("Please enter your choice (rock, paper, scissors): ")
    if player_choice not in options:
        print("Invalid choice, please try again.")
        continue
    computer_choice = random.choice(options)
    print("Computer's choice:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

print("Player score: ", player_score)
print("Computer score: ", computer_score)
if player_score > computer_score:
    print("You win!")
elif player_score < computer_score:
    print("You lose!")
else:
    print("It's a tie!")