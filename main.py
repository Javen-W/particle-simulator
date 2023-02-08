import math
import multiprocessing
import os
import time
from time import sleep
import pygame
import random

# initialize library
pygame.init()


class Pixel:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.rect = pygame.Rect(
            x, y,
            width, height
        )

    """
    Moves the pixel by a given velocity vector (i.e., angle and speed).
        Angle: the vector direction represented in radians
        Speed: the vector magnitude represented in speed
    """
    def move(self, angle, speed):
        dx = math.sin(angle) * speed
        dy = -math.cos(angle) * speed
        self.rect = self.rect.move(x=dx, y=dy)


class Game:
    def __init__(self):
        # game constants
        self.screen_dimensions = 600, 600
        self.pixel_size = 30

        # game vars
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        self.frame = 0
        self.pixels = []

    def draw(self, p: Pixel):
        pygame.draw.rect(self.screen, p.color, p.rect)

    def run(self):
        while True:
            # increment frame
            self.frame += 1

            # pixel actions

            # display
            self.screen.fill((0, 0, 0))
            for pixel in self.pixels:
                self.draw(p=pixel)
            pygame.display.flip()


# start game
if __name__ == '__main__':
    game = Game()
    game.run()
