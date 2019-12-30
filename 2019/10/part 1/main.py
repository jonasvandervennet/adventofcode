"""
Written by: Jonas Vander Vennet
on: 2019/12/30
Answer: 286
"""

from glob import glob


def read_map(asteroid_map):
    new_map = []
    for row in asteroid_map:
        new_map.append([])
        for char in row.replace('\n', ''):
            new_map[-1].append(char)
    return new_map


def get_asteroid_positions(asteroid_map):
    positions = []
    for i, row in enumerate(asteroid_map):
        for j, char in enumerate(row):
            if char == '#':
                positions.append((i, j))
    return positions


def amount_of_visible_asteroids(position, asteroid_positions):
    directions = set()
    for pos in asteroid_positions:
        if pos == position:
            continue
        if position[0] == pos[0]:
            direction = ''
        else:
            direction = str((position[1] - pos[1]) / (position[0] - pos[0]))  # dy/dx

        if position[1] < pos[1]:
            direction += 'R'
        else:
            direction += 'L'

        directions.add(direction)
    return len(directions)


def find_station_location(asteroid_map):
    positions = get_asteroid_positions(asteroid_map)
    most_seen = None
    best_position = None
    for asteroid in positions:
        seen = amount_of_visible_asteroids(asteroid, positions)
        if most_seen is None or seen > most_seen:
            most_seen = seen
            best_position = asteroid
    return best_position, most_seen


def main():
    outputs = [8, 33, 35, 41, 210]
    for expected_out, filename in zip(outputs, sorted(glob('test*.txt'))):
        with open(filename) as ifp:
            asteroid_map = ifp.readlines()
        asteroid_map = read_map(asteroid_map)
        _, asteroids_seen = find_station_location(asteroid_map)
        assert(asteroids_seen == expected_out)

    with open('../input.txt') as ifp:
        asteroid_map = ifp.readlines()
    asteroid_map = read_map(asteroid_map)
    _, asteroids_seen = find_station_location(asteroid_map)
    print(asteroids_seen)


if __name__ == '__main__':
    main()
