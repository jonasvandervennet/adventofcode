"""
Written by: Jonas Vander Vennet
on: 2019/12/04
Answer: 3620
"""
import numpy as np


def manhattan_dist(pos1: tuple, pos2: tuple):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_distances(pos: tuple, other: list):
    distances = [manhattan_dist(pos, coords) for coords in other]
    return distances


def get_boundaries(coords):
    min_x = min(coords, key=lambda x: x[0])[0]
    min_y = min(coords, key=lambda x: x[1])[1]
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]
    return min_x, min_y, max_x, max_y


def shift_coords(current, min_x, min_y):
    return [(x - min_x, y - min_y) for x, y in current]


def get_area_close_to_coords(coords, dist):
    area = 0
    boundaries = get_boundaries(coords)
    min_x, min_y, max_x, max_y = boundaries
    coords = shift_coords(coords, *boundaries[:2])
    grid = np.zeros((
        boundaries[2] - boundaries[0] + 1,
        boundaries[3] - boundaries[1] + 1), dtype=int)
    x_range = int((dist - (max_x - min_x)) / 2)
    y_range = int((dist - (max_y - min_y)) / 2)
    for x in range(max_x - x_range, min_x + 2*x_range + 1):
        for y in range(max_y - y_range, min_y + 2*y_range + 1):
            distances = get_distances((x, y), coords)
            if sum(distances) <= dist:
                print(x, y, get_distances((x, y), coords), sum(get_distances((x, y), coords)))
                area += 1
                grid[x, y] = 1
    for x, y in coords:
        grid[x, y] = 2
    print(grid)
    return area


def main():
    test_values = [
        ([
            (1, 1),
            (1, 6),
            (8, 3),
            (3, 4),
            (5, 5),
            (8, 9)
        ], 16),
    ]

    for coords, answer in test_values:
        result = get_area_close_to_coords(coords, 32)
        print(result, answer)
        assert(result == answer)

    with open('../input.txt') as ifp:
        coords = ifp.readlines()
    coords = [point.split(', ') for point in coords]
    coords = [tuple([int(point[0]), int(point[1])])for point in coords]
    result = get_area_close_to_coords(coords, 10000)
    print(result)


if __name__ == '__main__':
    main()
