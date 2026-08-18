# * Start
# * Set lives available for the user to guess
# * Computer_num (number between 1 and 100)
# * Collect User_guess (number between 1 and 100)
# * If lives are exhausted, end game and ask if the user wants to start again
# * If user_guess is equal to computer_guess, user wins, end game
#   and ask if the user wants to start again
# * If user_guess < computer_num, print guess is smaller than number
# * If user_guess > computer_num, print guess is bigger than number

# * Add probability of winning and losing based on the number of lives
#   left and the range of numbers.
# * Example: computer thinks of 10 and user tries 5 on the first attempt.
#   The program should write that the number is between 5 - 100.

import random
import ascii

while True:
    secret_number = random.randint(1, 100)
    user_lives = 7

    low_num = 1
    high_num = 100

    print("Guess the number from 1 to 100!")

    while user_lives > 0:
        print(f"You have {user_lives} lives")
        user_guess = int(input("Enter number: "))

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if user_guess == secret_number:
            print("Hurray! You guessed the number correctly!")
            break

        elif user_guess > secret_number:
            print("Guess is bigger than number. Make it low and try again")

            high_num = user_guess
            user_lives -= 1

            if user_lives > 0:
                print(f"Secret number is between {low_num} - {high_num}")

        elif user_guess < secret_number:
            print("Guess is smaller than number. Make it high and try again")

            low_num = user_guess
            user_lives -= 1

            if user_lives > 0:
                print(f"Secret number is between {low_num} - {high_num}")

    if user_lives == 0:
        print(
            f"Game Over!\n"
            f"You have no lives left. The number was {secret_number}"
        )

    start_again = input("Do you want to play again? (yes/no): ")

    if start_again == "yes":
        print("New game started!")

    elif start_again == "no":
        print("Thank you for playing! Goodbye!")
        break

    else:
        print("Please enter yes or no.")
        # print(f"{ascii.end}")
        break