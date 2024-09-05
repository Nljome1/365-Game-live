import random

def guess_number_game():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number within the valid range (1-100).")
                continue
            
            if guess < secret_number:
                print("Too low! Try guessing a higher number.")
            elif guess > secret_number:
                print("Too high! Try guessing a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to guess the correct number.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number_game()
