import random

print("Welcome to Sheldon Cooper's 'Rock, Paper, Scissors, Lizard, Spock' Game! 🪨📄✂️🦎🖖")
print("Let's play!")

def play_game():

    user_wins = 0
    computer_wins = 0
    try_both = 0
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    options[0]

    while True:
        user_input = input("Type rock/paper/scissors: ").lower()

        if user_input not in options:
            continue

    # rock: 0, paper: 1, scissors: 2, lizard: 3, spock: 4
        random_number = random.randint(0, 4)
        computer_pick = options[random_number]
        print("Sheldon picked", computer_pick + ".")

    # Rock crushes Scissors !
        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Paper covers Rock !
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Scissors cuts Paper !
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            try_both += 1
     # Rock crushes Lizard !       
        elif user_input == "rock" and computer_pick == "lizard":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Lizard poisons Spock !     
        elif user_input == "lizard" and computer_pick == "spock":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Spock smashes Scissors !
        elif user_input == "spock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Scissors decapitates Lizard !       
        elif user_input == "scissors" and computer_pick == "lizard":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Lizard eats Paper !
        elif user_input == "lizard" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Paper disproves Spock !
        elif user_input == "paper" and computer_pick == "spock":
            print("You won!")
            user_wins += 1
            try_both += 1
    # Spock vaporizes Rock !
        elif user_input == "spock" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            try_both += 1

        else:
            print("You lost...")
            computer_wins += 1
            try_both += 1

        if try_both == 7:
            break

    print("You won", user_wins, " times!")
    print("Sheldon won", computer_wins, " times!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Until next time!")
        break