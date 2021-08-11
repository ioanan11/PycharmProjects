import random
from words import word_list

def get_random_word():
    word = random.choice(word_list)
    return word

print(get_random_word())

def game(word):
    word_compl = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Let's play")
    print("You have ", tries , "tries")
    print(word_compl)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or a word")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter ", guess)
            elif guess not in word:
                print(guess , "is not correct, please try again")
                tries = tries - 1
                print("You have", tries, "more tries")
            else: print ("Good job!", guess , "is in the word")
            for i in word:
                if i==guess:
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You already tried this word")
            elif guess != word:
                print(guess, "is not the correct word, try again")
                tries = tries-1
            else: guessed=True
            word_compl = word
        else: print("Not valid, please enter a letter or a word")

    if guessed:
        print("You guessed the word! Good job!")
    else: print("Game over")
