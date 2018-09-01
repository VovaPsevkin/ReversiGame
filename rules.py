from board import Board
from disk import Disk
from view import View


class Rules:
    """
        check the valid moves to player
        make list of possible moves --> chip_opponent_to_convert

    """

    def __init__(self, board_obj):
        self.board_object = board_obj

    def is_ligal_move(self, move, color):
        """
            Check of admissibility of a move
            Checking each of the eight directions
            Determining the presence of chips that can be flipped
        :param move: str
        :param color:
        :return: True or False and list of possible moves
        """
        x_initial, y_initial = move.split(',')
        x_initial, y_initial = ord(x_initial) - ord('a'), int(y_initial) - 1

        # checks is the empty ceil
        # and whether the coordinates x and y belong to the game field
        if self.board_object.game_board[x_initial][y_initial] != Disk.NONE \
                or not self.is_on_board(x_initial, y_initial):
            return False

        # This func should also be known opponent 's chip. If the player's
        # color Dark, then, obviously, the opponent's color Light and vice versa
        if color == Disk.DARK:
            color_other_player = Disk.LIGHT
        else:
            color_other_player = Disk.DARK

        # list of all the opponent's chips that will be reversed in this turn.
        chip_opponent_to_convert = []

        # Checking each of the eight directions
        # For a move to be acceptable, the player must turn at least one of the
        # opponent's chips, holding it between the new chip and one of its old chips.
        # This means that the new chip should be next to one of the chips enemy.

        # Performs a search of the list of lists containing directions in which the
        # program will check the opponent's chip
        step_moves = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for x_direction, y_direction in step_moves:

            x, y = x_initial, y_initial
            x += x_direction  # the first step in the direction x
            y += y_direction  # the first step in the direction x

            while self.is_on_board(x, y) \
                    and self.board_object.game_board[x][y] == color_other_player:
                # Continue to move in this direction x and y
                x += x_direction
                y += y_direction

                # There are chips that can be turned over.
                # Move in the opposite direction to reaching the original cell,
                # noting all the chips along the way.
                if self.is_on_board(x, y) \
                        and self.board_object.game_board[x][y] == color:
                    # the while loop moves x and y in the opposite direction.
                    # Until x and y return to the original xstart and ystart (x_init... and y_init...)
                    while True:
                        x -= x_direction
                        y -= y_direction
                        # check if the coordinate of your own the player's chip
                        if x == x_initial and y == y_initial:
                            break
                        move = str(chr(x + ord('a'))) + ',' + str(y)
                        chip_opponent_to_convert.append(move)
        # If none of the opponent's chips has turned over in any of the eighth
        # then chip_opponent_to_convert will be an empty list.
        if len(chip_opponent_to_convert) == 0:
            return False
        # This is a sign that such a move is not valid, and the function is_valid_move()
        # should return False.Otherwise, the function is_valid_move() returns chip_opponent_to_convert
        return chip_opponent_to_convert

    def is_on_board(self, x, y):
        """
          Assistance / Service func to is_valid_move func
          It performs a simple check
          If the given x and y coordinates are within the playing field.
        :param x: Width of table
        :param y: Height
        :return: True or False
        """
        return (x >= 0 and x < self.board_object.size
                and y >= 0 and y < self.board_object.size)

    def get_valid_moves(self, color):
        """

        :param color: Disk Enum
        :return: list of tuples with possible moves for player
        """
        valid_moves = []
        for x in range(self.board_object.size):
            for y in range(self.board_object.size):
                move = (str(chr(x + ord('a'))) + ',' + str(y))
                if self.is_ligal_move(move=move, color=color):
                    valid_moves.append(move)

        return valid_moves


if __name__ == "__main__":
    board_obj = Board(8)
    v = View(board_obj=board_obj)
    v.viewing_game_board()
    rules = Rules(board_obj)
    print(rules.get_valid_moves(Disk.DARK))
    # print(rules.is_ligal_move(('c,4'), Disk.LIGHT))
    # print(rules.is_ligal_move(('e,6'), Disk.LIGHT))
    # print(rules.is_ligal_move(('d,3'), Disk.LIGHT))
    # print(rules.is_ligal_move(('f,5'), Disk.LIGHT))
