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

    def _draw_circle(self, surface, x, width, height, row):

        center_y = height//2
        if width > height:
            radius = height//2
        else:
            radius = width//2
        return pygame.draw.circle(surface, self._color, (x, int(row*height + center_y)), radius)

class Line_Draw(Automata):
    def __init__(self, ):
        super().__init__()
        self.cells = []

    def draw(self, surface, x, width, height, starting_row, count):        
        #surface, color, (x,y), radius, width
        for row_num in range(starting_row, count):
            self.cells.append( self._draw_circle(surface, x, width, height, row_num) )