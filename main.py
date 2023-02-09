import math
import multiprocessing
import os
import time
from time import sleep
import pygame
import random

# initialize library
pygame.init()


class Vector:
    def __init__(self, angle, length):
        self.angle = angle
        self.length = length

    @staticmethod
    def add_vectors(v1, v2):
        x = math.sin(v1.angle) * v1.length + math.sin(v2.angle) * v2.length
        y = math.cos(v1.angle) * v1.length + math.cos(v2.angle) * v2.length
        length = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y, x)
        return Vector(angle=angle, length=length)


class Pixel:
    def __init__(self, color, x, y, width, height, angle, speed):
        self.color = color
        self.rect = pygame.Rect(
            x, y,
            width, height
        )
        self.width = width
        self.height = height
        self.angle = angle
        self.speed = speed

    def move(self):
        dx = math.sin(self.angle) * self.speed
        dy = -math.cos(self.angle) * self.speed
        self.rect = self.rect.move(dx, dy)


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

    def move_pixel(self, p: Pixel):
        # initial movement
        p.move()

        # check for collisions
        if p.rect.x >= self.screen_dimensions[0] - p.width or p.rect.x <= 0:
            p.angle = -p.angle

        if p.rect.y >= self.screen_dimensions[1] - p.height or p.rect.y <= 0:
            p.angle = math.pi - p.angle

    def run(self):
        # todo temp random particles
        for _ in range(50):
            x, y = random.randint(50, 500), random.randint(50, 500)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            speed = random.random() * self.pixel_size
            angle = random.uniform(0, 2 * math.pi)
            p = Pixel(color=color, x=x, y=y, width=self.pixel_size, height=self.pixel_size, angle=angle, speed=speed)
            self.pixels.append(p)

        while self.frame < 1000:
            # increment frame
            self.frame += 1

            # pixel actions
            for pixel in self.pixels:
                self.move_pixel(p=pixel)

            # display
            self.update_display()

            # sleep
            sleep(1 / self.fps_limit)


# start game
if __name__ == '__main__':
    game = Game()
    game.run()
