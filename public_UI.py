import pygame
class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return(f"width: {self.width}, height: {self.height}")

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __str__(self):
        return(f"x: {self.x}, y:{self.y}")

# Mark: Colors
black = (0, 0, 0)
white = (245, 245, 245)
red = (255, 0, 0)
cyan = (0,186,186)

# MARK: Screen Parameters
window_height = 800
window_width = 800
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
fps = 1 