from abstractplayer import AbstractPlayer

from disk import Disk
from view import View
from board import Board

import random


class HumanPlayer(AbstractPlayer):

    def __init__(self, color):
        self.color = color
        super().__init__(color=color)

    def get_move(self, board, possible_moves):
        moves_text = "HumanPlayer" + "\t" + "It's your move\n" \
                                            "Your possible moves are: {}\n" \
                                            "Please choose your move row,col:".format(possible_moves)
        move = input(moves_text)
        return move


if __name__ == '__main__':
    board = Board(8)
    view = View(board_obj=board)

    pla_1 = HumanPlayer(Disk.DARK)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    num = [i for i in range(1, 9)]

    for i in range(10):
        move = random.choice(letters), random.choice(num)
        print(move)

        pla_1.get_move(board, move)
        view.viewing_game_board()
    # pla_1.get_move(board, ('b', 3))
    # view.viewing_game_board()
    #
    # pla_1.get_move(board, ('h', 3))
    # view.viewing_game_board()
    # pla_1.get_move(board, ('g', 7))
    # view.viewing_game_board()
