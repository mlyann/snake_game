# src/snake.py
import pygame
from src.settings import SNAKE_SIZE, GREEN

class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.body = [(100, 100), (80, 100), (60, 100)]  # Starting with 3 segments
        self.direction = 'RIGHT'

    def change_direction(self, new_direction):
        # Prevent the snake from reversing direction directly
        if new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = new_direction
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = new_direction
        elif new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = new_direction
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'RIGHT':
            head_x += self.size
        elif self.direction == 'LEFT':
            head_x -= self.size
        elif self.direction == 'UP':
            head_y -= self.size
        elif self.direction == 'DOWN':
            head_y += self.size

        new_head = (head_x, head_y)
        self.body.insert(0, new_head)  # Insert new head position
        self.body.pop()               # Remove the tail segment

    def grow(self):
        # When food is eaten, add a new segment (by not removing the tail)
        self.body.append(self.body[-1])

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, pygame.Rect(segment[0], segment[1], self.size, self.size))