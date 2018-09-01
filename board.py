from disk import Disk
from random import randint


class Board:
    """
            Represent Board Class - Roll of This obj
            1. Create Game Table
            2. Update Game Table
            3. Count Disks on Game Table
    attr:  size of board int
    attr:  list of lists that create by set_table func

    """

    def __init__(self, size):
        self.size = size
        self.set_table()

    def set_table(self):
        """
            Create Starting Board and game_board attr
        """
        self.game_board = [[Disk.NONE for j in range(self.size)] for i in range(self.size)]
        self.game_board[self.size // 2][self.size // 2] = Disk.DARK
        self.game_board[self.size // 2 - 1][self.size // 2 - 1] = Disk.DARK
        self.game_board[self.size // 2 - 1][self.size // 2] = Disk.LIGHT
        self.game_board[self.size // 2][self.size // 2 - 1] = Disk.LIGHT

    def count_of_disks(self):
        """
        :return: dictionary of scores
        """
        dark_counter = 0
        light_counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.game_board[i][j] == Disk.DARK:
                    dark_counter += 1
                elif self.game_board[i][j] == Disk.LIGHT:
                    light_counter += 1
        total_count_of_disks = {"Dark Disks": dark_counter, \
                                "Light Disks": light_counter}

        return total_count_of_disks

    def update_board(self, move, color):
        """
        :param move: str or int
        :param color: Disk instanse
        :return: update the game_board
        """

        x, y = move.split(',')
        x, y = ord(x) - ord('a'), int(y) - 1

        try:
            self.game_board[y][x] = color
        except Exception:
            raise IndexError("The move illegal")


if __name__ == "__main__":
    """
        Cheking The Board Class
         method update_board , view game_board_matrix 
    """
    board = Board(8)
    for i in range(8):
        for j in range(8):
            board.update_board((randint(0, 7), randint(0, 7)), Disk.DARK)
            print(board.game_board[i][j])
