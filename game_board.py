import pygame
import random
import message
from message import Button
from automata import GridCell
from public_UI import *
from copy import copy

class Board:
   
    def __init__(self, generation, window_width, window_height, board_style=0, num_cells=50):        
        self._generation = generation
        self._is_user_interaction_enabled = False
        self._num_cells = num_cells
        self.status_bar_height = 80
        self.__size = Size(window_width, window_height-self.status_bar_height)
        self.surface = pygame.Surface((self.size().width, self.size().height))
        self.active_grid = 0
        self.__init_grids__()
        self.set_active_grid(board_style)
        self.draw_grid(self.active_grid)
        self.status_bar = pygame.Surface((self.size().width, self.status_bar_height))
        self.pause_button()
        self.clear_button()
        self.randomize_button()
        
    def __str__(self):
        return(f"board#: {self.active_grid}, width: {self.size().width}, height: {self.size().height}, with number of cells(sq): {self._num_cells}")

    def __init_grids__(self):
        
        self.grids = [
            [None for x in range(self._num_cells*self._num_cells)],
            [None for x in range(self._num_cells*self._num_cells)]
        ]        
        for x in range(self._num_cells):            
            for y in range(self._num_cells):
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                self.grids[0][(self._num_cells*x)+y] = rect

    def size(self):
        return self.__size

    def cell_size(self):
        return Size(self.__size.width//self._num_cells, self.__size.height//self._num_cells)

    def get_generation(self):
        return self._generation

    def inactive_grid(self):
        return (self.active_grid +1) %2

    def get_cell_for_pos(self, grid_num, position=Position(0,0)):

        column = position.x//self.cell_size().width
        row = position.y//self.cell_size().height
        cell_index = (self._num_cells*column)+row
        try: 
            cell = self.grids[grid_num][cell_index]
            if cell.is_alive():
                pass
        except IndexError:
            cell = None  
        
        return (cell, cell_index)

    def check_cell_neighbors(self, cell):

        cell_index = self.get_cell_for_pos(self.active_grid, Position(cell.x, cell.y))[1]
        
        neighbor_list = []
        cell.neighbors = 0

        padding = self._num_cells//100

        north = Position(cell.x, cell.y - padding - self.cell_size().height)
        south = Position(cell.x, cell.y + padding + self.cell_size().height)
        east = Position(cell.x + padding + self.cell_size().width, cell.y)
        west = Position(cell.x - padding - self.cell_size().width, cell.y)

        north_east = Position(east.x, north.y)
        north_west = Position(west.x, north.y)
        south_east = Position(east.x, south.y)
        south_west = Position(west.x, south.y)

        north_neighbor = self.get_cell_for_pos(self.active_grid, north)[0]        
        south_neighbor = self.get_cell_for_pos(self.active_grid, south)[0]
        east_neighbor = self.get_cell_for_pos(self.active_grid, east)[0]
        west_neighbor = self.get_cell_for_pos(self.active_grid, west)[0]

        north_east_neighbor = self.get_cell_for_pos(self.active_grid, north_east)[0]
        north_west_neighbor = self.get_cell_for_pos(self.active_grid, north_west)[0]
        south_east_neighbor = self.get_cell_for_pos(self.active_grid, south_east)[0]
        south_west_neighbor = self.get_cell_for_pos(self.active_grid, south_west)[0]

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
        for index in range(self._num_cells*self._num_cells):
            cell = self.grids[self.active_grid][index]

            self.check_cell_neighbors(cell)
        self.active_grid = self.inactive_grid()

    def is_interactable(self):
        return self._is_user_interaction_enabled                
        
    def set_active_grid(self, choice=None):
        
        for grid in self.grids[self.active_grid]:
                grid.draw()

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
        for grid in self.grids[grid_num]:
            grid.draw()            
            if grid.is_alive():
                grid._draw_circle()
            else: 
                grid._clear_circle()                         
        self.draw_status_bar(screen)

    def draw_status_bar(self, screen):
    
        from message import Button
        
        pygame.display.set_caption(f"Conway's Game of Life")
        status_bar = pygame.Surface((self.__size.width, self.status_bar_height))        
        status_bar.fill(dead_color)
        self.status_bar = status_bar
        self.pause_button()        
        self.clear_button()
        self.randomize_button()
        message.message_display(f"Generation: {self._generation}", status_bar, Position(status_bar.get_rect().width, status_bar.get_rect().height), white)
        screen.blit(self.status_bar, (0, self.size().height))

    def clear(self):
        for board in self.grids:
            for grid in board:
                if grid != None:                
                    grid._clear_circle()
                    grid.draw()


    def pause_button(self):
        if pause:
            self.pauseBtn = Button("Play", (self.status_bar.get_rect().width//2, 0), self.status_bar, border_color=black, fill_color=green, text_color = white)
        else:            
            self.pauseBtn = Button("Pause", (self.status_bar.get_rect().width//2, 0), self.status_bar, border_color=black, fill_color=green, text_color = white)

    def clear_button(self):
        self.clearBtn = Button("Clear Board", (self.pauseBtn.x + self.pauseBtn.width + 8, 0), self.status_bar, border_color=black, fill_color=red, text_color=white)

    def randomize_button(self):
        self.randomizeBtn = Button("Randomize", (8, 0), self.status_bar, border_color=black, fill_color=cyan, text_color=white)

    def draw_rects(self, grid_num):
        for grid in self.grids[grid_num]:
             pygame.draw.rect(grid.surface, gray, grid.surface.get_rect(), 1)

    def clear_rects(self, grid_num):
        for grid in self.grids[grid_num]:
            pygame.draw.rect(grid.surface, dead_color, grid.surface.get_rect(), 1)