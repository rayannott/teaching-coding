import pygame

from src.simulation import Simulation
from src.grid import Grid
from src.utilis import Timer


MARGIN = 2


class SimulationGUI:
    def __init__(
        self, grid_size: tuple[int, int], screen_size: tuple[int, int] = (1000, 1000)
    ):
        self.grid_size = grid_size
        self.screen_size = screen_size

        self.bg_color = "#303030"
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_size = (
            self.screen_size[0] // self.grid_size[0],
            self.screen_size[1] // self.grid_size[1],
        )
        self.grid_background = self._get_grid_background()

        self.simulation = Simulation(grid_size)

        self.timer = Timer(0.15)
        self.running = False
        self.paused = True

    def render_grid(self, grid: Grid):
        n, m = self.grid_size
        for i in range(n):
            for j in range(m):
                color = "#FFFFFF" if grid[i][j] else self.bg_color
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        i * self.cell_size[0] + MARGIN,
                        j * self.cell_size[1] + MARGIN,
                        self.cell_size[0] - 2 * MARGIN,
                        self.cell_size[1] - 2 * MARGIN,
                    ),
                )

    def _get_grid_background(self) -> pygame.Surface:
        bg = pygame.Surface(self.screen_size)
        bg.fill(self.bg_color)
        n, m = self.grid_size
        for i in range(n):
            pygame.draw.line(
                bg,
                "#404040",
                (i * self.cell_size[0], 0),
                (i * self.cell_size[0], self.screen_size[1]),
            )
        for j in range(m):
            pygame.draw.line(
                bg,
                "#404040",
                (0, j * self.cell_size[1]),
                (self.screen_size[0], j * self.cell_size[1]),
            )
        return bg
    
    def update(self, time_delta: float):
        if self.paused:
            return
        if self.timer.tick(time_delta):
            self.simulation.step()
    
    def get_cell_by_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        return pos[0] // self.cell_size[0], pos[1] // self.cell_size[1]

    def process_click_event(self, event: pygame.event.Event):
        i, j = self.get_cell_by_pos(event.pos)
        self.simulation.current_grid[i][j] = not self.simulation.current_grid[i][j]
        
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.simulation.step()
            elif event.key == pygame.K_p:
                self.paused = not self.paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.process_click_event(event)

    def run(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            time_delta = clock.tick(60) * 0.001
            self.update(time_delta)
            for event in pygame.event.get():
                self.process_event(event)
            self.screen.blit(self.grid_background, (0, 0))
            self.render_grid(self.simulation.current_grid)
            pygame.display.flip()
        pygame.quit()
