"""
Written by: Jonas Vander Vennet
on: 2019/12/04
Answer: 3620
"""
import numpy as np


def manhattan_dist(pos1: tuple, pos2: tuple):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def neareast_neighbour(pos: tuple, other: list):
    distances = [manhattan_dist(pos, coords) for coords in other]
    min_dist = min(distances)
    if distances.count(min_dist) > 1:
        return 0
    return distances.index(min_dist) + 1


def mark_neighbours(grid: np.array, coords: list):
    x_max, y_max = grid.shape
    for x in range(x_max):
        for y in range(y_max):
            grid[x, y] = neareast_neighbour((x, y), coords)


def get_boundaries(coords):
    min_x = min(coords, key=lambda x: x[0])[0]
    min_y = min(coords, key=lambda x: x[1])[1]
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]
    return min_x, min_y, max_x, max_y


def get_border_values(grid):
    return (
        set(grid[0, :])
        .union(grid[-1, :])
        .union(grid[:, 0])
        .union(grid[:, -1])
    )


def shift_coords(current, min_x, min_y):
    return [(x - min_x, y - min_y) for x, y in current]


def get_largest_finite_area(coords):
    boundaries = get_boundaries(coords)
    coords = shift_coords(coords, *boundaries[:2])
    grid = np.zeros((
        boundaries[2] - boundaries[0] + 1,
        boundaries[3] - boundaries[1] + 1), dtype=int)
    for i, (x, y) in enumerate(coords):
        grid[x, y] = i + 1
    mark_neighbours(grid, coords)
    finite_numbers = list(set([i + 1 for i in range(len(coords))]).difference(get_border_values(grid)))
    _, counts = np.unique(grid, return_counts=True)
    return np.amax(counts[finite_numbers])


def main():
    test_values = [
        ([
            (1, 1),
            (1, 6),
            (8, 3),
            (3, 4),
            (5, 5),
            (8, 9)
        ], 17),
    ]

    for coords, answer in test_values:
        result = get_largest_finite_area(coords)
        assert(result == answer)

    with open('../input.txt') as ifp:
        coords = ifp.readlines()
    coords = [point.split(', ') for point in coords]
    coords = [tuple([int(point[0]), int(point[1])])for point in coords]
    result = get_largest_finite_area(coords)
    print(result)


if __name__ == '__main__':
    main()
