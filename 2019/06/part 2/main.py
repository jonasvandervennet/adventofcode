"""
Written by: Jonas Vander Vennet
on: 2019/12/30
Answer: 430
"""


def get_orbitmap(orbits):
    orbitmap = {}
    for center, orbiter in orbits:
        if center not in orbitmap.keys():
            orbitmap[center] = []
        if orbiter not in orbitmap.keys():
            orbitmap[orbiter] = []
        orbitmap[center].append(orbiter)
    return orbitmap


def get_center(node, orbitmap):
    for key, value in orbitmap.items():
        if node in value:
            return key


def path_to(node, orbitmap, destination='COM'):
    current = get_center(node, orbitmap)
    path = []
    while current != destination:
        path.append(current)
        current = get_center(current, orbitmap)
    return path


def get_intersection(path1, path2):
    # optimize speed of intersection searching
    # by looping over largest path first
    if len(path2) > len(path1):
        temp = path1
        path1 = path2
        path2 = temp

    for node1 in path1:
        for node2 in path2:
            if node1 == node2:
                return node1


def num_orbital_transfers(orbits):
    orbitmap = get_orbitmap(orbits)

    path_you, path_santa = path_to('YOU', orbitmap), path_to('SAN', orbitmap)
    intersection = get_intersection(path_you, path_santa)

    return path_you.index(intersection) + path_santa.index(intersection)


def main():
    expected_output = 4
    with open('test.txt') as ifp:
        orbit_declarations = ifp.readlines()
    orbit_declarations = [tuple(decl.replace('\n', '').split(')')) for decl in orbit_declarations]

    assert(num_orbital_transfers(orbit_declarations) == expected_output)

    with open('../input.txt') as ifp:
        orbit_declarations = ifp.readlines()
    orbit_declarations = [tuple(decl.replace('\n', '').split(')')) for decl in orbit_declarations]
    print(num_orbital_transfers(orbit_declarations))


if __name__ == '__main__':
    main()
