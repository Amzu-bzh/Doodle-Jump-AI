## Setup
# Modules
import pygame
pygame.init()
clock = pygame.time.Clock()

# Define the class for our square objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
         
        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((50, 50))
         
        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()

# Functions for coordinate
def coor(tup: list):
    tup[0] += 656
    return tuple(tup)

# Constantes
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Doodle Jump")

RUNNING = True

SPEED = 10
GRAVITY = 16

## Game
# Player
doodle = Player()

d_x = 279
d_y = 0

# Game loop
while RUNNING:
    
    tel_screen = pygame.draw.rect(screen, (133, 127, 126), pygame.Rect(656, 0, 608, 1080))
    pygame.draw.rect(screen, (0, 255, 0), coor([d_x, d_y, 50, 50]))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                d_y -= 600
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        d_x -= SPEED
        
    if keys[pygame.K_RIGHT]:
        d_x += SPEED

    
    if d_x <= 0:
        d_x = 558
    elif d_x >= 559:
        d_x = 1
    
    d_y += GRAVITY
    
    if d_y >= 1020:
        RUNNING = False
    
    clock.tick(60)
    pygame.display.update()
    
pygame.quit()