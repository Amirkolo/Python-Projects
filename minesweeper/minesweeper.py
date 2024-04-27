"""
Minesweeper Game

A simple command-line version of the Minesweeper game.
"""

import random
import re


class Board:
    """
    Class representing the Minesweeper game board.
    """

    def __init__(self, dim_size, num_bombs):
        """
        Initialize the Minesweeper board.

        Args:
        dim_size (int): The dimension size of the square board.
        num_bombs (int): The number of bombs to be placed on the board.

        Attributes:
        dim_size (int): The dimension size of the square board.
        num_bombs (int): The number of bombs on the board.
        board (list): 2D list representing the Minesweeper board.
        dug (set): Set of coordinates that have been dug by the player.
        """
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        """
        Create a new empty Minesweeper board.

        Returns:
        list: 2D list representing the empty Minesweeper board.
        """
        return [[' ' for _ in range(self.dim_size)]
                for _ in range(self.dim_size)]

    def assign_values_to_board(self):
        """
        Randomly place bombs on the board and assign values to non-bomb cells.
        """
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            location = random.randint(0, self.dim_size**2 - 1)
            row = location // self.dim_size
            column = location % self.dim_size

            if self.board[row][column] == '*':
                continue

            self.board[row][column] = '*'
            bombs_planted += 1

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.num_neighboring_bombs(r, c)

    def num_neighboring_bombs(self, row, column):
        """
        Count the number of neighboring bombs for a given cell.

        Args:
        row (int): The row index of the cell.
        column (int): The column index of the cell.

        Returns:
        int: The number of neighboring bombs.
        """
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, column-1), min(self.dim_size - 1, (column+1)) + 1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, column):
        """
        Dig a cell on the Minesweeper board.

        Args:
        row (int): The row index of the cell to be dug.
        column (int): The column index of the cell to be dug.

        Returns:
        bool: True if the dig is successful, False if a bomb is encountered.
        """
        if (row, column) in self.dug:
            return True

        self.dug.add((row, column))

        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, column-1), min(self.dim_size - 1, (column+1)) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        """
        Get a string representation of the visible board.

        Returns:
        str: The string representation of the visible board.
        """
        visible_board = [[' ' for _ in range(self.dim_size)]
                         for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for column in range(self.dim_size):
                if (row, column) in self.dug:
                    visible_board[row][column] = str(self.board[row][column])
                else:
                    visible_board[row][column] = ' '
        return '\n'.join([' '.join(row) for row in visible_board])


def play(dim_size=10, num_bombs=10):
    """
    Play the Minesweeper game.

    Args:
    dim_size (int): The dimension size of the square board (default is 10).
    num_bombs (int): The number of bombs on the board (default is 10).
    """
    board = Board(dim_size, num_bombs)
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',
                              input('Where would you like to dig? Input as row, column: '))
        row, column = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.dim_size or column < 0 or column >= board.dim_size:
            print('Invalid location. Try again')
            continue

        safe = board.dig(row, column)

        if not safe:
            break

    print(board)

    if safe:
        print('Congrats, you are safe')
    else:
        print('SORRY. GAME OVER!!!')


if __name__ == "__main__":
    play()
