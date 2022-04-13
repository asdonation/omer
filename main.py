import pygame
import board
import game
import graphic
import position

def __main__():
    current_game = game.Game()
    current_graphic = graphic.Graphic()

    current_game.current_board.random_mid_game()
    current_game.current_board.random_mid_game()
    current_game.current_board.paint()

    display = current_graphic.screen
    while current_game.can_play():
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
        current_graphic.draw_board()
        # print(current_board.board_matrix)
        # move = current_game.get_user_move()
        # current_game.paint()
        current_graphic.draw_rectangle(current_game.current_board.board_matrix)
        current_graphic.press(event, current_game)
        pygame.display.flip()

__main__()


# import pygame
# import board
# import game
# import position
#
# def __main__():
#     current_board = board.Board()
#     current_game = game.Game()
#     current_game.random_mid_game2()
#     current_game.random_mid_game2()
#     current_game.paint()
#     while current_game.can_play():
#         move = current_game.get_user_move()
#         current_game.paint()
#
#
# __main__()