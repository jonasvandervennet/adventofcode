"""
Written by: Jonas Vander Vennet
on: 2019/12/31
Answer: 504
"""

from glob import glob


def dist(pos1, pos2):
    return (pos1[0] - pos2[0]) * (pos1[0] - pos2[0]) + (pos1[1] - pos2[1]) * (pos1[1] - pos2[1])


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


def asteroids_to_destroy(position, asteroid_positions):
    directions = {}
    for pos in asteroid_positions:
        if pos == position:
            continue
        if position[0] == pos[0]:
            direction = ''
        else:
            direction = str((pos[1] - position[1]) / (pos[0] - position[0]))  # dy/dx

        if position[1] < pos[1]:
            direction += 'R'
        elif position[1] > pos[1]:
            direction += 'L'
        elif position[0] < pos[0]:
            direction += 'D'
        else:
            direction += 'U'

        if direction not in directions.keys() or dist(position, pos) < dist(position, directions[direction]):
            directions[direction] = pos

    asteroids_in_order = []
    # Up
    for key, pos in directions.items():
        if 'U' in key:
            asteroids_in_order.append(pos)
            break
    # First quadrant
    to_sort = []
    for key in directions.keys():
        if '-' in key and 'R' in key:
            to_sort.append(key)
    for key in sorted(to_sort, key=lambda x: float(x[1:-1])):
        asteroids_in_order.append(directions[key])
    # Right
    if 'R' in directions.keys():
        asteroids_in_order.append(directions['R'])
    # Fourth quadrant
    to_sort = []
    for key in directions.keys():
        if '-' not in key and 'R' in key and key != 'R':
            to_sort.append(key)
    for key in sorted(to_sort, key=lambda x: -float(x[:-1])):
        asteroids_in_order.append(directions[key])
    # Down
    for key, pos in directions.items():
        if 'D' in key:
            asteroids_in_order.append(pos)
            break
    # Third quadrant
    to_sort = []
    for key in directions.keys():
        if '-' in key and 'L' in key:
            to_sort.append(key)
    for key in sorted(to_sort, key=lambda x: float(x[1:-1])):
        asteroids_in_order.append(directions[key])
    # Left
    if 'L' in directions.keys():
        asteroids_in_order.append(directions['L'])
    # Second quadrant
    to_sort = []
    for key in directions.keys():
        if '-' not in key and 'L' in key and key != 'L':
            to_sort.append(key)
    for key in sorted(to_sort, key=lambda x: -float(x[:-1])):
        asteroids_in_order.append(directions[key])

    return asteroids_in_order


def vaporize_200_asteroids(asteroid_map):
    station_position, _ = find_station_location(asteroid_map)
    # station_position = (13, 11)
    destroyed = 0
    while True:
        positions = get_asteroid_positions(asteroid_map)
        asteroids = asteroids_to_destroy(station_position, positions)
        for pos in asteroids:
            asteroid_map[pos[0]][pos[1]] = '.'
            destroyed += 1
            if destroyed == 200:
                return pos


def answer(asteroid_map):
    pos = vaporize_200_asteroids(asteroid_map)
    return pos[0] + 100 * pos[1]


def main():
    outputs = [802]
    for expected_out, filename in zip(outputs, sorted(glob('test*.txt'))):
        with open(filename) as ifp:
            asteroid_map = ifp.readlines()
        asteroid_map = read_map(asteroid_map)
        ans = answer(asteroid_map)
        assert(ans == expected_out)

    with open('../input.txt') as ifp:
        asteroid_map = ifp.readlines()
    asteroid_map = read_map(asteroid_map)
    ans = answer(asteroid_map)
    print(ans)


if __name__ == '__main__':
    main()
