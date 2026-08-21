import random
import ascii


while True:
    # print("=========================")
    # print("START GAME")
    # print("=========================")
    print(ascii.start)

    print(ascii.name)
    print("🎯 SMART NUMBER GUESSING GAME")
    print("Guess the secret number!")
    print()

    # Difficulty
    while True:
        print("Choose your difficulty:")
        print("1. Easy   - 10 lives - Number from 1 to 50")
        print("2. Medium - 7 lives - Number from 1 to 100")
        print("3. Hard   - 5 lives - Number from 1 to 200")

        difficult = input("Select your choice (1/2/3): ").strip()

        if difficult == "1":
            mode = "Easy"
            user_lives = 10
            low_num = 1
            high_num = 50
            break

        elif difficult == "2":
            mode = "Medium"
            user_lives = 7
            low_num = 1
            high_num = 100
            break

        elif difficult == "3":
            mode = "Hard"
            user_lives = 5
            low_num = 1
            high_num = 200
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            print()

    # secret_number = random.randint(1, 100)
    secret_number = random.randint(low_num, high_num)

    print()
    print("=== GAME SETTINGS ===")
    print(f"🎮 Difficulty: {mode}")
    print(f"❤️ You have {user_lives} lives.")
    print(f"🔢 The number is between {low_num} and {high_num}.")
    print()

    # Game loop
    while user_lives > 0:

        possible_number = high_num - low_num + 1
        next_guess = (1 / possible_number) * 100
        winning = min(user_lives / possible_number, 1) * 100

        print("----------------------------------------")
        print(f"You have {user_lives} lives")
        print(f"Possible numbers: {possible_number}")
        print(f"🎯 Chance on next guess: {next_guess:.2f}%")
        print(f"🏆 Chance of winning: {winning:.2f}%")
        print("----------------------------------------")

        try:
            user_guess = int(input("Enter number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_guess < 1 or user_guess > high_num:
            print(f"Please enter a number between 1 and {high_num}.")
            continue

        if user_guess == secret_number:
            print("Hurray! You guessed the number correctly!")
            print(f"You won on {mode} mode!")
            break

        elif user_guess > secret_number:
            print("Guess is bigger than number. Make it low and try again.")
            high_num = user_guess - 1
            user_lives -= 1

        else:
            print("Guess is smaller than number. Make it high and try again.")
            low_num = user_guess + 1
            user_lives -= 1

        if user_lives > 0:
            print(f"Secret number is between {low_num} - {high_num}")
            print()

    if user_lives == 0:
        print("Game Over!")
        print(f"You have no lives left.")
        print(f"The number was {secret_number}")

    # Play again
    while True:
        start_again = input(
            "Do you want to play again? (yes/no): "
        ).lower().strip()

        if start_again == "yes":
            print("New game started!")
            print()
            break

        elif start_again == "no":
            print("Thank you for playing! Goodbye!")
            print(ascii.end)
            exit()

        else:
            print("Please enter only yes or no.")