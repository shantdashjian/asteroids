import pygame

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt