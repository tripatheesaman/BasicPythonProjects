import random


def to_guess(guess):
    answer = random.randint(1,5)
    while(guess != answer):
        if(guess>answer):
            print("Close!But you were a bit too high")
            guess = int(input("Enter your new guess: "))
        elif(guess<answer):
            print("Close!! But you were a bit too low")
            guess = int(input("Enter your new guess: "))
    
    print(f"WOW!! Spot on!! The number was indeed {guess} ")


guess = int(input("Enter your guess: "))
to_guess(guess)
