import pygame


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Board:
    def __init__(self, generation, window_width, window_height, number_of_cells=25):
        self._generation = generation
        self._user_interaction_enabled = True
        self._number_of_cells = number_of_cells
        self._cell_size = window_width//number_of_cells
        self._size = window_width
        self._window_size = Size(window_width, window_height)

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

    def set_board_size(self, number_of_cells):
        self._number_of_cells = number_of_cells
        self._cell_size = number_of_cells

    def draw_grid(self):
        
        from game import window_height
        from game import window_width
        from game import screen
        from game import black

        self._user_interaction_enabled = False

        for x in range(self._number_of_cells):
            for y in range(self._number_of_cells):
                rect = pygame.Rect(x*self.cell_size().width, y*self.cell_size().height,
                self.cell_size().width, self.cell_size().height)

                print(y*self.cell_size().height)

                pygame.draw.rect(screen, black, rect, 1)

    def draw_status_bar(self):
        pass