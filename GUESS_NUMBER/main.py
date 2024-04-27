import random

def guess(x):
    """
    Perform a guessing game where the user tries to guess a random number between 1 and x.

    Parameters:
        x (int): The upper bound for the range of random numbers.

    Returns:
        None
    """
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess < random_number:
            print('Sorry, guess again, too low.')
        elif user_guess > random_number:
            print('Sorry, guess again, too high.')
    print (f'Congratulations! You have guessed the number {random_number} correctly!')

def computer_guess(x):
    """
    Let the computer guess the user's number through a series of prompts.

    Parameters:
        x (int): The upper bound for the range of random numbers.

    Returns:
        None
    """
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 

    print(f'Yayyyy, the computer guessed your number, {guess}, correctly!')

if __name__ == "__main__":
    computer_guess(1000)
