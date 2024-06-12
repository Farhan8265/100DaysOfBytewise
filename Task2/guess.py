# Exercise: Guess the Number Game
import random
random_num = random.randint(1, 100)

guesses = 0

while True:
    guess = int (input ("Guess the Number between 1 and 100: ") )
    
    guesses += 1
    if guess == random_num:
        print(f"Congratulations! You guessed the number {random_num} correctly in {guesses} guesses.")
        break
    elif guess < random_num:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")