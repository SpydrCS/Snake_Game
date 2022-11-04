import pygame
import os
import random

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

APPLE_WIDTH = 20
APPLE_HEIGHT = 20
SNAKE_PART_SIZE = 10

SCORE_FONT = pygame.font.SysFont('comicsans', 20)
END_FONT = pygame.font.SysFont('comicsans', 100)

APPLE_EATEN = pygame.USEREVENT + 1

APPLE_IMAGE = pygame.image.load('apple.jpg')
APPLE = pygame.transform.scale(APPLE_IMAGE, (APPLE_WIDTH, APPLE_HEIGHT))
MENU_IMAGE = pygame.image.load('menu.png')
MENU = pygame.transform.scale(MENU_IMAGE, (WIDTH, HEIGHT))

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
MAX_APPLES = 10

def generate_apple_locations():
    apple_count = 0
    apple_list = []
    while (apple_count < MAX_APPLES):
        x = random.randint(15, WIDTH - 35)
        y = random.randint(15, HEIGHT - 35)

        if x < 100 and y < 50:
            continue

        if x + APPLE_WIDTH > 420 and x < 470 and y + APPLE_HEIGHT > 240 and y < 270:
            continue

        apple = pygame.Rect(x, y, APPLE_WIDTH, APPLE_HEIGHT)
        for others in apple_list:
            if apple.colliderect(others):
                continue
        apple_list.append(apple)
        apple_count += 1

    return apple_list


def handle_eating_apples(head : pygame.Rect, apple_list):
    for apple in apple_list:
        if head.colliderect(apple):
            pygame.event.post(pygame.event.Event(APPLE_EATEN))
            apple_list.remove(apple)


def check_snake_collision_with_itself(snake):
    head = snake[0]
    for i in range(1, len(snake)):
        if head == snake[i]:
            return True
    return False

def check_snake_collision_with_borders(snake):
    head = snake[0]
    if head.x <= 15 or head.x + SNAKE_PART_SIZE >= WIDTH - 15 or head.y <= 15 or head.y + SNAKE_PART_SIZE >= HEIGHT - 15:
        return True
    return False



def draw_window(snake, apple_list, score):
    WIN.fill(GRASS_GREEN)

    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (20, 15))

    border_left = pygame.Rect(0, 0, 15, HEIGHT)
    border_right = pygame.Rect(WIDTH - 15, 0, 15, HEIGHT)
    border_top = pygame.Rect(0, 0, WIDTH, 15)
    border_bottom = pygame.Rect(0, HEIGHT - 15, WIDTH, 15)
    
    pygame.draw.rect(WIN, GREY, border_left)
    pygame.draw.rect(WIN, GREY, border_right)
    pygame.draw.rect(WIN, GREY, border_top)
    pygame.draw.rect(WIN, GREY, border_bottom)

    for (i, part) in enumerate(snake):
        if i == 0:
            pygame.draw.rect(WIN, RED, part)
        else:
            pygame.draw.rect(WIN, ORANGE, part)

    for apple in apple_list:
        WIN.blit(APPLE, (apple.x, apple.y))

    pygame.display.update()


def draw_end_game(score):
    draw_text = END_FONT.render("Final score: " + str(score), 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    score = 0
    snake = []
    snake_part1 = pygame.Rect(450, 250, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
    snake_part2 = pygame.Rect(440, 250, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
    snake_part3 = pygame.Rect(430, 250, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
    snake.append(snake_part1)
    snake.append(snake_part2)
    snake.append(snake_part3)

    last_snake = snake

    apple_list = generate_apple_locations()

    direction = "R"  # L, R, U, D (LEFT, RIGHT, UP, DOWN)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "R":
                    direction = "L"
                    new_snake = []
                    head_part = last_snake[0]
                    new_snake.append(pygame.Rect(head_part.x - SNAKE_PART_SIZE, head_part.y, head_part.width, head_part.height))
                    for i in range(len(last_snake)-1):
                        new_snake.append(last_snake[i])
                    tail_part = last_snake[len(last_snake)-1]
                    pygame.draw.rect(WIN, GRASS_GREEN, tail_part)
                    last_snake = new_snake

                if event.key == pygame.K_RIGHT and direction != "L":
                    direction = "R"
                    new_snake = []
                    head_part = last_snake[0]
                    new_snake.append(pygame.Rect(head_part.x + SNAKE_PART_SIZE, head_part.y, head_part.width, head_part.height))
                    for i in range(len(last_snake)-1):
                        new_snake.append(last_snake[i])
                    tail_part = last_snake[len(last_snake)-1]
                    pygame.draw.rect(WIN, GRASS_GREEN, tail_part)
                    last_snake = new_snake

                if event.key == pygame.K_UP and direction != "D":
                    direction = "U"
                    new_snake = []
                    head_part = last_snake[0]
                    new_snake.append(pygame.Rect(head_part.x, head_part.y - SNAKE_PART_SIZE, head_part.width, head_part.height))
                    for i in range(len(last_snake)-1):
                        new_snake.append(last_snake[i])
                    tail_part = last_snake[len(last_snake)-1]
                    pygame.draw.rect(WIN, GRASS_GREEN, tail_part)
                    last_snake = new_snake

                if event.key == pygame.K_DOWN and direction != "U":
                    direction = "D"
                    new_snake = []
                    head_part = last_snake[0]
                    new_snake.append(pygame.Rect(head_part.x, head_part.y + SNAKE_PART_SIZE, head_part.width, head_part.height))
                    for i in range(len(last_snake)-1):
                        new_snake.append(last_snake[i])
                    tail_part = last_snake[len(last_snake)-1]
                    pygame.draw.rect(WIN, GRASS_GREEN, tail_part)
                    last_snake = new_snake

            if event.type == APPLE_EATEN:
                score += 1
                tail = last_snake[len(last_snake)-1]
                if direction == "L":
                    new_tail = pygame.Rect(tail.x + SNAKE_PART_SIZE, tail.y, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
                    last_snake.append(new_tail)
                elif direction == "R":
                    new_tail = pygame.Rect(tail.x - SNAKE_PART_SIZE, tail.y, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
                    last_snake.append(new_tail)
                elif direction == "U":
                    new_tail = pygame.Rect(tail.x, tail.y + SNAKE_PART_SIZE, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
                    last_snake.append(new_tail)
                elif direction == "D":
                    new_tail = pygame.Rect(tail.x, tail.y - SNAKE_PART_SIZE, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
                    last_snake.append(new_tail)

        if apple_list == []:
            draw_end_game(score)
            break

        if check_snake_collision_with_itself(last_snake):
            draw_end_game(score)
            break

        if check_snake_collision_with_borders(last_snake):
            draw_end_game(score)
            break

        handle_eating_apples(last_snake[0], apple_list)

        draw_window(last_snake, apple_list, score)

    main()

def menu():
    WIN.blit(MENU, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main()
                    break
        pygame.display.update()

if __name__ == "__main__":
    menu()