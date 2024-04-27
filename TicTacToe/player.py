"""
Tic Tac Toe Player Module

This module provides classes representing different types of players in a Tic Tac Toe game.

Classes:
    Player: Represents a generic player.
    RandomComputerPlayer: Represents a computer player making random moves.
    HumanPlayer: Represents a human player.
    GeniusComputerPlayer: Represents a computer player using the minimax algorithm to make intelligent moves.
"""

import math
import random

class Player:
    """
    Represents a generic player.

    Attributes:
        letter (str): The letter representing the player ('X' or 'O').
    """

    def __init__(self, letter):
        """
        Initializes a player with a given letter.

        Args:
            letter (str): The letter representing the player ('X' or 'O').
        """
        self.letter = letter

    def get_move(self, game):
        """
        Gets the player's next move given the current state of the game.

        This method needs to be implemented by subclasses.

        Args:
            game (TicTacToe): The Tic Tac Toe game instance.

        Returns:
            int: The index of the square for the player's next move.
        """
        pass

class RandomComputerPlayer(Player):
    """
    Represents a computer player making random moves.
    """

    def __init__(self, letter):
        """
        Initializes a random computer player with a given letter.

        Args:
            letter (str): The letter representing the player ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """
        Gets the random computer player's next move.

        Args:
            game (TicTacToe): The Tic Tac Toe game instance.

        Returns:
            int: The index of the square for the random move.
        """
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    """
    Represents a human player.
    """

    def __init__(self, letter):
        """
        Initializes a human player with a given letter.

        Args:
            letter (str): The letter representing the player ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """
        Gets the human player's next move through user input.

        Args:
            game (TicTacToe): The Tic Tac Toe game instance.

        Returns:
            int: The index of the square for the player's move entered by the user.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square, try again.')

        return val
        
class GeniusComputerPlayer(Player):
    """
    Represents a computer player using the minimax algorithm to make intelligent moves.
    """

    def __init__(self, letter):
        """
        Initializes a genius computer player with a given letter.

        Args:
            letter (str): The letter representing the player ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """
        Gets the genius computer player's next move using the minimax algorithm.

        Args:
            game (TicTacToe): The Tic Tac Toe game instance.

        Returns:
            int: The index of the square for the intelligent move.
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        """
        Implements the minimax algorithm to determine the best move for the player.

        Args:
            state (TicTacToe): The current state of the Tic Tac Toe game.
            player (str): The letter representing the player ('X' or 'O').

        Returns:
            dict: A dictionary containing the best move's position and the corresponding score.
        """
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1
                )
            }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else: 
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] =' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best
