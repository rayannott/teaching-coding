from collections import Counter

from src.grid import get_clean_grid, get_random_grid


def test_get_clean_grid():
    grid = get_clean_grid(3, 3)
    assert grid == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    grid = get_clean_grid(2, 4)
    assert grid == [[0, 0, 0, 0], [0, 0, 0, 0]]

    grid = get_clean_grid(1, 1)
    assert grid == [[0]]


def test_get_random_grid():
    grid = get_random_grid(120, 80)
    counter = Counter([cell for row in grid for cell in row])
    assert counter[0] + counter[1] == 120 * 80
    assert abs(counter[0] - counter[1]) / (120 * 80) < 0.1
