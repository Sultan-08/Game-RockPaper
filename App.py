import random
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.\n")
    # Choices available
    choices = ["rock", "paper", "scissors"]
    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.\n")
            continue
        # Computer randomly selects
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!\n")
        else:
            print("Computer wins!\n")
# Run the game
rock_paper_scissors()
