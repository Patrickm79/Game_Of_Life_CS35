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


class GridCell(Automata):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def _draw_circle(self):
        center_y = self.height//2
        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2

        return pygame.draw.circle(self.surface, self._color, (self.width//2, center_y), radius)


    def draw(self):
        from game import screen, black
        rect = pygame.Rect(0,0, self.width, self.height)

        screen.blit(self.surface, (self.x, self.y))
        return pygame.draw.rect(self.surface, black, rect, 1)

class Line_Draw(Automata):
    def __init__(self):
        super().__init__()
        self.cells = []

    def draw(self, surface, x, width, height, starting_row, count):        
        for row_num in range(starting_row, count):
            self.cells.append(self._draw_circle(surface, x, width, height, row_num) )