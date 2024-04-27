"""
Sudoku Solver Module

This module provides functions to solve Sudoku puzzles.

Functions:
    find_next_empty: Finds the next empty cell in the Sudoku puzzle.
    is_valid: Checks if a guess is valid for a given cell in the Sudoku puzzle.
    solve_sudoku: Solves the Sudoku puzzle recursively.
"""


def find_next_empty(puzzle):
    """
    Finds the next empty cell in the Sudoku puzzle.

    Args:
        puzzle (list of lists): The Sudoku puzzle represented as a 9x9 grid.

    Returns:
        tuple: The row and column indices of the next empty cell. If no empty cell is found, returns (None, None).
    """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None


def is_valid(puzzle, guess, row, col):
    """
    Checks if a guess is valid for a given cell in the Sudoku puzzle.

    Args:
        puzzle (list of lists): The Sudoku puzzle represented as a 9x9 grid.
        guess (int): The number to be checked for validity.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        bool: True if the guess is valid for the cell, False otherwise.
    """
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    """
    Solves the Sudoku puzzle recursively.

    Args:
        puzzle (list of lists): The Sudoku puzzle represented as a 9x9 grid.

    Returns:
        bool: True if the puzzle is solved, False otherwise.
    """
    row, col = find_next_empty(puzzle)
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,    -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,    -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   -1, -1, 5,    -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,    2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
