import random

a = input("start or end Game: ")

if a == "start":
    print("Welcome to the Number Guessing Game!!")
    print("computer will think of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:

        # Show status option only after first attempt
        if attempts < 10:
            status = input("<_< Type 'end' to quit or press Enter to continue: >_>")
            if status == "end":
                print("Game ended by user.")
                break

        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break

        attempts -= 1
    if attempts == 0:
        print(f"Sorry, you've used all your attempts. The number was {number}.")

elif a == "end":
    print("Game over. Thanks for playing!")