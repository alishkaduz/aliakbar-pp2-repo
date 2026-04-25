import pygame
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = MickeyClock(WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 15))

    mickey.update()
    mickey.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()