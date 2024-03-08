## Setup
# Modules
import pygame

from classes.game import Game

# Initialization
pygame.init()
screen = pygame.display.set_mode((0, 0))
game = Game(screen)

# Run game
game.run()

# Close
pygame.quit()