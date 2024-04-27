def generate_madlib():
    """
    Generate a madlib based on user input.

    This function prompts the user to input an adjective, two verbs, and a famous person's name.
    It then generates a madlib using the provided inputs and prints the result.

    Parameters: None

    Returns: None
    """
    # string concatenation (putting strings together)
    # let's create a string that says "subscribe to"
    youtuber = "Klie Yang"  # (KY being the string variable)

    # ways to do this
    # print (f "subscribe to {}")

    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")

    madlib = f"Computer programming is so {adj}! It makes me so excited because " \
             f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    print(madlib)

if __name__ == "__main__":
    generate_madlib()
