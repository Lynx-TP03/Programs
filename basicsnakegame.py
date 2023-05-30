import pygame
import time
import random

# Window dimensions
window_width = 800
window_height = 600

# Snake block size
block_size = 20

# Colors (RGB)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake's movement speed
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def score(score):
    text = score_font.render("Score: " + str(score), True, white)
    window.blit(text, [0, 0])


def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], block_size, block_size])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Snake's body
    snake_list = []
    snake_length = 1

    # Randomly position the food on the screen
    food_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            window.blit(message, [window_width / 6, window_height / 3])
            score(snake_length - 1)
            pygame.display.update()

            # Handling game over events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling movement events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundaries and collision with self
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # Draw the food
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

        # Update the snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with self
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        snake(block_size, snake_list)

        # Check if the snake has eaten the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            snake_length += 1

        score(snake_length - 1)
        pygame.display.update()

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()