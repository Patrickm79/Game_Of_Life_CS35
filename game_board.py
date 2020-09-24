import pygame
import message
from message import Position
from automata import GridCell


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Board:
    def __init__(self, generation, window_width, window_height, number_of_cells=25):
        self._generation = generation
        self._user_interaction_enabled = True
        self._number_of_cells = number_of_cells
        self.status_bar_height = 80
        self._size = Size(window_width, window_height-self.status_bar_height)
        self.__init_grids__()

    def get_cell_num_for_pos(self, grid_num, position=Position(0,0)):
        row = position.x//self.cell_size().width
        column = position.y//self.cell_size().height
        # TODO: change grid to be dynamic
        return (self.grids[grid_num][(self._number_of_cells*row)+column])

    def size(self):
        return self._size

    def cell_size(self):
        return Size(self._size.width//self._number_of_cells, self._size.height//self._number_of_cells)

    def get_generation(self):
        return self._generation

    def increase_generation(self):
        self._generation += 1

    def is_interactable(self):
        return self._user_interaction_enabled

    def __init_grids__(self):
        """init grits[0] active and grids[1] inactive"""

        self.grids = [
            [None for x in range(self._number_of_cells*self._number_of_cells)],
            [None for x in range(self._number_of_cells*self._number_of_cells)]
        ]
        # fill array with cells        
        for x in range(self._number_of_cells):            
            for y in range(self._number_of_cells):
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, 
                self.cell_size().width, self.cell_size().height)

                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height,
                self.cell_size().width, self.cell_size().height)

                self.grids[0][(self._number_of_cells*x)+y] = rect
                self.grids[1][(self._number_of_cells*x)+y] = rect

    def set_board_size(self, number_of_cells):
        self._number_of_cells = number_of_cells
        self._cell_size = number_of_cells

    def draw_grid(self, num):
        self.increase_generation()

        from game import window_height
        from game import window_width
        from game import screen
        from game import black

        self._user_interaction_enabled = False

        for grid in self.grids[num]:
            grid.draw()
        self.draw_status_bar(screen)
        self.get_cell_num_for_pos(0, (Position(self.size().width//2, self.size().height//2)))._draw_circle()
        self.get_cell_num_for_pos(0, (Position(0, 0)))._draw_circle()

    def draw_status_bar(self, screen):
        from game import white
        from message import draw_button

        pygame.display.set_caption(f"Conway's Game of Life")

        status_bar = pygame.Surface((self._size.width, self.status_bar_height))

        status_bar.fill(white)

        message.message_display(f"Generation: {self._generation}", status_bar, 
        Position(status_bar.get_rect().width, status_bar.get_rect().height))

        test_button = draw_button("test", (0,0), status_bar, (255,0,0), fill_color=(255,0,0), text_color = white)

        screen.blit(status_bar, (0, self._size.height)) 

        pygame.display.set_caption(f"Generation: {self._generation}")
        # Move to lower right under grid, and option to change window size, cells, etc.