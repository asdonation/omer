import pygame
import constant
import game
import board
import graphic


class Graphic:

    def __init__(self):
        self.right = pygame.K_RIGHT
        self.graphic_matrix_board = []
        for row in range(board.board_size):
            lst = []
            self.graphic_matrix_board.append(lst)
            for col in range(board.board_size):
                lst.append(0)

        self.square2 = pygame.image.load('2.png')
        self.square2 = pygame.transform.scale(self.square2, (90, 90))

        self.square4 = pygame.image.load('4.png')
        self.square4 = pygame.transform.scale(self.square4, (90, 90))

        self.square8 = pygame.image.load('8.png')
        self.square8 = pygame.transform.scale(self.square8, (90, 90))

        self.square16 = pygame.image.load('16.png')
        self.square16 = pygame.transform.scale(self.square16, (90, 90))

        self.square32 = pygame.image.load('32.png')
        self.square32 = pygame.transform.scale(self.square32, (90, 90))

        self.square64 = pygame.image.load('64.png')
        self.square64 = pygame.transform.scale(self.square64, (90, 90))

        self.square128 = pygame.image.load('128.png')
        self.square128 = pygame.transform.scale(self.square128, (90, 90))

        self.square256 = pygame.image.load('256.png')
        self.square256 = pygame.transform.scale(self.square256, (90, 90))

        self.square512 = pygame.image.load('512.png')
        self.square512 = pygame.transform.scale(self.square512, (90, 90))

        self.square1024 = pygame.image.load('1024.png')
        self.square1024 = pygame.transform.scale(self.square1024, (90, 90))

        self.square2048 = pygame.image.load('1024.png')
        self.square2048 = pygame.transform.scale(self.square2048, (90, 90))

        self.screen = pygame.display.set_mode((constant.window_width, constant.window_height))
        self.squares = [self.square2, self.square4, self.square8, self.square16, self.square32, self.square64,
                    self.square128, self.square256, self.square512, self.square1024, self.square2048]

    def graphic_display(self):

        return self.screen

    def draw_board(self):
        self.screen.fill(constant.white)
        pygame.draw.rect(self.screen, (84, 84, 84), (200, 200, 400, 400))
        pygame.draw.line(self.screen, constant.black, (200, 200), (200, 600), 5)
        pygame.draw.line(self.screen, constant.black, (300, 200), (300, 600), 5)
        pygame.draw.line(self.screen, constant.black, (400, 200), (400, 600), 5)
        pygame.draw.line(self.screen, constant.black, (500, 200), (500, 600), 5)
        pygame.draw.line(self.screen, constant.black, (600, 200), (600, 600), 5)
        pygame.draw.line(self.screen, constant.black, (200, 200), (600, 200), 5)
        pygame.draw.line(self.screen, constant.black, (200, 300), (600, 300), 5)
        pygame.draw.line(self.screen, constant.black, (200, 400), (600, 400), 5)
        pygame.draw.line(self.screen, constant.black, (200, 500), (600, 500), 5)
        pygame.draw.line(self.screen, constant.black, (200, 600), (600, 600), 5)

    @staticmethod
    def calculate_index(num):
        division_num = 0
        while num > 0:
            num //= 2
            division_num += 1
        return division_num - 2

    def draw_rectangle(self, board_matrix):
        for i in range(board.board_size):
            for j in range(board.board_size):
                if board_matrix[i][j] > 0:
                    self.screen.blit(self.squares[self.calculate_index(board_matrix[i][j])], (205 + 100 * j, 205 + 100 * i))

    def press(self, event, game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # print (list(self))
                game.move_right()
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_UP:
                game.move_up()
            if event.key == pygame.K_DOWN:
                game.move_down()



