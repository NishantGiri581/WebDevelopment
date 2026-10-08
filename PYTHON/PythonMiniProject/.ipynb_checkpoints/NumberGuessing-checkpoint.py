import random

number = random.randint(1,100)
attempt = 0
max_attempts = 7

print("🎲 Guess the Number (1 to 100)")

while attempt < max_attempts:
    try:
        guess = int(input(f"Attempt{attempt + 1}: Enter your guess: "))
        attempt += 1

        if guess == number:
            print("🏆Correct! You guessed it.")
            break
        elif guess < number:
            print("📉Too low!")
        else:
            print("📈Too High!")    
    except ValueError:  
        print("Please enter a valid number.")  

if attempt == max_attempts:
    print(f"❌Out of attempts! The number was {number}.")  
