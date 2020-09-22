import pygame

blue = (0,0,200)
red = (200,50,50)

class Automata:
    #init = alive
    def __init__(self):
        self._alive = True
        # TODO: Find a more specific color
        self._color = blue
    
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

class Line_Draw(Automata):
    def __init__(self, ):
        super().__init__()
        
    def draw(self, screen, x, cell_size):
        pygame.draw.circle(screen, self._color, (x, cell_size//2), 15, 2)
        pygame.draw.circle(screen, self._color, (x, int(cell_size*1.5)), 15, 2)
        pygame.draw.circle(screen, self._color, (x, int(cell_size*2.5)), 15, 2)