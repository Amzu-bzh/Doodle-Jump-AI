## Setup
# Modules
import pygame

## Class
class Player:
    def __init__(self) -> None:
        self.x = 279 + 656
        self.y = 0
        
        self.color = (0, 200, 0)
        
        self.speed = 10
        self.gravity = 10
        self.jump_height = 600
        self.velocity = 20
        
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
    
    def move(self):
        self.y += self.gravity
        
        if self.x <= 656:
            self.x = 656 + 607 - 50
        elif self.x >= 656 + 608 - 50:
            self.x = 656 + 1
        
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
    
        self.x = self.rect.x
        self.y = self.rect.y
        
    
    def jump(self):
        self.y -= self.jump_height
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)