import pathlib
from itertools import cycle

import pygame

from network import Network
from gui import NetworkGui, FRAMERATE, SCREEN_SIZE, BG_COLOR


SAVES_DIR = pathlib.Path('saves')
SAVES_DIR.mkdir(exist_ok=True)


class NetworkApp:
    def reload_saves(self):
        return list(SAVES_DIR.glob('*.json'))
    
    def __init__(self):
        self.network_paths = self.reload_saves()
        self.gui = NetworkGui()

        self.surface = pygame.display.set_mode(SCREEN_SIZE)

        self.running = True
    
    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.gui.run()
    
    def draw_ui(self):
        ...

    def run(self):
        pygame.init()
        background = pygame.Surface(SCREEN_SIZE)
        background.fill(BG_COLOR)
        pygame.display.set_caption("Network App")
        clock = pygame.time.Clock()
        while self.running:
            time_delta = clock.tick(FRAMERATE) / 1000.0
            for event in pygame.event.get():
                self.process_event(event)
            self.surface.blit(background, (0, 0))
            self.draw_ui()
            pygame.display.update()
        pygame.quit()
