from board import Board
from disk import Disk


class View:
    """
            Represent Display Class - Roll of this obj
            1. Show The Game Table
            2. Get Input Move From User

    attr : board_obj that was set from outside
    """

    def __init__(self, board_obj):
        """

        :param board_obj: the instanse of Board Class
        """
        self.board_obj = board_obj

    def viewing_game_board(self):
        """

        :return: show the board
                    cheking if :   1 = Dark  --->  X
                                   2 = Light --->  Y
        """
        a_letter_ascii_num = ord("a")
        print("\t|", end=" ")
        for i in range(self.board_obj.size):
            print("{:^3}{:>2}".format(chr(a_letter_ascii_num + i), "|"), \
                  sep=" ", end=" ")
        print()
        print("-" * 59)
        for i in range(self.board_obj.size):
            print("{:^3}{:>2}".format(i + 1, "|"), sep=" ", end=" ")

            for j in range(self.board_obj.size):

                if self.board_obj.game_board[i][j] == Disk.DARK:
                    print("{:^3}{:>2}".format('X', "|"), \
                          sep=" ", end=" ")

                elif self.board_obj.game_board[i][j] == Disk.LIGHT:
                    print("{:^3}{:>2}".format('O', "|"), \
                          sep=" ", end=" ")
                else:
                    print("{:^3}{:>2}".format('', "|"), \
                          sep=" ", end=" ")
            print()


if __name__ == "__main__":
    board = Board(8)

    """
        Test function from board
    """
    board.update_board((1, 2), Disk.DARK)
    board.update_board((1, 3), Disk.LIGHT)

    d = View(board_obj=board)
    d.get_input_from_console(Disk.DARK)
    d.get_input_from_console(Disk.LIGHT)
    d.viewing_game_board()
