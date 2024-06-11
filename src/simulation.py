from src.grid import get_random_grid, get_clean_grid, next_step


class Simulation:
    def __init__(self, grid_size: tuple[int, int]):
        self.grid_size = grid_size
        self.current_grid = get_clean_grid(*self.grid_size)
    
    def step(self):
        self.current_grid = next_step(self.current_grid)
    
    def random_grid(self):
        self.current_grid = get_random_grid(*self.grid_size)

    def clean_grid(self):
        self.current_grid = get_clean_grid(*self.grid_size)
    