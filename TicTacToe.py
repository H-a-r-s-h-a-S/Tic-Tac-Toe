'''Play Tic Tac Toe and waste your time!'''


class TicTacToe:

    '''Start a Tic Tac Toe game'''

    def __init__(self, interactive=True):
        '''Is the game interactive?'''

        self.interactive = interactive

    def move(self, board, player, index):
        '''"player" places his symbol at "index" on the "board"'''

        if self.valid_move(board=board, index=index):
            board.board[index-1] = player.symbol

        else:
            print(value='invalid move. Try again!')
            player.get_move(board=board)

    def valid_move(self, board, index):
        '''Is a move at "index" valid in "board"?'''

        if index in range(1, 10):
            return board.board[index-1] == ' '

        else:
            return False

    def winner(self, board, symbol):
        '''Has the player with the "symbol" on "board" won?'''

        rows = [board.board[i:i+3] for i in range(0, 9, 3)]
        for row in rows:
            if row.count(symbol) == 3:
                return True

        cols = [board.board[i:i+7:3] for i in range(3)]
        for col in cols:
            if col.count(symbol) == 3:
                return True

        diag1 = [board.board[i] for i in (0, 4, 8)]
        if diag1.count(symbol) == 3:
            return True

        diag2 = [board.board[i] for i in (2, 4, 6)]
        if diag2.count(symbol) == 3:
            return True

        return False

    def game_over(self, board):
        '''Is the game over?'''

        if ' ' in board.board:
            if self.winner(board=board, symbol='X'):
                return True

            return self.winner(board=board, symbol='O')

        else:  # game has been tied
            return True

    def play(self, board, player1, player2):
        '''Start to play the game
board: Board being used to play the game
player1: The player who gets to move first
player2: The second player'''

        if self.interactive:
            board.print_board()

        current = player1

        while not self.game_over(board=board):

            idx = current.get_move(board=board)
            self.move(board=board, player=current, index=idx)

            if self.interactive:
                board.print_board()

            current = player2 if current == player1 else player1

        if self.winner(board=board, symbol='X'):
            return 1

        elif self.winner(board=board, symbol='O'):
            return -1

        else:
            return 0
