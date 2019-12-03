"""
Written by: Jonas Vander Vennet
on: 2019/12/03
Answer: 375
"""


def manhattan_distance(pos1, pos2):
    dist = 0
    for i in range(len(pos1)):
        dist += abs(pos1[i] - pos2[i])
    return dist


def move_amount(start, offset, amount):
    return [
        (start[0] + (i + 1) * offset[0], start[1] + (i + 1) * offset[1])
        for i in range(amount)]


def get_wire_paths(wire_movement, start=(0, 0)):
    visited = [start]
    for movement in wire_movement:
        direction = movement[0]
        amount = int(movement[1:])
        if direction == 'U':
            offset = (0, 1)
        elif direction == 'D':
            offset = (0, -1)
        elif direction == 'R':
            offset = (1, 0)
        elif direction == 'L':
            offset = (-1, 0)
        else:
            raise ValueError(f'Recieved invalid movement direction: {direction}')
        visited = visited + move_amount(visited[-1], offset, amount)
    return visited


def get_wire_intersections(w1, w2):
    w1_visited = get_wire_paths(w1)
    w2_visited = get_wire_paths(w2)
    w2_set = set(w2_visited)  # better for cheking contents

    intersections = [
        position
        for position in w1_visited
        if position != (0, 0) and position in w2_set]
    return intersections


def get_closest_intersection(w1, w2):
    intersections = get_wire_intersections(w1, w2)
    best_intersection = None
    best_dist = None
    for intersection in intersections:
        dist = manhattan_distance((0, 0), intersection)
        if best_dist is None or dist < best_dist:
            best_dist = dist
            best_intersection = intersection
    return best_intersection, best_dist


def main():
    test_values = [
        (['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'], 6),
        (['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'], 159),
        (['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'], 135)
    ]

    for w1, w2, answer in test_values:
        closest_intersection, dist = get_closest_intersection(w1, w2)
        assert(dist == answer)

    with open('../input.txt') as ifp:
        w1, w2 = ifp.readlines()
    w1 = w1.split(',')
    w2 = w2.split(',')
    _, dist = get_closest_intersection(w1, w2)
    print(dist)


if __name__ == '__main__':
    main()
