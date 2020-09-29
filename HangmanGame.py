from formatting import word_list
from formatting import displayHangman
import random


def getWord():
    return random.choice(word_list).upper()


def hangmanGame(word):
    guessable = word[0] + " " + "_ " * (len(word) - 1)  # getting first letter from the word
    rand_num = random.randint(1, len(word) - 1)   # getting a random index between 2nd index and the last index in word 
    wordAsList = guessable.split()
    wordAsList[rand_num] = word[rand_num]  # getting a random index letter from word
    guessable = " ".join(wordAsList)
    guessed = False
    word_guessed = []
    tries = 6
    letter_guessed = []
    print("Let's play Hangman\n")
    print(displayHangman(tries), "\n")
    print(guessable)
    while not guessed and tries > 0:
        print(f"\nYou have {tries} Tries left")
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letter_guessed:
                print(f"You already guessed {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word")
                tries -= 1
                letter_guessed.append(guess)
            else:
                print(f"Great you found a letter {guess} is in the word")
                letter_guessed.append(guess)
                wordAsList = guessable.split()
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                guessable = " ".join(wordAsList)
                if "_" not in guessable:
                    guessed = True
        elif len(guess) == len(word):
            if guess in word_guessed:
                print(f"You already guessed {guess}")
            elif guess != word:
                print(f"{guess} is not the word")
                tries -= 1
                word_guessed, append(guess)
            else:
                guessed = True
                guessable = word
        else:
            print("Not a valid guess!")
        print(displayHangman(tries), "\n")
        print(guessable)

    if guessed:
        print("\nGreat you guessed the word!  *You Win*")
    else:
        print(f"\nYou ran out of tries \U0001f47B the word was {word}, Try again")


def main():
    again = "Y"
    while again == "Y":
        word = getWord()
        hangmanGame(word)
        again = input("\nPlay Again? (Y/N) ").upper()


main()
