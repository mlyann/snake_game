# src/game.py
import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from src.snake import Snake
from src.food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')

    def check_collisions(self):
        # Check if the snake eats the food
        head = self.snake.body[0]
        if head == self.food.position:
            self.snake.grow()
            self.food.respawn()
            self.score += 1

        # Check if the snake hits the window boundaries
        head_x, head_y = head
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            self.game_over()

        # Check if the snake collides with itself
        if head in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        print("Game Over! Your score:", self.score)
        pygame.quit()
        sys.exit()

    def update(self):
        self.snake.move()
        self.check_collisions()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.update()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)