from board import Board
from disk import Disk
from view import View
from myplayer import HumanPlayer
from randomplayer import RandomPlayer
from rules import Rules


class Game:

    def __init__(self):
        self.games_board = Board(8)
        self.game_view = View(self.games_board)
        self.rules_game = Rules(self.games_board)

        self.player_one = HumanPlayer(Disk.DARK)
        self.player_two = RandomPlayer(Disk.LIGHT)

    def play_game(self):
        self.current_player = self.player_one
        self.game_view.viewing_game_board()

        while self.rules_game.get_valid_moves(self.current_player.color):
            possible_moves = self.rules_game.get_valid_moves(self.current_player.color)
            move = self.player_one.get_move(self.games_board, possible_moves=possible_moves)
            self.update_move(move=move, color=self.current_player.color)
            self.game_view.viewing_game_board()
            self.convert_opponent_chips(move=move, color=self.current_player.color)
            self.game_view.viewing_game_board()
            self.current_player = self.switch_players()

    def switch_players(self):
        """

        :return:
        """
        # 5 if a > 7 else 0
        return self.player_two if self.current_player == self.player_one \
            else self.player_one

    def convert_opponent_chips(self, move, color):
        """
            convert all disks
        :param move: the move of Player
        :param color: The color of Player
        :return:
        """
        for item in self.rules_game.is_ligal_move(move=move, color=color):
            x, y = item.split(',')
            x, y = ord(x) - ord('a'), int(y)
            self.games_board.game_board[y][x] = color

    def update_move(self, move, color):
        """
            upadate the board use the Board obj function
        :param move: the move of Player
        :param color: The color of Player
        :return:
        """
        print(self.rules_game.is_ligal_move(move=move, color=color))
        self.games_board.update_board(move, color)


if __name__ == "__main__":
    game = Game()
    game.play_game()
