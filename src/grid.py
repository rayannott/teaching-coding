import random


Grid = list[list[bool]]


def decide_cell(grid: Grid, i: int, j: int) -> bool:
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


def next_step(grid: Grid) -> Grid:
    """
    Returns the grid after one step of the Game of Life.
    """
    n = len(grid)
    m = len(grid[0])
    new_grid = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_grid[i][j] = decide_cell(grid, i, j)
    return new_grid


def game_of_life_seq(grid_0: Grid, steps: int) -> list[Grid]:
    """
    Returns the sequence of grids after `steps` steps of the Game of Life.
    """
    grids = [grid_0]
    for _ in range(steps):
        grid = next_step(grids[-1])
        grids.append(grid)
    return grids


def get_random_grid(N: int, M: int) -> Grid:
    """
    Returns a random grid of size N x M.
    """
    return [[random.choice([True, False]) for _ in range(M)] for _ in range(N)]


def get_clean_grid(N: int, M: int) -> Grid:
    """
    Returns a clean grid of size N x M.
    """
    return [[False for _ in range(M)] for _ in range(N)]
