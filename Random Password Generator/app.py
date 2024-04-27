import string
import random

def generate_password():
    """
    Generates a random password based on user input for length.
    
    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password_length = int(input('How long would you like your password to be? '))
    
    # Shuffle the characters to make the password more random
    shuffled_characters = list(characters)
    random.shuffle(shuffled_characters)
    
    password = []
    
    # Select random characters from the shuffled list
    for _ in range(password_length):
        password.append(random.choice(shuffled_characters))
    
    # Shuffle the password characters again for added randomness
    random.shuffle(password)
    
    # Join the characters to form the password
    password = "".join(password)
    
    return password

if __name__ == "__main__":
    option = input('Do you want to generate a password? (Yes/No): ').lower()
    if option == 'yes':
        print(generate_password())
    elif option == 'no':
        print('See You Soon!')
    else:
        print('Invalid input, please type Yes/No')
