from abstractplayer import AbstractPlayer
from random import randint


class RandomPlayer(AbstractPlayer):

    def __init__(self, color):
        super().__init__(color=color)

    def get_move(self, board, possible_moves):
        moves_text = "RandomPlayer" + "\t" + "It's your move\n" \
                                             "Your possible moves are: {}\n" \
                                             "Please choose your move row,col:".format(possible_moves)
        index = randint(0, len(possible_moves) - 1)
        move = moves_text + "{}".format(possible_moves[index])
        return move
