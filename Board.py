# to display the game board prettily
from tabulate import tabulate

# to make the game interactive from the terminal
from os import system


class Board:

    '''Create a board'''

    def __init__(self):
        '''Create an empty 3x3 Tic Tac Toe board'''

        self.board = [' ' for i in range(9)]

    def print_board(self):
        '''Display the 3x3 board prettily'''

        board = [self.board[i:i+3] for i in range(0, 9, 3)]

        system(command='clear')  # change this accordingly
        print(tabulate(tabular_data=[[1, 2, 3], [
              4, 5, 6], [7, 8, 9]], tablefmt='grid'))
        print('\n\n')

        print(tabulate(tabular_data=board, tablefmt='grid'))
        print('\n\n')

    def available_moves(self):
        '''Obtain all possible moves'''

        indices = []

        for idx in range(9):
            if self.board[idx] == ' ':
                indices.append(idx)

        return indices
