import pygame
from public_UI import white, black, screen
from message import *

blue = (0,0,200)
red = (200,50,50)

class GridCell:
    def __init__(self, x, y, width, height):
        super().__init__()
        #pos
        self.x = x
        self.y = y
        #size
        self.width = width
        self.height = height
        #state
        self._alive = False
        self._color = blue
        self.neighbors = 0
        self.drawn = False
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def __str__(self):
        return (f"x: {self.x}, y: {self.y}, width: {self.width}, color: {self.color}, alive: {self.alive}")

    def _draw_circle(self):
        self._alive = True
        pygame.draw.ellipse(self.surface, self._color, self.surface.get_rect())

    def _clear_circle(self):
        self._alive = False
        pygame.draw.ellipse(self.surface, white, self.surface.get_rect())


    def draw(self):
        rect = pygame.Rect(0,0, self.width, self.height)

        screen.blit(self.surface, (self.x, self.y))
        #pygame.draw.rect(self.surface, black, rect, 1)

    def is_alive(self):
        return self._alive

    def get_color(self):
        return self._color

    def kill(self):
        if self._alive:
            self._color = red
            self._alive = False
            self._draw_circle()

    def revive(self):
        self._color = blue
        self._alive = True        

    def change_color(self, color):
        self._color = color

class Automata:
    #set initial state to alive
    def __init__(self, num, name):
        self.cells: GridCell = [None for num in range(num)]
        self.name = name

class Blinker(Automata):
    def __init__(self, cell_array):
        super().__init__(len(cell_array), "Blinker")
        self.cells = cell_array

    def draw_blink(self):        
        for cell in self.cells:
            cell._draw_circle()