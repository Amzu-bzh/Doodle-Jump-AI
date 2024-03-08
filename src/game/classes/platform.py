## Setup
# Modules
import pygame

from random import randint

## Class
class Platform:
    def __init__(self, y) -> None:
        self.x = 656 + 20 + randint(0, 448)
        self. y = y
        
        self.color = (20, 20, 255)
        
        self.rect = pygame.Rect(self.x, self.y, 120, 30)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)