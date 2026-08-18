import random
import ascii

while True:
    print("=========================\nSTART GAME\n=========================")

    print(f"{ascii.name}")
    print("🎯 SMART NUMBER GUESSING GAME")
    print("Guess the secret number between 1 and 100!")
    print()

    while True:
        print("Choose your difficulty:")
        print("1. Easy   - 10 lives")
        print("2. Medium - 7 lives")
        print("3. Hard   - 5 lives")

        difficult = input("Select your choice (1/2/3): ").strip()
        if difficult == "1":
            mode = "Easy"
            user_lives = 10
            break

        elif difficult == "2":
            mode = "Medium"
            user_lives = 7
            break

        elif difficult == "3":
            mode = "Hard"
            user_lives = 5
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            print()

        print("===GAME SETTING===")

    secret_number = random.randint(1, 100)
    low_num = 1
    high_num = 100
    total_lives = user_lives

    print()
    print(f"🎮 Difficulty: {mode}")
    print(f"❤️ You have {user_lives} lives.")
    print(f"🔢 The number is between {low_num} and {high_num}.")
    print()

    while user_lives > 0:
        possible_number = high_num - low_num + 1
        next_guess = (1 / possible_number) * 100

        winning = (min(user_lives / possible_number, 1) * 100)
        print("----------------------------------------")
        print(f"You have {user_lives} lives")
        print(f"possible numbers: {possible_number}")
        print(
            f"🎯 Chance on next guess: "
            f"{next_guess:.2f}%")
        print(
            f"🏆 Chance of winning with remaining lives: "
            f"{winning:.2f}%")
        print("----------------------------------------")

        try:
            user_guess = int(input("Enter number: "))
        except ValueError:
            print("please enter a valid nmber!")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if user_guess == secret_number:
            print("Hurray! You guessed the number correctly!")
            print(f"You won on {mode} mode")
            break

        elif user_guess > secret_number:
            print("Guess is bigger than number. Make it low and try again")

            high_num = user_guess - 1
            user_lives -= 1

            if user_lives > 0:
                print(f"Secret number is between {low_num} - {high_num - 1}")

        elif user_guess < secret_number:
            print("Guess is smaller than number. Make it high and try again")

            low_num = user_guess + 1
            user_lives -= 1

        if user_lives > 0:
            print(f"Secret number is between {low_num} - {high_num}")

    if user_lives == 0:
        print(
            f"Game Over!\n"
            f"You have no lives left. The number was {secret_number}"
        )
    while True:
        start_again = input("Do you want to play again? (yes/no): ").lower().strip()

        if start_again == "yes":
         print("New game started!")
         break

        elif start_again == "no":
            print("Thank you for playing! Goodbye!")
            print(f"{ascii.end}")
            exit()

        else:
         print("Please enter only yes or no.")