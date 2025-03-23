# src/food.py
import pygame
import random
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, RED

class Food:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.position = self.random_position()

    def random_position(self):
        # Generate a random position for the food aligned to the grid
        x = random.randrange(0, SCREEN_WIDTH, self.size)
        y = random.randrange(0, SCREEN_HEIGHT, self.size)
        return (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], self.size, self.size))

    def respawn(self):
        # Reposition the food after it's eaten
        self.position = self.random_position()