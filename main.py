import datetime
import math

import pygame
from pygame import Color, Vector2

HOUR_SEC = 3600
HOUR_MICROSEC = HOUR_SEC * 1e6
MIN_SEC = 60
MIN_MICROSEC = MIN_SEC * 1e6
TWELVE_HOURS_MICROSEC = 12 * HOUR_MICROSEC


FRAMERATE = 60

SCREEN_SIZE_HEIGHT = 600

WHITE = Color("white")
BG_COLOR = Color("#202020")


def display_clock(screen: pygame.Surface):
    RADIUS = SCREEN_SIZE_HEIGHT * 0.4
    center = Vector2(screen.get_rect().center)
    def _get_unitvector_with_angle(angle: float) -> Vector2:
        return Vector2(math.sin(angle), -math.cos(angle))
    def _draw_arrow(angle: float, length: float, thickness: int):
        vec = length * _get_unitvector_with_angle(angle)
        pygame.draw.line(screen, WHITE, center, center + vec, thickness)
    def _draw_tick(angle: float, length: float, thickness: int):
        uvec = _get_unitvector_with_angle(angle)
        pygame.draw.line(
            screen, WHITE, 
            center + uvec * (RADIUS - length), 
            center + uvec * RADIUS, 
            thickness
        )
    pygame.draw.circle(screen, WHITE, center, RADIUS, 5)
    pygame.draw.circle(screen, WHITE, center, 5)

    now = datetime.datetime.now().time()
    microseconds_since_00 = 1e6 * ((now.hour % 12) * HOUR_SEC + now.minute * MIN_SEC + now.second) + now.microsecond
    angle_hour = 2 * math.pi * microseconds_since_00 / TWELVE_HOURS_MICROSEC
    angle_minute = 2 * math.pi * (microseconds_since_00 % HOUR_MICROSEC) / HOUR_MICROSEC
    angle_second = 2 * math.pi * (microseconds_since_00 % MIN_MICROSEC) / MIN_MICROSEC

    _draw_arrow(angle_hour, RADIUS * 0.5, 6)
    _draw_arrow(angle_minute, RADIUS * 0.9, 4)
    _draw_arrow(angle_second, RADIUS * 0.9, 2)

    for i in range(12):
        _draw_tick(
            angle=math.pi/6 * i,
            length=50 if i % 3 == 0 else 30,
            thickness=6 if i % 3 == 0 else 3,
        )


def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
    background = pygame.Surface((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
    background.fill(BG_COLOR)
    pygame.display.set_caption("Current local time")
    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(FRAMERATE) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        surface.blit(background, (0, 0))
        display_clock(surface)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
