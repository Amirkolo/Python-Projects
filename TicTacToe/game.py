"""
Tic Tac Toe Game Module

This module provides a Tic Tac Toe game implementation along with utilities to play the game.

Classes:
    TicTacToe: Represents the Tic Tac Toe game.
"""

import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    """
    Represents a Tic Tac Toe game.

    Attributes:
        board (list): A list representing the 3x3 game board.
        current_winner (str): The current winner of the game.
    """

    def __init__(self):
        """Initializes the Tic Tac Toe game."""
        self.board = [' ' for _ in range(9)] # we will use a single list to represent a 3x3 board
        self.current_winner = None # keep track of winner
    
    def print_board(self):
        """Prints the current state of the game board."""
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """Prints the numbering guide for the game board."""
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + '|')

    def available_moves(self):
        """Returns a list of available moves on the game board."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """Checks if there are empty squares on the game board."""
        return ' ' in self.board
    
    def num_empty_squares(self):
        """Counts the number of empty squares on the game board."""
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        """
        Makes a move on the game board.

        Args:
            square (int): The index of the square to make the move.
            letter (str): The player's letter ('X' or 'O').

        Returns:
            bool: True if the move is made successfully, False otherwise.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True 
        return False

    def winner(self, square, letter):
        """
        Checks if a player has won the game.

        Args:
            square (int): The index of the square that was last filled.
            letter (str): The player's letter ('X' or 'O').

        Returns:
            bool: True if the player has won, False otherwise.
        """
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3 
        column = [self.board[col_ind+i*3] for i in range (3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    """
    Plays a game of Tic Tac Toe.

    Args:
        game (TicTacToe): The Tic Tac Toe game instance.
        x_player (Player): The player who plays as 'X'.
        o_player (Player): The player who plays as 'O'.
        print_game (bool, optional): Whether to print the game progress. Defaults to True.

    Returns:
        str: The winner of the game ('X' or 'O') or 'Tie' if the game ends in a tie.
    """
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        if print_game:
            time.sleep(1.2)
                
    if print_game:
        print("It's a tie!")
    return "Tie"

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After a thousand (1000) iterations, we see {x_wins} X win, {o_wins} O win, and {ties} draw!')
