
import pygame
import sys
from game_board import Board
from automata import Line_Draw

pygame.init()

# define dimensions for game window
window_height = 800
window_width = 800

# set game mode using the dimensions we provide 
# (could possibly make this based on the resolution of the user's screen
# or add a full screen button)

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# fps in this case is the refresh rate
fps = 5
black = (0, 0, 0)
white = (245, 245, 245)

# Create board with paramaters defined above
board = Board(0, window_width, window_height, 25)

# Establish the size of the cells and board
cell_size = board.cell_size()
board_size = board.size()

# Create the aspect ratio of the cell
x = cell_size.width//2

# Draw using the Line_Draw class
line = Line_Draw()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    # Create a standard to measure fps with (in this case sys clock)
    dt = clock.tick(fps)
    # Fill the screen with a color
    screen.fill(white)
    # Draw grids
    board.draw_grid()
    # Draw aspect ratio'd cells
    line.draw(screen, x, cell_size.width, cell_size.height, 0, 3)
    # capture events
    handle_events()
    # Allow user to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if x >= board_size.width:
        x = cell_size.width//2
    else:
        x += cell_size.width

    # double buffers by default
    pygame.display.flip()