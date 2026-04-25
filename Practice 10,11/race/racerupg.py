import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")
road_img = pygame.image.load("road.png")

player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Player
player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 5

# Enemy
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

# Coin
coin_x = random.randint(0, WIDTH - 30)
coin_y = -50

# Different coin weights (values)
coin_values = [1, 2, 5]
coin_value = random.choice(coin_values)

# Score
coins_collected = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
running = True

# Increase speed every N coins
N = 5

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player in bounds
    player_x = max(0, min(WIDTH - 50, player_x))

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - 50)

    # Move coin
    coin_y += 4
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 30)
        coin_value = random.choice(coin_values)

    # Rectangles for collision
    player_rect = pygame.Rect(player_x, player_y, 50, 100)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)
    coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)

    # ❌ Collision with enemy
    if player_rect.colliderect(enemy_rect):
        print("Game Over")
        running = False

    # 💰 Collect coin
    if player_rect.colliderect(coin_rect):
        coins_collected += coin_value

        # Respawn coin
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 30)
        coin_value = random.choice(coin_values)

        # 🚀 Increase difficulty
        if coins_collected % N == 0:
            enemy_speed += 1

    # Draw
    screen.fill((30, 30, 30))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    screen.blit(coin_img, (coin_x, coin_y))

    # Show coin value above coin
    value_text = font.render(str(coin_value), True, (255, 255, 0))
    screen.blit(value_text, (coin_x, coin_y - 20))

    # Score display
    score_text = font.render(f"Coins: {coins_collected}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()