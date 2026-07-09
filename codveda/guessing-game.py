import random

def guessing_game():
    print("I hava a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 10)

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulation! you guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    # The code above is a simple number guessing game where the user has to guess a number between 1 and 100.
  

if __name__ == "__main__":
    guessing_game()