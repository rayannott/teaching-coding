import random
from typing import Callable


Grid = list[list[int]]


def neighbors(grid: Grid, i: int, j: int, unique_vals: int) -> list[int]:
    """
    Returns the count of each unique value in the neighbors of the cell at position (i, j) in the grid.
    """
    n = len(grid)
    m = len(grid[0])
    counts = [0] * unique_vals
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and x < n and y >= 0 and y < m and (x != i or y != j):
                counts[grid[x][y]] += 1
    return counts


def decide_cell_vanilla(grid: Grid, i: int, j: int) -> int:
    """
    Returns the next state of the cell at position (i, j) in the grid.
    """
    neighb = neighbors(grid, i, j, 2)
    count_alive = neighb[1]
    if grid[i][j]:
        return count_alive == 2 or count_alive == 3
    else:
        return count_alive == 3


def decide_cell_ternary(grid: Grid, i: int, j: int) -> int:
    neighb = neighbors(grid, i, j, 3)
    num_uniq_elements = len(set(neighb))
    if num_uniq_elements == 3:
        return neighb.index(min(neighb))
    cell = grid[i][j]
    return cell


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


def get_random_grid(N: int, M: int, values: list[int] = [0, 1]) -> Grid:
    """
    Returns a random grid of size N x M.

    N > 0, M > 0.
    """
    return [[random.choice(values) for _ in range(M)] for _ in range(N)]


def get_clean_grid(N: int, M: int) -> Grid:
    """
    Returns a clean grid of size N x M.

    N > 0, M > 0.
    """
    return [[0 for _ in range(M)] for _ in range(N)]
