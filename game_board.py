import pygame
import random
import message
from message import Position
from automata import GridCell
from public_UI import Position, white, black, Size, screen
from copy import copy

class Board:
    def __init__(self, generation, window_width, window_height, board_style=0, number_of_cells=25):
        self._generation = generation
        self._user_interaction_enabled = True
        self._number_of_cells = number_of_cells
        self.status_bar_height = 80
        self._size = Size(window_width, window_height-self.status_bar_height)
        self.active_grid = 0
        self.__init_grids__()
        self.set_active_grid(board_style)
        self.draw_grid(self.active_grid)

    def __str__(self):
        return(f"board#: {self.active_grid}, width: {self.size().width}, height: {self.size().height},  with number of cells(sq): {self._number_of_cells}")

    def __init_grids__(self):
        self.grids = [
            [None for x in range(self._number_of_cells*self._number_of_cells)],
            [None for x in range(self._number_of_cells*self._number_of_cells)]
        ]        
        for x in range(self._number_of_cells):            
            for y in range(self._number_of_cells):
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                self.grids[0][(self._number_of_cells*x)+y] = rect
                #self.grids[1][(self._number_of_cells*x)+y] = rect

    def inactive_grid(self):
        return (self.active_grid +1) %2

    def size(self):
        return self._size

    def cell_size(self):
        return Size(self._size.width//self._number_of_cells, self._size.height//self._number_of_cells)

    def get_generation(self):
        return self._generation

    def get_cell_num_for_pos(self, grid_num, position=Position(0,0)):
        column = position.x//self.cell_size().width
        row = position.y//self.cell_size().height
        cell_index = (self._number_of_cells*column)+row

        try:
            cell = self.grids[grid_num][cell_index]

            if cell.is_alive():
                print(f"row: {row}, column: {column}, index: {cell_index}")

        except IndexError:
            cell = None
            print(f"No cell num for {position}")
        return (cell, cell_index)

    def check_cell_neighbors(self, cell):
        cell_index = self.get_cell_num_for_pos(self.active_grid, Position(cell.x, cell.y))[1]
        neighbor_list = []
        cell.neighbors = 0

        north = Position(cell.x, cell.y - self.cell_size().height)
        south = Position(cell.x, cell.y + self.cell_size().height)
        east = Position(cell.x + self.cell_size().width, cell.y)
        west = Position(cell.x - self.cell_size().width, cell.y)

        north_east = Position(east.x, north.y)
        north_west = Position(west.x, north.y)
        south_east = Position(east.x, south.y)
        south_west = Position(west.x, south.y)

        north_neighbor = self.get_cell_num_for_pos(self.active_grid, north)[0]

        if north_neighbor is not None and north_neighbor.is_alive():
            print(f"my index: {cell_index}, north neighbor index: {self.get_cell_num_for_pos(self.active_grid, north)[1]}")

        south_neighbor = self.get_cell_num_for_pos(self.active_grid, south)[0]

        if south_neighbor is not None and south_neighbor.is_alive():
            print(f"my index: {cell_index}, south neighbor index: {self.get_cell_num_for_pos(self.active_grid, south)[1]}")

        east_neighbor = self.get_cell_num_for_pos(self.active_grid, east)[0]
        if cell.is_alive():
            print(f"east neighbor index: {self.get_cell_num_for_pos(self.active_grid, east)[1]}")
        west_neighbor = self.get_cell_num_for_pos(self.active_grid, west)[0]
        if cell.is_alive():
            print(f"west neighbor index: {self.get_cell_num_for_pos(self.active_grid, west)[1]}")

        east_neighbor = self.get_cell_num_for_pos(self.active_grid, east)[0]        
        if east_neighbor is not None and east_neighbor.is_alive():
           print(f"my index: {cell_index}, east neighbor index: {self.get_cell_num_for_pos(self.active_grid, east)[1]}")

        west_neighbor = self.get_cell_num_for_pos(self.active_grid, west)[0]
        if west_neighbor.is_alive() and west_neighbor is not None:
            print(f"my index: {cell_index}, west neighbor index: {self.get_cell_num_for_pos(self.active_grid, west)[1]}")

        north_east_neighbor = self.get_cell_num_for_pos(self.active_grid, north_east)[0]
        if north_east_neighbor is not None and north_east_neighbor.is_alive():
            print(f"my index: {cell_index}, north_east neighbor index: {self.get_cell_num_for_pos(self.active_grid, north_east)[1]}")

        north_west_neighbor = self.get_cell_num_for_pos(self.active_grid, north_west)[0]
        if north_west_neighbor is not None and north_west_neighbor.is_alive():
            print(f"my index: {cell_index}, north_west neighbor index: {self.get_cell_num_for_pos(self.active_grid, north_west)[1]}")

        south_east_neighbor = self.get_cell_num_for_pos(self.active_grid, south_east)[0]
        if south_east_neighbor is not None and south_east_neighbor.is_alive():
            print(f"my index: {cell_index}, south_east neighbor index: {self.get_cell_num_for_pos(self.active_grid, south_east)[1]}")

        south_west_neighbor = self.get_cell_num_for_pos(self.active_grid, south_west)[0]
        if south_west_neighbor is not None and south_west_neighbor.is_alive():
            print(f"my index: {cell_index}, south_west neighbor index: {self.get_cell_num_for_pos(self.active_grid, south_west)[1]}")            

        neighbor_list.append(north_neighbor)
        neighbor_list.append(south_neighbor)
        neighbor_list.append(east_neighbor)
        neighbor_list.append(west_neighbor)

        neighbor_list.append(north_east_neighbor)
        neighbor_list.append(north_west_neighbor)
        neighbor_list.append(south_east_neighbor)
        neighbor_list.append(south_west_neighbor)

        for neighbor in neighbor_list:
            if neighbor is not None and neighbor.is_alive():
                cell.neighbors += 1

        if cell.neighbors is not 0:
            print(f"{cell.neighbors}")

        self.grids[self.inactive_grid()][cell_index] = copy(cell)

        if cell.is_alive():
            if cell.neighbors == 2 or cell.neighbors == 3:                                
                self.grids[self.inactive_grid()][cell_index].revive()  
            else:
                self.grids[self.inactive_grid()][cell_index].kill()
        else:
            if cell.neighbors == 3:
                self.grids[self.inactive_grid()][cell_index].revive()


    def increase_generation(self):
        self._generation += 1

        for index in range(self._number_of_cells*self._number_of_cells):
            cell = self.grids[self.active_grid][index]

            self.check_cell_neighbors(cell)

            #self.grids[self.inactive_grid()][index] = next_generation
        self.active_grid = self.inactive_grid()

    def is_interactable(self):
        return self._user_interaction_enabled

    def set_board_size(self, number_of_cells):
        self._number_of_cells = number_of_cells
        self._cell_size = number_of_cells

    def set_active_grid(self, choice=None):
        self.increase_generation()

        from game import window_height
        from game import window_width

        self._user_interaction_enabled = False

        if choice == None:
            for grid in self.grids[self.active_grid]:
                draw = random.choice([0,1])
                if draw == 1:
                    grid._draw_circle()
        elif choice == 1:
            for grid in self.grids[self.active_grid]:
                grid._draw_circle()
        else:
            for grid in self.grids[self.active_grid]:
                grid._clear_circle()
    
    def draw_grid(self, grid_num):                
        self._is_user_interaction_enabled = False

        for grid in self.grids[grid_num]:
            grid.draw()
            if grid.is_alive():
                grid._draw_circle()
            else: 
                grid._clear_circle()

        self.draw_status_bar(screen)

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