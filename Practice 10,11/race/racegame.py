import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racer")

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
road_img = pygame.image.load("road.png")

# Resize images (optional but useful)
player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Player position
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

# Enemy position
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside screen
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - 50:
        player_x = WIDTH - 50

    # Move enemy
    enemy_y += enemy_speed

    # Reset enemy when it goes off screen
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - 50)
        score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, 50, 100)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)

    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        running = False

    # Draw everything
    screen.blit(road_img, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()