
import pygame
import sys
from game_board import Board
import message
from public_UI import *

pygame.init()

board = Board(0, window_width, window_height, None, 100)

pause = False

def paused():
    global pause
    board._user_interaction_enabled = True
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    board._user_interaction_enabled = True
                    unpause()
        board_size = board.size()

        pause_line_1 = message.message_display("Paused".upper(), screen, Position(board_size.width//2, board_size.height//2), red)
        #line 2
        message.message_display("(press 'p' to continue)", screen, Position(board_size.width//2, board_size.height//2 + pause_line_1.height), cyan)
        pygame.display.update()
        #clock.tick(15)

def unpause():
    global pause
    pause = False
    board._user_interaction_enabled = False

def handle_events():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                paused()
        if event.type == pygame.MOUSEBUTTONDOWN and pause == True and board._user_interaction_enabled == True:
                if event.button == 0:
                    mouse_pos = pygame.mouse.get_pos()
                    board.get_cell_num_for_pos(0, Position(mouse_pos[0], mouse_pos[1]))[0]._draw_circle()
                    board.grids[0][(board._number_of_cells*board._number_of_cells)//2]._draw_circle()
                    board.grids[0][(board._number_of_cells*board._number_of_cells)//2+1]._draw_circle()
                    board.grids[0][(board._number_of_cells*board._number_of_cells)//2+2]._draw_c

                    # board.grids[0][24]._draw_circle()
                    # board.grids[0][25]._draw_circle()
                    # board.grids[0][31]._draw_circle()
while True:
    dt = clock.tick(fps)

    screen.fill(white)
    board.increase_generation()

    board.draw_grid(board.active_grid)

    board.draw_grid(0)

    handle_events()
    
    # double buffers by default
    pygame.display.flip()