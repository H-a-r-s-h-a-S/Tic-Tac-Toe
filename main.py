from Players import Human, Bot
from Board import Board
from TicTacToe import TicTacToe


player_name = input('Enter your name: ')
you = Human(name=player_name, symbol='X')
bot = Bot(name='Martin', symbol='O')
board = Board()
t = TicTacToe(interactive=True)

res = t.play(board=board, player1=you, player2=bot)

if res == 1:
    print(you, 'has won!')
elif res == -1:
    print(bot, 'has won!')
else:
    print('The game is drawn')
