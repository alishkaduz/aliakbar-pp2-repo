import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
block_size = 20
snake = [(100, 100)]
direction = (block_size, 0)

# Food
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, block_size)
        y = random.randrange(0, HEIGHT, block_size)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

# Score & level
score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(speed)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, block_size):
                direction = (0, -block_size)
            elif event.key == pygame.K_DOWN and direction != (0, -block_size):
                direction = (0, block_size)
            elif event.key == pygame.K_LEFT and direction != (block_size, 0):
                direction = (-block_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-block_size, 0):
                direction = (block_size, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # ❌ Wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over (Wall)")
        running = False

    # ❌ Self collision
    if new_head in snake:
        print("Game Over (Self)")
        running = False

    snake.insert(0, new_head)

    # 🍎 Food collision
    if new_head == food:
        score += 1
        food = generate_food()

        # 🎯 Level system (every 3 points)
        if score % 3 == 0:
            level += 1
            speed += 2   # increase speed
    else:
        snake.pop()

    # Drawing
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, block_size, block_size))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, block_size, block_size))

    # Draw score and level
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()