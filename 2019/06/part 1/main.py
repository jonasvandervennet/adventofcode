"""
Written by: Jonas Vander Vennet
on: 2019/12/29
Answer: 223251
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


def num_direct_indirect_orbits(orbits):
    orbitmap = get_orbitmap(orbits)
    num_orbits = 0
    level = 1
    current = ['COM']
    while len(current) > 0:
        next_level = []
        for node in current:
            for neightbour in orbitmap[node]:
                num_orbits += level
            next_level += orbitmap[node]
        current = next_level
        level += 1
    return num_orbits


def main():
    expected_output = 42
    with open('test.txt') as ifp:
        orbit_declarations = ifp.readlines()
    orbit_declarations = [tuple(decl.replace('\n', '').split(')')) for decl in orbit_declarations]

    assert(num_direct_indirect_orbits(orbit_declarations) == expected_output)

    with open('../input.txt') as ifp:
        orbit_declarations = ifp.readlines()
    orbit_declarations = [tuple(decl.replace('\n', '').split(')')) for decl in orbit_declarations]
    print(num_direct_indirect_orbits(orbit_declarations))


if __name__ == '__main__':
    main()
