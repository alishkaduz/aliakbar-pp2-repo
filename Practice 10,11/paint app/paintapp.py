import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

drawing = False
tool = "brush"  # brush, rect, circle, eraser
color = BLACK
start_pos = None

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)

            elif tool == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "brush"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "eraser"

            # Color selection
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

    # Drawing with mouse
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        if tool == "brush":
            pygame.draw.circle(screen, color, mouse_pos, 5)

        elif tool == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, 10)

    pygame.display.update()

pygame.quit()