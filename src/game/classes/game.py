## Setup
# Modules
import pygame

from classes.player import Player
from classes.platform import Platform
from classes.phone_screen import Phone_screen

## Class
class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.phone = Phone_screen()
        
        self.doodle = Player()
        self.p1 = Platform(1020)
        self.p2 = Platform(700)
    
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.doodle.x -= self.doodle.speed
        elif keys[pygame.K_RIGHT]:
            self.doodle.x += self.doodle.speed
        
        if self.doodle.y >= 1000:
            self.running = False
        
    def update(self):        
        if (self.p1.rect.colliderect(self.doodle.rect)) or (self.p2.rect.colliderect(self.doodle.rect)):
            self.doodle.jump()
        
        self.doodle.move()

    
    def display(self):
        self.screen.fill((255, 255, 255))
        self.phone.draw(self.screen)
        self.p1.draw(self.screen)
        self.p2.draw(self.screen)
        self.doodle.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)