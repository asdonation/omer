import time
import board
import constant
import graphic


class Game:

    def __init__(self):
        self.current_board = board.Board()

    def can_play(self):
        return not self.is_lose() and not self.is_win()

    def is_win(self):
        if self.current_board.is_cell_contains(constant.win_number):
            print('win')
        return self.current_board.is_cell_contains(constant.win_number)

    def is_lose(self):
        if self.current_board.lose_condition1():
            print('lose')
        return self.current_board.lose_condition1()

    def random_mid_game2(self):
        self.current_board.random_mid_game()

    def paint(self):
        self.current_board.paint()

    def get_user_move(self):
        move_input = str(input(print("Enter 'w' / 's' / 'd' / 'a' ")))
        if move_input not in ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D']:
            return self.get_user_move()
        elif move_input in ['w', 'W']:  # TODO: handle case when 2 tiles are equals
            return self.move_up()
        elif move_input in ['a', 'A']:
            return self.move_left()
        elif move_input in ['s', 'S']:
            return self.move_down()
        elif move_input in ['d', 'D']:
            return self.move_right()

    def move_right(self):
        self.general_move(constant.full_range, range(2, -1, -1), 0, +1)

    def move_left(self):
        self.general_move(constant.full_range, range(1, 4), 0, -1)

    def move_up(self):
        self.general_move(range(1, 4), constant.full_range, -1, 0)

    def move_down(self):
        self.general_move(range(2, -1, -1), constant.full_range, +1, 0)

    def general_move(self, row_range_arr, col_range_arr, row_addition, col_addition):
        changed_something = False
        if col_addition == 0:
            for j in col_range_arr:
                for i in row_range_arr:
                    changed_something = self.general_move_iteration(col_addition, i, j,
                                                                    row_addition) or changed_something
        else:
            for i in row_range_arr:
                for j in col_range_arr:
                    changed_something = self.general_move_iteration(col_addition, i, j,
                                                                    row_addition) or changed_something
        # Generate new number on board for next turn
        if changed_something:
            self.current_board.random_mid_game()

    def general_move_iteration(self, col_addition, i, j, row_addition):
        changed = False
        skip = False
        while not skip and not j + col_addition >= constant.board_size and not i + row_addition >= constant.board_size and \
                not j + col_addition < 0 and not i + row_addition < 0 and \
                (self.current_board.board_matrix[i][j] == self.current_board.board_matrix[i + row_addition][
                    j + col_addition] or \
                 self.current_board.board_matrix[i + row_addition][j + col_addition] == constant.empty_cell):
            if self.current_board.board_matrix[i][j] == constant.empty_cell:
                skip = True
            elif self.current_board.board_matrix[i + row_addition][j + col_addition] == constant.empty_cell \
                    and j + col_addition < constant.board_size and i + row_addition < constant.board_size:
                self.current_board.board_matrix[i + row_addition][j + col_addition] = \
                    self.current_board.board_matrix[i][j]
                self.current_board.board_matrix[i][j] = 0
                j += col_addition
                i += row_addition
                changed = True
            elif self.current_board.board_matrix[i][j] == self.current_board.board_matrix[i + row_addition][
                j + col_addition]:
                self.current_board.board_matrix[i][j] = 0
                self.current_board.board_matrix[i + row_addition][j + col_addition] = \
                    self.current_board.board_matrix[i + row_addition][j + col_addition] * 2
                changed = True
            else:
                skip = True
        return changed
