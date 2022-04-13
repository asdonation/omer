import board
import constant
import random
import position
import sys

board_size = 4


class Board:
    def __init__(self):
        random.seed()
        self.board_matrix = []
        for row in range(board_size):
            lst = []
            self.board_matrix.append(lst)
            for col in range(board_size):
                lst.append(0)

        # self.board_matrix[0][0] = 2
        # self.board_matrix[0][1] = 4
        # self.board_matrix[0][2] = 8
        # self.board_matrix[0][3] = 2
        # self.board_matrix[1][0] = 64
        # self.board_matrix[1][1] = 128
        # self.board_matrix[1][2] = 16
        # self.board_matrix[1][3] = 0
        # self.board_matrix[2][0] = 2
        # self.board_matrix[2][1] = 4
        # self.board_matrix[2][2] = 2
        # self.board_matrix[2][3] = 8
        # self.board_matrix[3][0] = 2
        # self.board_matrix[3][1] = 64
        self.board_matrix[3][2] = 1024
        self.board_matrix[3][3] = 1024
        # self.random_mid_game()
        # self.random_mid_game()

    def is_cell_contains(self, num):

        for i in range(board_size):
            for j in range(board_size):
                if self.board_matrix[i][j] == num:
                    return True
        return False

    def can_move(self):
        if not self.lose_condition1():
            return True
        return False

    def paint(self):

        for i in range(board_size):
            for j in range(board_size):
                print(self.board_matrix[i][j], end='   ')
                if j == board_size - 1:
                    # move down one line
                    print('\n')

    def lose_condition1(self):
        if self.is_cell_contains(constant.empty_cell):
            return False
        for i in range(board_size):
            for j in range(3):
                if self.board_matrix[i][j] == self.board_matrix[i][j+1]:
                    return False
        for i in range(3):
            for j in range(board_size):
                if self.board_matrix[i][j] == self.board_matrix[i + 1][j]:
                    return False
        return True

    def random_mid_game(self):
        pos1 = random.randrange(board_size)
        pos2 = random.randrange(board_size)
        while self.board_matrix[pos1][pos2] != 0:
            pos1 = random.randrange(board_size)
            pos2 = random.randrange(board_size)
        self.board_matrix[pos1][pos2] = random.randrange(2, 5, 2)
