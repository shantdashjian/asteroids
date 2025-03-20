import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_left = self.velocity.rotate(random_angle)
        vector_right = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_left.velocity = vector_left * 1.3
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right.velocity = vector_right