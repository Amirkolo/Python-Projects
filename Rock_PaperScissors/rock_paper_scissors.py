"""
Rock Paper Scissors Game

This program allows the user to play the Rock Paper Scissors game against the computer.

Functions:
    play: Allows the user to play the game.
    is_win: Checks if the player wins against the opponent.
"""

import random

def play():
    """
    Allows the user to play the Rock Paper Scissors game against the computer.

    Returns:
        str: The result of the game ('You won', 'You lost', or "It's a tie").
    """
    user = input("WHAT IS YOUR CHOICE? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return 'You won'
    
    return 'You lost'

def is_win(player, opponent):
    """
    Checks if the player wins against the opponent in Rock Paper Scissors.

    Args:
        player (str): The choice of the player ('r' for rock, 'p' for paper, 's' for scissors).
        opponent (str): The choice of the opponent.

    Returns:
        bool: True if the player wins, False otherwise.
    """
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True

print(play())
