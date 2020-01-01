"""
Written by: Jonas Vander Vennet
on: 2020/01/01
Answer: 6227
"""

import numpy as np
from glob import glob


class Moon:
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z])
        self.vel = np.array([0, 0, 0])
        self.new_vel_offset = np.array([0, 0, 0])

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
        return f"pos=<x=  {x}, y= {y}, z= {z}>, vel=<x= {vx}, y= {vy}, z= {vz}>"


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
    return sum([moon.energy for moon in moons])


def main():
    outputs = [179, 1940]
    num_iterations = [10, 100]
    for expected_out, iterations, filename in zip(outputs, num_iterations, sorted(glob('test*.txt'))):
        moons = []
        with open(filename) as ifp:
            moon_positions = ifp.readlines()
        for line in moon_positions:
            moons.append(Moon(*get_xyz(line.replace('\n', ''))))
        energy = simulate(moons, iterations)
        assert(energy == expected_out)

    moons = []
    with open('../input.txt') as ifp:
        moon_positions = ifp.readlines()
    for line in moon_positions:
        moons.append(Moon(*get_xyz(line.replace('\n', ''))))
    energy = simulate(moons, 1000)
    print(energy)


if __name__ == '__main__':
    main()
