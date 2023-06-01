from words import words
import random
import string


def get_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()


def hangman(words):
    word = get_words(words)
    print(word)
    word_letters = set(word)
    guessed_letters = set()
    alphabets = set(string.ascii_uppercase)
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("You have used: ", ' '.join(guessed_letters))
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_letter = input("Enter a letter: ").upper()
        if user_letter in alphabets and user_letter not in guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in alphabets and user_letter in guessed_letters:
            print("You've already tried that!!")
        else:
            print("Invalid Entry!!")
    if lives > 0:
        print(f"The word was {word}.\nCongrats nerd!!! Get a life")
    else:
        print(f"Dumbass!!!You thought you could.\nThe word was {word}.HAHAHAHAHAHAHAHAH DUMBASS")


hangman(words)
