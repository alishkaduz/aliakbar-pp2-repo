import pygame
import datetime

class MickeyClock:
    def __init__(self, width, height):
        self.center = pygame.Vector2(width // 2, height // 2)

        original = pygame.image.load("mickey_hand.png").convert_alpha()

        self.sec_hand = pygame.transform.rotozoom(original, 0, 0.7)
        self.min_hand = pygame.transform.rotozoom(original, 0, 0.5)
        self.hour_hand = pygame.transform.rotozoom(original, 0, 0.4)

        self.sec_hand_left = pygame.transform.flip(self.sec_hand, True, False)
        self.hour_hand_left = pygame.transform.flip(self.hour_hand, True, False)

        self.sec_offset = pygame.Vector2(0, -70)
        self.min_offset = pygame.Vector2(0, -100)
        self.hour_offset = pygame.Vector2(0, -50)

    def get_angles(self):
        now = datetime.datetime.now()

        seconds = now.second + now.microsecond / 1_000_000
        minutes = now.minute + seconds / 60
        hours = (now.hour % 12) + minutes / 60

        sec_angle = seconds * 6
        min_angle = minutes * 6
        hour_angle = hours * 30

        return sec_angle, min_angle, hour_angle

    def draw_hand(self, surface, image, angle, offset):
        rotated_offset = offset.rotate(angle)
        rotated_image = pygame.transform.rotate(image, -angle)

        rect = rotated_image.get_rect(center=self.center + rotated_offset)
        surface.blit(rotated_image, rect)

    def draw_dial(self, surface):
        pygame.draw.circle(surface, (220, 220, 220), self.center, 200, 3)

        for i in range(60):
            angle = i * 6
            direction = pygame.Vector2(0, -1).rotate(angle)

            start = self.center + direction * 180

            if i % 5 == 0:
                end = self.center + direction * 150
                thickness = 4
            else:
                end = self.center + direction * 165
                thickness = 2

            pygame.draw.line(surface, (200, 200, 200), start, end, thickness)

    def update(self):
        self.sec_angle, self.min_angle, self.hour_angle = self.get_angles()

    def draw(self, surface):
        self.draw_dial(surface)

        pygame.draw.circle(surface, (255, 255, 255), self.center, 6)

        self.draw_hand(surface, self.hour_hand_left, self.hour_angle, self.hour_offset)
        self.draw_hand(surface, self.min_hand, self.min_angle, self.min_offset)
        self.draw_hand(surface, self.sec_hand_left, self.sec_angle, self.sec_offset)