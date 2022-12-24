# to randomize the bot moves
from random import choice


class Player:
    def __init__(self, name, symbol):
        '''Create a Player'''
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f'"{self.name}"'

    def get_move(self, board):
        pass


class Bot(Player):

    '''Create a bot player'''

    def get_move(self, board):
        '''Generate a random position(index) for the game'''

        valid = board.available_moves()
        return choice(seq=valid) + 1


class Human(Player):

    '''Create a human player'''

    def get_move(self, board=None):
        '''Obtain a position(index) as input for the game'''

        idx = int(input('Enter position(1-9): '))

        return idx
