import random
from Words import words
import string

def get_valid_word(words):
    """
    Retrieve a valid word from the provided list of words.

    This function selects a random word from the list of words provided,
    ensuring that the word does not contain underscores or spaces.

    Parameters:
        words (list): A list of words to choose from.

    Returns:
        str: A valid word selected from the list.
    """
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    """
    Play the hangman game.

    This function initializes the hangman game, prompting the user to guess
    letters in order to reveal the hidden word. The user is given a limited
    number of lives, and the game ends when the word is guessed correctly or
    when the user runs out of lives.

    Parameters: None

    Returns: None
    """
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Take away a life if wrong
                print('Letter is not in word')
        elif user_letter in used_letters:
            print('Bro, you literally chose that letter, cannot choose that again. ;-)')

        else:
            print('Invalid character, please try again, bruv.')

    if lives == 0:
        print('You died, sorry. The word was', word, '!')
    else:
        print('You guessed the word', word, '!')

if __name__ == "__main__":
    hangman()
