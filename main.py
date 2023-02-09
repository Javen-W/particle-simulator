import math
from time import sleep
import pygame
import random

# initialize library
pygame.init()


class Vector:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction

    @staticmethod
    def add_vectors(v1, v2):
        x = math.sin(v1.direction) * v1.magnitude + math.sin(v2.direction) * v2.magnitude
        y = math.cos(v1.direction) * v1.magnitude + math.cos(v2.direction) * v2.magnitude
        magnitude = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y, x)
        return Vector(magnitude=magnitude, direction=angle)


class Pixel:
    def __init__(self, color, x: int, y: int, size: int, velocity: Vector):
        self.color = color
        self.rect = pygame.Rect(
            x, y,
            size, size
        )
        self.size = size
        self.velocity = velocity

    def move(self, v: Vector = None):
        if v:
            self.velocity = Vector.add_vectors(self.velocity, v)
        dx = math.sin(self.velocity.direction) * self.velocity.magnitude
        dy = -math.cos(self.velocity.direction) * self.velocity.magnitude
        self.rect = self.rect.move(dx, dy)


class Game:
    def __init__(self):
        # game constants
        self.screen_dimensions = 600, 600
        self.pixel_size = 30
        self.fps_limit = 30
        self.gravity = Vector(magnitude=1.1, direction=math.pi)
        self.drag = 0.999  # the loss in speed as a particle goes through the air
        self.elasticity = 0.75  # the loss in speed as a particle collides

        # game vars
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        self.frame = 0
        self.pixels = []

        # todo temp random particles
        for _ in range(30):
            x, y = random.randint(50, 500), random.randint(50, 500)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            velocity = Vector(magnitude=random.random() * self.pixel_size, direction=random.uniform(0, 2 * math.pi))
            p = Pixel(color=color, x=x, y=y, size=self.pixel_size, velocity=velocity)
            self.pixels.append(p)

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

    def move_pixel(self, p: Pixel, p_index: int):
        # apply gravity
        p.move(v=self.gravity)

        # apply air drag
        p.velocity.magnitude *= self.drag

        # check for wall collisions
        if p.rect.x > self.screen_dimensions[0] - p.size:
            # right wall
            p.rect.x = 2 * (self.screen_dimensions[0] - p.size) - p.rect.x
            p.velocity.direction = -p.velocity.direction
            p.velocity.magnitude *= self.elasticity
        elif p.rect.x < 0:
            # left wall
            p.rect.x = 0
            p.velocity.direction = -p.velocity.direction
            p.velocity.magnitude *= self.elasticity

        if p.rect.y > self.screen_dimensions[1] - p.size:
            # floor
            p.rect.y = self.screen_dimensions[1] - p.size
            p.velocity.direction = math.pi - p.velocity.direction
            p.velocity.magnitude *= self.elasticity
        elif p.rect.y < 0:
            # ceiling
            p.rect.y = p.size
            p.velocity.direction = math.pi - p.velocity.direction
            p.velocity.magnitude *= self.elasticity

        # check for other particle collisions
        for other_p in self.pixels[p_index+1:]:
            dx = p.rect.x - other_p.rect.x
            dy = p.rect.y - other_p.rect.y
            distance = math.hypot(dx, dy)

            if distance <= p.size:
                print("frame ({}): collision with distance {}".format(self.frame, distance))

                # reflect the particle angles
                tangent = math.atan2(dy, dx)
                p.velocity.direction = 2 * tangent - p.velocity.direction
                other_p.velocity.direction = 2 * tangent - other_p.velocity.direction

                # force the particle out of overlap
                angle = 0.5 * math.pi + tangent
                # dx = math.sin(angle) * (p.size - distance)
                # dy = math.cos(angle) * (p.size - distance)
                dx = math.sin(angle)
                dy = math.cos(angle)
                p.rect.x += dx
                p.rect.y -= dy
                print("tangent={}, angle={}, dx={}, -dy={}".format(tangent, angle, math.sin(angle), math.cos(angle)))
                other_p.rect.x -= dx
                other_p.rect.y += dy

                # the particles exchange energy
                (p.velocity.magnitude, other_p.velocity.magnitude) = (other_p.velocity.magnitude, p.velocity.magnitude)
                p.velocity.magnitude *= self.elasticity
                other_p.velocity.magnitude *= self.elasticity

    def find_pixel(self, x: int, y: int):
        for p in self.pixels:
            if math.hypot(p.rect.x - x, p.rect.y - y) <= p.size:
                return p
        return None

    def run(self):
        selected_pixel = None
        while self.frame < 1000:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    selected_pixel = self.find_pixel(x=mouseX, y=mouseY)
                elif event.type == pygame.MOUSEBUTTONUP:
                    selected_pixel = None

            # increment frame
            self.frame += 1

            # pixel actions
            if selected_pixel:
                selected_pixel.color = (255, 0, 0)
            for i, pixel in enumerate(self.pixels):
                if pixel != selected_pixel:
                    self.move_pixel(p=pixel, p_index=i)

            # display
            self.update_display()

            # sleep
            sleep(1 / self.fps_limit)


# start game
if __name__ == '__main__':
    game = Game()
    game.run()
