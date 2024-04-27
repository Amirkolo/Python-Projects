def replace_word():
    """
    Replace a word in a given string with another word.

    This function prompts the user to enter a string, a word to replace in that string,
    and the replacement word. It then replaces all occurrences of the word to replace
    with the replacement word and prints the modified string.

    Parameters: None

    Returns: None
    """
    input_str = 'Hi guys, I am Amir. and I would to have coffee with you'
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(input_str.replace(word_to_replace, word_replacement))

if __name__ == "__main__":
    replace_word()
