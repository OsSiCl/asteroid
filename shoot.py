import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt