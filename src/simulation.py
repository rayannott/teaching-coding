from enum import Enum, auto
from itertools import cycle
from typing import Iterable
import pathlib

from src.grid import get_random_grid, get_clean_grid, vanilla_step, ternary_step
from src.utilis import make_gif
from src.blueprint import Blueprint


BLUEPRINTS_DIR = pathlib.Path('blueprints')
BLUEPRINTS_FILE = BLUEPRINTS_DIR / 'bps.jsonl'


class Mode(Enum):
    VANILLA = auto()
    TERNARY = auto()


NEXT_STEP_FUNCTION_MAP = {
    Mode.VANILLA: vanilla_step,
    Mode.TERNARY: ternary_step,
}

COLOR_MAP = {
    Mode.VANILLA: {
        0: "#303030",
        1: "#FFFFFF",
    },
    Mode.TERNARY: {
        0: "#303030",
        1: "#ffcc99",
        2: "#66ccff",
    },
}


class Simulation:
    def __init__(self, grid_size: tuple[int, int], mode: Mode = Mode.VANILLA):
        self.grid_size = grid_size
        self.mode = mode
        self.allowed_values = list(COLOR_MAP[mode].keys())
        self.next_step_func = NEXT_STEP_FUNCTION_MAP[mode]
        self.current_grid = get_clean_grid(*self.grid_size)
        self._history = [self.current_grid.copy()]

        self.blueprints = self.load_blueprints()
        self.blueprints_iter = cycle(self.blueprints)

    @staticmethod
    def load_blueprints() -> set[Blueprint]:
        with open(BLUEPRINTS_FILE) as f:
            loaded = {Blueprint.deserialize(line.strip()) for line in f if not line.startswith('#') and line.strip()}
        print(f"Loaded {len(loaded)} blueprints.")
        return loaded
    
    def dump_blueprint(self, bp: Blueprint):
        with open(BLUEPRINTS_FILE, 'a') as f:
            f.write(bp.serialize() + '\n')

    def save_blueprint(self, bp: Blueprint):
        self.blueprints.add(bp)
        self.blueprints_iter = cycle(self.blueprints)

    def step(self):
        self.current_grid = self.next_step_func(self.current_grid)
        # self._history.append(self.current_grid.copy())
    
    def paste_blueprint(self, blueprint: Blueprint, cell: tuple[int, int], override_with_value_0: bool = True):
        for cell, val in self.iterate_blueprint_cells(blueprint, cell):
            if val == 0 and not override_with_value_0:
                continue
            self.current_grid[cell[0]][cell[1]] = val

    def iterate_blueprint_cells(self, blueprint: Blueprint, topleft: tuple[int, int]) -> Iterable[tuple[tuple[int, int], int]]:
        i, j = topleft
        n, m = len(blueprint.subgrid), len(blueprint.subgrid[0])
        for ki in range(n):
            for kj in range(m):
                if 0 <= i + ki < self.grid_size[0] and 0 <= j + kj < self.grid_size[1]:
                    cell = (i + ki, j + kj)
                    val = blueprint.subgrid[ki][kj]
                    yield cell, val

    def get_color(self, cell_val: int) -> str:
        return COLOR_MAP[self.mode][cell_val]

    def random_grid(self):
        self.current_grid = get_random_grid(*self.grid_size, values=self.allowed_values)

    def clean_grid(self):
        self.current_grid = get_clean_grid(*self.grid_size)

    def generate_gif(self):
        make_gif(self._history, COLOR_MAP[self.mode])
