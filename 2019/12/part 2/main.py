"""
Written by: Jonas Vander Vennet
on: 2020/01/02
Answer: 331346071640472
"""

import numpy as np
from glob import glob
from time import time


class Moon:
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z])
        self.vel = np.array([0, 0, 0])
        self.new_vel_offset = np.array([0, 0, 0])

        self.history = set()
        self.readable_history = []

    def gravity(self, other):
        assert(isinstance(other, Moon))
        offset = [0, 0, 0]
        for i in range(3):
            s = self.pos[i]
            o = other.pos[i]
            if s < o:
                offset[i] = 1
            elif s > o:
                offset[i] = -1
        self.new_vel_offset = self.new_vel_offset + offset

    def update(self):
        self.vel = self.vel + self.new_vel_offset
        self.pos = self.pos + self.vel
        self.new_vel_offset = np.array([0, 0, 0])

    @property
    def energy(self):
        kinetic = sum([abs(i) for i in self.vel])
        potential = sum([abs(i) for i in self.pos])
        return kinetic * potential

    def __str__(self):
        x, y, z = self.pos
        vx, vy, vz = self.vel
        return f"pos=<x= {x}, y= {y}, z= {z}>, vel=<x= {vx}, y= {vy}, z= {vz}>"

    def state(self, dimension):
        i = ['X', 'Y', 'Z'].index(dimension)
        return f"{self.pos[i]}&{self.vel[i]}"


def get_xyz(line):
    line = line[1:-1]
    xyz = [0, 0, 0]
    for i, part in enumerate(line.split(',')):
        xyz[i] = int(part.split('=')[-1])
    return xyz


def simulate(moons, iterations):
    for i in range(iterations):
        for m1 in moons:
            for m2 in moons:
                if m1 != m2:
                    m1.gravity(m2)
        for moon in moons:
            moon.update()
    for moon in moons:
        print(moon)
    return sum([moon.energy for moon in moons])


def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


def lcm(x, y, z=None):
    if z is None:
        # two arguments
        return x / gcd(x, y) * y
    return lcm(lcm(x, y), z)


def simulate_until_repeat(moons):
    """
    Different dimensions are independent from each other.
    Calculate each dimension seperately and then find the lowest
    common multiple of the three turnarounds.
    """
    variables = ['X', 'Y', 'Z']
    turnarounds = [0 for i in range(3)]
    for i, dimension in enumerate(variables):
        turnarounds[i] = simulate_dimension_until_repeat(moons, dimension)
    return int(lcm(*turnarounds))


def simulate_dimension_until_repeat(moons, dimension):
    i = 0
    history = set()
    while True:
        state = ''
        for m1 in moons:
            for m2 in moons:
                if m1 != m2:
                    m1.gravity(m2)
        for moon in moons:
            moon.update()
        for moon in moons:
            state += moon.state(dimension)
        if state in history:
            return i
        history.add(state)
        i += 1


def main():
    outputs = [2772, 4686774924]
    for expected_out, filename in zip(outputs, sorted(glob('test*.txt'))):
        start = time()
        moons = []
        with open(filename) as ifp:
            moon_positions = ifp.readlines()
        for line in moon_positions:
            moons.append(Moon(*get_xyz(line.replace('\n', ''))))
        iterations = simulate_until_repeat(moons)
        end = time() - start
        print(f"{iterations} iterations took {end} seconds")
        assert(iterations == expected_out)

    start = time()
    moons = []
    with open('../input.txt') as ifp:
        moon_positions = ifp.readlines()
    for line in moon_positions:
        moons.append(Moon(*get_xyz(line.replace('\n', ''))))
    iterations = simulate_until_repeat(moons)
    end = time() - start
    print(f"{iterations} iterations took {end} seconds")


if __name__ == '__main__':
    main()
