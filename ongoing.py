import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

SNAKE_PART_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRASS_GREEN = (69, 139, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (139, 69, 0)
GREY = (131, 139, 139)

FPS = 60
SNAKE_SPEED = 10

def snake_set_movement(last_snake, keys_pressed, direction):
    new_snake = []
    head_part = last_snake[0]

    if keys_pressed[pygame.K_LEFT] and dir != "R":
        new_snake.append(pygame.Rect(head_part.x - SNAKE_PART_SIZE, head_part.y, head_part.width, head_part.height))
        for i in range(len(last_snake)-1):
            new_snake.append(last_snake[i])
    if keys_pressed[pygame.K_RIGHT] and dir != "L":
        new_snake.append(pygame.Rect(head_part.x + SNAKE_PART_SIZE, head_part.y, head_part.width, head_part.height))
        for i in range(len(last_snake)-1):
            new_snake.append(last_snake[i])
    if keys_pressed[pygame.K_DOWN] and dir != "U":
        new_snake.append(pygame.Rect(head_part.x, head_part.y + SNAKE_PART_SIZE, head_part.width, head_part.height))
        for i in range(len(last_snake)-1):
            new_snake.append(last_snake[i])
    if keys_pressed[pygame.K_UP] and dir != "D":
        new_snake.append(pygame.Rect(head_part.x, head_part.y - SNAKE_PART_SIZE, head_part.width, head_part.height))
        for i in range(len(last_snake)-1):
            new_snake.append(last_snake[i])

    tail_part = last_snake[len(last_snake)-1]
    pygame.draw.rect(WIN, GRASS_GREEN, tail_part)
    last_snake = new_snake


def draw_window(last_snake):
    WIN.fill(GRASS_GREEN)

    border_left = pygame.Rect(0, 0, 15, HEIGHT)
    border_right = pygame.Rect(WIDTH - 15, 0, 15, HEIGHT)
    border_top = pygame.Rect(0, 0, WIDTH, 15)
    border_bottom = pygame.Rect(0, HEIGHT - 15, WIDTH, 15)
    
    pygame.draw.rect(WIN, GREY, border_left)
    pygame.draw.rect(WIN, GREY, border_right)
    pygame.draw.rect(WIN, GREY, border_top)
    pygame.draw.rect(WIN, GREY, border_bottom)

    for part in last_snake:
        pygame.draw.rect(WIN, ORANGE, part)

    pygame.display.update()


def main():
    snake = []
    snake_part1 = pygame.Rect(450, 250, 10, 10)
    snake_part2 = pygame.Rect(440, 250, 10, 10)
    snake_part3 = pygame.Rect(430, 250, 10, 10)
    snake.append(snake_part1)
    snake.append(snake_part2)
    snake.append(snake_part3)

    last_snake = snake

    direction = "R"  # L, R, U, D (LEFT, RIGHT, UP, DOWN)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys_pressed = pygame.key.get_pressed()

        snake_set_movement(last_snake, keys_pressed, direction)

        draw_window(last_snake)

    pygame.quit()


if __name__ == "__main__":
    main()