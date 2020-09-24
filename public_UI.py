import pygame
class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

# Mark: Colors
black = (0, 0, 0)
white = (245, 245, 245)
red = (255, 0, 0)
cyan = (0,186,186)

# MARK: Screen Parameters
window_height = 1000
window_width = 1650
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
fps = 1 