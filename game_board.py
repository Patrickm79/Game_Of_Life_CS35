import pygame
import random
import message
from message import Position
from automata import GridCell
from public_UI import Position, white, black


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
        self.active_grid = 0
        self.__init_grids__()
        self.draw_grid(self.active_grid)

    def inactive_grid(self):
        # since the board is either 1 or 0, active_grid+1%2 will always return the inverse
        return (self.active_grid +1) %2

    def get_cell_num_for_pos(self, grid_num, position=Position(0,0)):
        row = position.x//self.cell_size().width
        column = position.y//self.cell_size().height

        cell = self.grids[grid_num][(self._number_of_cells*row)+column]
        if cell.drawn == True:
            print(f"row: {row}, column: {column}, index: {(self._number_of_cells*row)+column}")

        return (cell,(self._number_of_cells*row)+column)

    def size(self):
        return self._size

    def cell_size(self):
        return Size(self._size.width//self._number_of_cells, self._size.height//self._number_of_cells)

    def get_generation(self):
        return self._generation


    def check_cell_neighbors(self, cell):
        if cell.drawn == True:
            cell_index = self.get_cell_num_for_pos(self.active_grid, Position(cell.x, cell.y))[1]
            if cell_index > 0:
                north_neighbor = self.grids[self.active_grid][cell_index-1]
                north_neighbor._draw_circle()
            # if cell_index < len(self.grids[self.active_grid])-1:
            #     south_neighbor = self.grids[self.active_grid][cell_index+1]
            #     south_neighbor._draw_circle()

        #if cell.alive == False and cell.neighbors ==3:
            #cell.resurrect()
        #if cell.neighbors in range(2,4) and cell.alive == True: #cell has 2 or 3 neighbors
            #Do Nothing
        #if cell.neighbors < 2 or cell.neighbors >3: 
            #cell.kill()
        return cell

    def increase_generation(self):
        self._generation += 1

        for index in range(self._number_of_cells*self._number_of_cells):
            cell = self.grids[self.active_grid][index]

            next_generation = self.check_cell_neighbors(cell)

            self.grids[self.inactive_grid()][index] = next_generation        
        self.active_grid = self.inactive_grid()

    def is_interactable(self):
        return self._user_interaction_enabled

    def __init_grids__(self):
        """init grits[0] active and grids[1] inactive"""

        self.grids = [
            [None for x in range(self._number_of_cells*self._number_of_cells)],
            [None for x in range(self._number_of_cells*self._number_of_cells)]
        ]
        self.active_grid = 0
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

    def draw_grid(self, grid_num, choice=None):
        self.increase_generation()

        from game import window_height
        from game import window_width
        from game import screen
        from game import black

        self._user_interaction_enabled = False

        for grid in self.grids[grid_num]:
            grid.draw()
            draw = random.choice([0,1])
            if draw == 1:
                grid._draw_circle()
            else:
                grid._clear_circle()

        self.draw_status_bar(screen)


        # self.get_cell_num_for_pos(0, (Position(self.size().width//2, self.size().height//2)))._draw_circle()
        # self.get_cell_num_for_pos(0, (Position(0, 0)))._draw_circle()

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