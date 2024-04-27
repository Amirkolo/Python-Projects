import random

def roll_dice():
    """
    Simulate rolling two dice and display their outcomes.

    This function prompts the user to roll two dice. It generates random numbers for each die,
    displays the corresponding dice drawings, and prints the outcome of each die roll.

    Parameters: None

    Returns: None
    """
    # Define a dictionary to store dice side representations
    dice_faces = {
        1: """
        +-------+
        |       |
        |   *   |
        |       |
        +-------+
        """,
        2: """
        +-------+
        | *     |
        |       |
        |     * |
        +-------+
        """,
        3: """
        +-------+
        | *     |
        |   *   |
        |     * |
        +-------+
        """,
        4: """
        +-------+
        | *   * |
        |       |
        | *   * |
        +-------+
        """,
        5: """
        +-------+
        | *   * |
        |   *   |
        | *   * |
        +-------+
        """,
        6: """
        +-------+
        | *   * |
        | *   * |
        | *   * |
        +-------+
        """
    }

    roll = input('Roll the dice? (Yes/No): ')

    while roll.lower() == "yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        # Print the dice drawings using the dictionary
        print(dice_faces[dice1])
        print(dice_faces[dice2])

        print('Dice rolled: {} and {}'.format(dice1, dice2))

        roll = input('Roll again? (Yes/No): ')

if __name__ == "__main__":
    roll_dice()
