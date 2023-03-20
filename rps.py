import random

valid_inputs = ["rock", "paper", "scissors"]

while True:
    you = input("Select rock, paper, or scissors (or enter 'exit' to quit): ").lower()
    if you == "exit":
        print("Thanks for playing!")
        break
    elif you not in valid_inputs:
        print("Invalid input. Please try again.")
        continue

    bot = random.choice(valid_inputs)
    print("bot selected:", bot)

    if you == bot:
        print("Tie!")
    elif (you == "rock" and bot == "scissors") or \
         (you == "paper" and bot == "rock") or \
         (you == "scissors" and bot == "paper"):
        print("you win!")
    else:
        print("bot wins!")
