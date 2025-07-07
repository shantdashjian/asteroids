import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.fill_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.fill_color, self.position, self.radius, 0)
        pygame.draw.circle(screen, self.border_color, self.position, self.radius, 4)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position. y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position. y, new_radius)
        asteroid2.velocity = vector2