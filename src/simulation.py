from src.grid import get_random_grid, next_step


class Simulation:
    def __init__(self, grid_size: tuple[int, int]):
        self.grid_size = grid_size
        self.current_grid = get_random_grid(*grid_size)
    
    def step(self):
        self.current_grid = next_step(self.current_grid)
    