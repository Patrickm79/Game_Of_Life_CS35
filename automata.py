import pygame
from public_UI import *
from message import *

class GridCell:
    def __init__(self, x,  y, width, height):        
        super().__init__()
        # Position
        self.x = x
        self.y = y
        # Size
        self.width = width
        self.height = height
        # State
        self._alive = False
        self._age = 1
        self.max_age = 101
        self._color = self.age_color()
        self.neighbors = 0
        #create a clear surface to draw on
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        
    
    def get_age(self):
        return self._age

    def __str__(self):
        return (f"x: {self.x}, y: {self.y}, width: {self.width}, color: {self._color}, alive: {self._alive}")
        
    def _draw_circle(self):
        self._alive = True
        pygame.draw.ellipse(self.surface, self._color, self.surface.get_rect())
        
    def _clear_circle(self):
        self._alive = False        
        pygame.draw.ellipse(self.surface, dead_color, self.surface.get_rect())
        
    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def is_alive(self):
        return self._alive
    
    def get_color(self):
        return self.age_color()
    
    def kill(self):
        if self._alive:
            self._alive = False

    def age_color(self):
        #0-youth
        if self.get_age() >= self.max_age:
            self._age = 1
        current = self.get_age()/self.max_age
        youth = 0.25*self.max_age
        if self.get_age() <= youth:            
            return (0,255*current+100,0)

        #youth-midlife
        elif self.get_age() <= int(0.5*self.max_age):
            return (255*current,0,0)

        #midlife-old_age
        elif self.get_age() <= int(0.75*self.max_age):
            return (0,0,255*current)

        #old_age
        else:

            #max age, step up to 1
            blue = self._color[2]
            sure = blue + current*255
            max = 255
            if sure > max:
                sure = max
            return (0,current*255,sure)
    
    def revive(self):
        self._color = self.age_color()
        self._alive = True
        self._age += 1
    
    def change_color(self, color):
        self._color = color

class Automata:
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