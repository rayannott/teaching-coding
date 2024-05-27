import datetime
import math
import statistics
import random
from itertools import pairwise

import pygame
from pygame import Color, Vector2

HOUR_SEC = 3600
HOUR_MICROSEC = HOUR_SEC * 1e6
MIN_SEC = 60
MIN_MICROSEC = MIN_SEC * 1e6
TWELVE_HOURS_MICROSEC = 12 * HOUR_MICROSEC


FRAMERATE = 60

SCREEN_SIZE_HEIGHT = 850

WHITE = Color("white")
BG_COLOR = Color("#151515")

pygame.init()
pygame.font.init()

FONT = pygame.font.Font("Survival-Instinx.otf", 40)


class Clock:
    def __init__(
        self,
        surface: pygame.Surface,
        center: Vector2,
        radius: float,
    ):
        self.surface = surface
        self.center = center
        self.radius = radius

    def set_center(self, center: Vector2):
        self.center = center

    def display(self, time: datetime.time):
        def _get_unitvector_with_angle(angle: float) -> Vector2:
            return Vector2(math.sin(angle), -math.cos(angle))

        def _draw_arrow(angle: float, length: float, thickness: int):
            vec = length * _get_unitvector_with_angle(angle)
            pygame.draw.line(
                self.surface, WHITE, self.center, self.center + vec, thickness
            )

        def _draw_tick(angle: float, length: float, thickness: int):
            uvec = _get_unitvector_with_angle(angle)
            pygame.draw.line(
                self.surface,
                WHITE,
                self.center + uvec * (self.radius - length),
                self.center + uvec * self.radius,
                thickness,
            )

        pygame.draw.circle(self.surface, WHITE, self.center, self.radius, 5)
        pygame.draw.circle(self.surface, WHITE, self.center, 5)

        microseconds_since_00 = (
            1e6 * ((time.hour % 12) * HOUR_SEC + time.minute * MIN_SEC + time.second)
            + time.microsecond
        )
        angle_hour = 2 * math.pi * microseconds_since_00 / TWELVE_HOURS_MICROSEC
        angle_minute = (
            2 * math.pi * (microseconds_since_00 % HOUR_MICROSEC) / HOUR_MICROSEC
        )
        angle_second = (
            2 * math.pi * (microseconds_since_00 % MIN_MICROSEC) / MIN_MICROSEC
        )

        _draw_arrow(angle_hour, self.radius * 0.5, 7)
        _draw_arrow(angle_minute, self.radius * 0.9, 3)
        _draw_arrow(angle_second, self.radius * 0.9, 1)

        for i in range(12):
            _draw_tick(
                angle=math.pi / 6 * i,
                length=self.radius * 0.2 if i % 3 == 0 else self.radius * 0.1,
                thickness=6 if i % 3 == 0 else 3,
            )


class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
        self.background = pygame.Surface((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
        self.background.fill(BG_COLOR)
        pygame.display.set_caption("Clock Game")
        self.clock = pygame.time.Clock()

        self.running = True

        self.started = False

        self.round_counter = 0
        self.score = 0
        self.performance_times: list[float] = []

        self.n_clocks = 3
        self.round_length = 5
        self.clock_radius = 150
        self.screen_center = Vector2(self.surface.get_rect().center)
        unit_vector = Vector2(0, -1)
        self.clock_centers = [
            self.screen_center + unit_vector.rotate(360 / self.n_clocks * i) * 250
            for i in range(self.n_clocks)
        ]

        self.clocks: list[Clock] = []
        self.times: list[datetime.time] = []
        self.picked_time_idx: int | None = None

    def _generate_clocks(self) -> list[Clock]:
        return [
            Clock(self.surface, center, self.clock_radius)
            for center in self.clock_centers
        ]

    def _generate_times(self) -> list[datetime.time]:
        return [
            datetime.time(
                random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)
            )
            for _ in range(3)
        ]

    def _pick_time(self):
        return random.randrange(0, self.n_clocks)
    
    def _generate_round(self):
        self.clocks = self._generate_clocks()
        self.times = self._generate_times()
        self.picked_time_idx = self._pick_time()

    def clock_clicked(self, pos: Vector2) -> int | None:
        for i, clock in enumerate(self.clocks):
            if (pos - clock.center).length() < self.clock_radius:
                return i
        return None
    
    def process_clock_clicked(self, clicked_clock: int | None):
        if clicked_clock is None:
            return
        self.performance_times.append(datetime.datetime.now().timestamp())
        if clicked_clock == self.picked_time_idx:
            self.score += 1
        self.round_counter += 1
        print(f"Score: {self.score}/{self.round_counter}")
        if self.round_counter >= self.round_length:
            self.started = False
            self.clocks = []
            self.picked_time_idx = None
            return
        self._generate_round()
    
    def display_pre_post_game_text(self):
        if self.started:
            return
        lines = [
            "Press SPACE to start",
        ]
        
        if self.round_counter > 0:
            lines.append(f"Score: {self.score}/{self.round_counter}")
            pairwise_diffs = [
                t2 - t1 for t1, t2 in pairwise(self.performance_times)
            ]
            lines.append(
                f"Performance: {statistics.mean(pairwise_diffs):.2f} ± {statistics.stdev(pairwise_diffs):.2f}"
            )
        for i, line in enumerate(lines):
            text = FONT.render(line, True, WHITE)
            text_rect = text.get_rect(center=(self.screen_center.x, self.screen_center.y + i * 60))
            self.surface.blit(text, text_rect)

    def display_clocks(self):
        for clock, time in zip(self.clocks, self.times):
            clock.display(time)

    def display_time(self):
        if self.picked_time_idx is None:
            return
        time = self.times[self.picked_time_idx]
        text = FONT.render(
            f"{time.hour:02d}:{time.minute:02d}", True, WHITE
        )
        text_rect = text.get_rect(center=self.screen_center)
        self.surface.blit(text, text_rect)

    def run(self):
        while self.running:
            _ = self.clock.tick(FRAMERATE) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        self.started = True
                        self.score = 0
                        self.round_counter = 0
                        self.performance_times = [datetime.datetime.now().timestamp()]
                        self._generate_round()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.started:
                        continue
                    pos = Vector2(pygame.mouse.get_pos())
                    clicked_clock = self.clock_clicked(pos)
                    self.process_clock_clicked(clicked_clock)

            self.surface.blit(self.background, (0, 0))
            self.display_pre_post_game_text()
            self.display_clocks()
            self.display_time()
            pygame.display.update()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
