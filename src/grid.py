import random
from typing import Callable


Grid = list[list[int]]


def decide_cell_vanilla(grid: Grid, i: int, j: int) -> int:
    """
    Returns the next state of the cell at position (i, j) in the grid.
    """
    n = len(grid)
    m = len(grid[0])
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and x < n and y >= 0 and y < m and (x != i or y != j):
                count += grid[x][y]
    if grid[i][j]:
        return count == 2 or count == 3
    else:
        return count == 3


def decide_cell_ternary(grid: Grid, i: int, j: int) -> int:
    n = len(grid)
    m = len(grid[0])
    counts = [0, 0, 0]
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and x < n and y >= 0 and y < m and (x != i or y != j):
                counts[grid[x][y]] += 1
    # argmax
    picked = counts.index(min(counts))
    return (picked + 1) % 3


def next_step(grid: Grid, decider_func: Callable[[Grid, int, int], int]) -> Grid:
    """
    Returns the grid after one step of the Game of Life.
    """
    n = len(grid)
    m = len(grid[0])
    new_grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_grid[i][j] = decider_func(grid, i, j)
    return new_grid


def vanilla_step(grid: Grid) -> Grid:
    return next_step(grid, decide_cell_vanilla)


def ternary_step(grid: Grid) -> Grid: 
    return next_step(grid, decide_cell_ternary)


def get_random_grid(N: int, M: int, values: list[int]) -> Grid:
    """
    Returns a random grid of size N x M.
    """
    return [[random.choice(values) for _ in range(M)] for _ in range(N)]


def get_clean_grid(N: int, M: int) -> Grid:
    """
    Returns a clean grid of size N x M.
    """
    return [[0 for _ in range(M)] for _ in range(N)]
