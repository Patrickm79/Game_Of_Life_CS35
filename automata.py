import pygame
from public_UI import white

blue = (0,0,200)
red = (200,50,50)

class Automata:
    #init = alive
    def __init__(self):
        self._alive = True
        # TODO: Find a more specific color
        self._color = blue
        self.neighbors = 0
    
    def kill(self):
        self._color = red
        self._alive = False

    def revive(self):
        self._color = blue
        self._alive = True

    def is_alive(self):
        # returns true if alive, false if dead
        return self._alive

    def get_color(self):
        return self._color

    def change_color(self, color):
        # add (RGB functionality to this)
        self._color = color


class GridCell(Automata):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.drawn = False
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def _draw_circle(self):
        self.drawn = True
        center_y = self.height//2
        center_x = self.width//2
        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2

        return pygame.draw.circle(self.surface, self._color, (center_x, center_y), radius)

    def _clear_circle(self):
        self.drawn = False
        center_y = self.height//2
        center_x = self.width//2
        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2
        pygame.draw.circle(self.surface, white, (center_x, center_y), radius)


    def draw(self):
        from game import screen, black
        rect = pygame.Rect(0,0, self.width, self.height)

        screen.blit(self.surface, (self.x, self.y))
        return pygame.draw.rect(self.surface, black, rect, 1)

class Line_Draw(Automata):
    def __init__(self):
        super().__init__()

    def draw_blink(self, surface, x, width, height, starting_row, count):        
        for row_num in range(starting_row, count):
            self._draw_circle(surface, x, width, height, row_num)