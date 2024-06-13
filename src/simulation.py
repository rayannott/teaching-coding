from enum import Enum, auto
from itertools import cycle
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
    def load_blueprints() -> list[Blueprint]:
        with open(BLUEPRINTS_FILE) as f:
            return [Blueprint.deserialize(line.strip()) for line in f]
    
    def dump_blueprint(self, bp: Blueprint):
        with open(BLUEPRINTS_FILE, 'a') as f:
            f.write(bp.serialize() + '\n')

    def step(self):
        self.current_grid = self.next_step_func(self.current_grid)
        # self._history.append(self.current_grid.copy())

    def get_color(self, cell_val: int) -> str:
        return COLOR_MAP[self.mode][cell_val]

    def random_grid(self):
        self.current_grid = get_random_grid(*self.grid_size, values=self.allowed_values)

    def clean_grid(self):
        self.current_grid = get_clean_grid(*self.grid_size)

    def generate_gif(self):
        make_gif(self._history, COLOR_MAP[self.mode])
