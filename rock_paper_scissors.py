import random

print("\nWelcome to Sheldon Cooper's 'Rock, Paper, Scissors, Lizard, Spock' Game! 🪨 📄 ✂️ 🦎 🖖")
print("Let the battle of wits commence!")

def play_game():

    user_wins = 0
    computer_wins = 0
    try_both = 0
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    options[0]

    win_phrases_user = [
    "✅ You won! Sheldon didn't see that coming. ✅",
    "✅ You won! Sheldon's plan failed against your tactics. ✅",
    "✅ You won! Sheldon's logic is no match for your intuition. ✅",
    "✅ You won! Sheldon's outdone by your mastery of the game! ✅",
    "✅ You won! Sheldon underestimated your abilities. ✅"
    ]

    win_phrases_computer = [
        "🚫 Sheldon and his brain, YEAH! You've been outsmarted. 🚫",
        "🚫 Sheldon's superior strategy! You're outmatched. 🚫",
        "🚫 Sheldon's intellect reigns supreme! Accept your loss. 🚫",
        "🚫 Behold Sheldon's genius! Bow down in defeat. 🚫",
        "🚫 Witness the genius of Sheldon! You're outwitted. 🚫"
    ]

    while True:
        user_input = input("\nType rock/paper/scissors/lizard/spock: ").lower()

        if user_input not in options:
            print("Bazinga! Please enter a valid option.")
            continue

    # rock: 0, paper: 1, scissors: 2, lizard: 3, spock: 4
        random_number = random.randint(0, 4)
        computer_pick = options[random_number]
        print("- Sheldon picked", computer_pick + ".")

        if user_input == computer_pick:
            print("It's a tie!")
            try_both += 1

        elif (user_input == "rock" and (computer_pick == "scissors" or computer_pick == "lizard")) or \
            (user_input == "paper" and (computer_pick == "rock" or computer_pick == "spock")) or \
            (user_input == "scissors" and (computer_pick == "paper" or computer_pick == "lizard")) or \
            (user_input == "lizard" and (computer_pick == "paper" or computer_pick == "spock")) or \
            (user_input == "spock" and (computer_pick == "rock" or computer_pick == "scissors")):
            
            random_phrase_user = random.choice(win_phrases_user)
            print(random_phrase_user)
            user_wins += 1
            try_both += 1

        else:
            random_phrase_computer = random.choice(win_phrases_computer)
            print(random_phrase_computer)
            computer_wins += 1
            try_both += 1

        if try_both == 5:
            break

    print("\nYou won", user_wins, " times!")
    print("Sheldon won", computer_wins, " times!")

while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Thank you for engaging in this intellectually stimulating activity.")
        break