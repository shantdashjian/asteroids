import random
import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
    
    def update(self, dt):
        self.position += (self.velocity * dt)