import random

def play_game():

    user_wins = 0
    computer_wins = 0
    try_both = 0
    options = ["rock", "paper", "scissors"]
    options[0]

    while True:
        user_input = input("Type rock/paper/scissors: ").lower()

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            try_both += 1

        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            try_both += 1

        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            try_both += 1

        else:
            print("You lost...")
            computer_wins += 1
            try_both += 1

        if try_both == 5:
            break

    print("You won", user_wins, " times!")
    print("Computer won", computer_wins, " times!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Until next time!")
        break