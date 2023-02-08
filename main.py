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
        old_rect = self.rect
        self.rect = self.rect.move(dx, dy)
        print("moved pixel; old: {}, new: {}".format( (old_rect.x, old_rect.y ), (self.rect.x, self.rect.y)))
        print("dx: {}, dy: {}\n".format(dx, dy))

class Game:
    def __init__(self):
        # game constants
        self.screen_dimensions = 600, 600
        self.pixel_size = 30
        self.fps_limit = 15

        # game vars
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        self.frame = 0
        self.pixels = []

    def draw(self, p: Pixel):
        pygame.draw.rect(self.screen, p.color, p.rect)

    def update_display(self):
        # erase old screen
        self.screen.fill((0, 0, 0))

        # draw pixels
        for pixel in self.pixels:
            self.draw(p=pixel)

        # draw display text
        font = pygame.font.Font(None, 30)
        text_display = font.render("Frame: {}".format(self.frame), True, (255, 255, 255))
        self.screen.blit(text_display, (0, 0))

        # update display
        pygame.display.flip()

    def run(self):
        # todo temp random particles
        for _ in range(30):
            x, y = random.randint(0, self.screen_dimensions[0]), random.randint(0, self.screen_dimensions[0])
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            p = Pixel(color=color, x=x, y=y, width=self.pixel_size, height=self.pixel_size)
            self.pixels.append(p)

        while self.frame < 1000:
            # increment frame
            self.frame += 1

            # pixel actions
            # TODO temp random movement
            for pixel in self.pixels:
                speed = random.random() * self.pixel_size
                angle = random.uniform(0, 2 * math.pi)
                pixel.move(angle=angle, speed=speed)

            # display
            self.update_display()

            # sleep
            sleep(1 / self.fps_limit)


# start game
if __name__ == '__main__':
    game = Game()
    game.run()
