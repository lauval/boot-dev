from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")

            # determine new angle of travel (uniform split)
            new_angle = random.uniform(20,50)

            # create new velocity vectors for both asteroids
            first_asteroid_vector = self.velocity.rotate(new_angle)
            second_asteroid_vector = self.velocity.rotate(-1*new_angle)

            # define the new asteroids' radii
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # create new asteroids
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)

            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

            # set each asteroid's velocity and scale by 20%
            asteroid_1.velocity = first_asteroid_vector * 1.2
            asteroid_2.velocity = second_asteroid_vector * 1.2





