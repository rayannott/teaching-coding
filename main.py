import random

import pygame
from pygame import Vector2, Color


WHITE = Color('white')
YELLOW = Color('yellow')
GREEN = Color('green')
RED = Color('red')
BLUE = Color('blue')
RGB = [RED, GREEN, BLUE]


pygame.init()

pygame.display.set_caption('Quick Start')

class App:
    def __init__(self) -> None:

        self.surface = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)

        self.background = pygame.Surface(self.surface.get_size())
        W, H = self.surface.get_size()
        self.background.fill(pygame.Color('#101010'))

        self.is_running = True

        self.nodes: list[Vector2] = []

        self.fraction = 0.5
        self.simulation_running = False
        self._current_node = Vector2(random.uniform(0, W), random.uniform(0, H))
    
    def process_event(self, event: pygame.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False
            elif event.key == pygame.K_SPACE:
                self.simulation_running = not self.simulation_running
        if event.type == pygame.MOUSEBUTTONUP:
            self.nodes.append(Vector2(pygame.mouse.get_pos()))
    
    def draw(self):
        for node in self.nodes:
            pygame.draw.circle(self.surface, WHITE, node, 4,)
    
    def simulate(self):
        next_node = random.choice(self.nodes)
        new_point = (next_node - self._current_node) * self.fraction + self._current_node
        self._current_node = new_point.copy()
        self.background.set_at(new_point, YELLOW)

    def update(self):
        if self.simulation_running:
            self.simulate()

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.process_event(event)
            self.surface.blit(self.background, (0, 0))
            self.update()
            self.draw()
            pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.run()
