import pygame

from src.simulation import Simulation, Mode
from src.utilis import Timer, mute_color

from src.blueprint import Blueprint


MARGIN = 1


class SimulationGUI:
    def __init__(
        self, grid_size: tuple[int, int], screen_size: tuple[int, int] = (1300, 1000)
    ):
        self.grid_size = grid_size
        self.screen_size = screen_size

        self.bg_color = "#303030"
        self.screen = pygame.display.set_mode(self.screen_size)
        min_screen_size = min(self.screen_size)
        self.grid_screen_size = (min_screen_size, min_screen_size)
        self.grid_screen = pygame.Surface(self.grid_screen_size)
        self.cell_size = min_screen_size // max(self.grid_size)
        self.grid_background = self._get_grid_background()

        self.simulation = Simulation(grid_size, mode=Mode.VANILLA)

        self.timer = Timer(0.15)
        self.running = False
        self.paused = True

        self.cell_down = None
        self.cell_up = None

        self.bp_hand = None

    def draw_cell(self, i: int, j: int, color: str):
        pygame.draw.rect(
            self.grid_screen,
            color,
            (
                i * self.cell_size + MARGIN,
                j * self.cell_size + MARGIN,
                self.cell_size - 2 * MARGIN,
                self.cell_size - 2 * MARGIN,
            ),
        )

    def render_grid(self):
        grid = self.simulation.current_grid
        n, m = self.grid_size
        for i in range(n):
            for j in range(m):
                color = self.simulation.get_color(grid[i][j])
                self.draw_cell(i, j, color)

    def render_blueprint(self):
        if self.bp_hand is None:
            return
        pos = pygame.mouse.get_pos()
        cell_hover = self.get_cell_by_pos(pos)
        if cell_hover is None:
            return
        is_ctrl_mode = pygame.key.get_mods() & pygame.KMOD_CTRL
        for cell, val in self.simulation.iterate_blueprint_cells(self.bp_hand, cell_hover):
            if is_ctrl_mode and val == 0:
                continue
            color = self.simulation.get_color(val)
            if color != self.bg_color:
                color = mute_color(color)
            self.draw_cell(*cell, color)

    def _get_grid_background(self) -> pygame.Surface:
        bg = pygame.Surface(self.grid_screen_size)
        bg.fill(self.bg_color)
        n, m = self.grid_size
        for i in range(n):
            pygame.draw.line(
                bg,
                "#404040",
                (i * self.cell_size, 0),
                (i * self.cell_size, self.screen_size[1]),
            )
        for j in range(m):
            pygame.draw.line(
                bg,
                "#404040",
                (0, j * self.cell_size),
                (self.screen_size[0], j * self.cell_size),
            )
        return bg

    def update(self, time_delta: float):
        if self.paused:
            return
        if self.timer.tick(time_delta):
            self.simulation.step()

    def get_cell_by_pos(self, pos: tuple[int, int]) -> tuple[int, int] | None:
        if not self.grid_screen.get_rect().collidepoint(pos):
            return None
        return pos[0] // self.cell_size, pos[1] // self.cell_size

    def process_click_event(self, event: pygame.event.Event, is_mouse_up: bool):
        click = self.get_cell_by_pos(event.pos)
        if click is None:
            print("Click outside grid")
            return
        is_shift_mode = pygame.key.get_mods() & pygame.KMOD_SHIFT
        is_ctrl_mode = pygame.key.get_mods() & pygame.KMOD_CTRL
        if is_mouse_up:
            self.cell_up = click
        else:
            self.cell_down = click
        if not is_shift_mode and self.cell_down == self.cell_up:
            # switch cell state
            i, j = click
            if self.bp_hand is None:
                print("switch cell state", click)
                self.simulation.current_grid[i][j] = (
                    self.simulation.current_grid[i][j] + 1
                ) % len(self.simulation.allowed_values)
            else:
                # paste blueprint
                print("paste blueprint at", click)
                self.simulation.paste_blueprint(self.bp_hand, click, override_with_value_0=not is_ctrl_mode)
            self.cell_down, self.cell_up = None, None
        elif (
            is_shift_mode
            and self.cell_down
            and self.cell_up
            and self.cell_down != self.cell_up
        ):
            # create blueprint
            self.bp_hand = Blueprint(
                self.simulation.current_grid, self.cell_down, self.cell_up
            )
            print("new blueprint in hand:", self.bp_hand)
            self.cell_down, self.cell_up = None, None

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_SPACE:
                self.simulation.step()
            elif event.key == pygame.K_p:
                self.paused = not self.paused
            elif event.key == pygame.K_r:
                self.simulation.random_grid()
            elif event.key == pygame.K_c:
                self.simulation.clean_grid()
            elif event.key == pygame.K_q:
                self.bp_hand = None
            elif event.key == pygame.K_x:
                self.bp_hand = next(self.simulation.blueprints_iter)
                print("blueprint in hand:", self.bp_hand)
            elif event.key == pygame.K_s:
                if self.bp_hand is None:
                    print("no blueprint in hand to save")
                    return
                self.simulation.save_blueprint(self.bp_hand)
            elif event.key == pygame.K_d:
                if self.bp_hand is None:
                    print("no blueprint in hand to dump")
                    return
                self.simulation.dump_blueprint(self.bp_hand)
            elif event.key == pygame.K_UP:
                self.timer.current_time = 0.
                self.timer.max_time *= 0.75
                print(self.timer.max_time)
            elif event.key == pygame.K_DOWN:
                self.timer.current_time = 0.
                self.timer.max_time *= 1.25
                print(self.timer.max_time)
            elif event.key == pygame.K_g:
                self.simulation.generate_gif()
        elif event.type in {pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP}:
            if event.button in {1, 3}:
                self.process_click_event(event, event.type == pygame.MOUSEBUTTONUP)
            else:
                # scroll
                print(f'scroll {"up" if event.button == 4 else "down"}')


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
            self.render_grid()
            self.render_blueprint()
            self.screen.blit(self.grid_background, (0, 0))
            self.screen.blit(self.grid_screen, (0, 0))
            pygame.display.flip()
        pygame.quit()
