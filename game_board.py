import pygame

class Board:
    def __init__(self, generation, window_width, number_of_cells=25):
        self._generation = generation
        self._user_interaction_enabled = True
        self._number_of_cells = number_of_cells
        self._cell_size = window_width//number_of_cells
        self._size = window_width

    def size(self):
        return self._size

    def cell_size(self):
        return self._cell_size

    def get_generation(self):
        return self._generation

    def increase_generation(self):
        self._generation += 1

    def is_interactable(self):
        return self._user_interaction_enabled

    def set_board_size(self, number_of_cells):
        self._number_of_cells = number_of_cells
        self._cell_size = number_of_cells

    def draw_grid(self):
        
        from game import window_height
        from game import window_width
        from game import screen
        from game import black

        self._user_interaction_enabled = False

        for x in range(window_width//self._number_of_cells):            
            for y in range(window_height//self._number_of_cells):                
                    rect = pygame.Rect(x*self._cell_size, y*self._cell_size,
                                    self._cell_size, self._cell_size)
                    pygame.draw.rect(screen, black, rect, 1)

    def draw_status_bar(self):
        pass