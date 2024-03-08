## Setup
# Modules
import pygame

## Class
class Phone_screen():
    def __init__(self) -> None:
        self.w = 608
        self.h = 1080
        
        self.color = (117, 112, 112)
        
        self.rect = pygame.Rect(656, 0, self.w, self.h)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)