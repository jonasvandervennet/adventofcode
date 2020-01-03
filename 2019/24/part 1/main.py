"""
Written by: Jonas Vander Vennet
on: 2020/01/03
Answer: 17321586
"""


import numpy as np


def read_map(bugmap):
    result = []
    for line in bugmap:
        row = []
        line = line.replace('\n', '')
        for char in line:
            row.append(0 if char == '.' else 1)
        result.append(np.array(row))
    return np.array(result)


def update(bugmap):
    newmap = bugmap.copy()
    y_max, x_max = bugmap.shape
    for i in range(y_max):
        if i == 0:
            y_offsets = [1, 0]
        elif i == y_max - 1:
            y_offsets = [-1, 0]
        else:
            y_offsets = [-1, 1, 0]
        for j in range(x_max):
            if j == 0:
                x_offsets = [1, 0]
            elif j == x_max - 1:
                x_offsets = [-1, 0]
            else:
                x_offsets = [-1, 1, 0]
            bug_count = 0
            for y_off in y_offsets:
                for x_off in x_offsets:
                    if y_off == 0 and x_off == 0:
                        continue
                    if y_off != 0 and x_off != 0:
                        continue  # only 4 adjacent tiles, not diagonal
                    if bugmap[i+y_off, j+x_off] == 1:
                        bug_count += 1
            if bug_count != 1 and bugmap[i, j] == 1:
                newmap[i, j] = 0
            elif bug_count in [1, 2] and bugmap[i, j] == 0:
                newmap[i, j] = 1
    return newmap


def encode(bugmap):
    encoding = ''
    for row in bugmap:
        for item in row:
            encoding += str(item)
    return encoding


def run_until_repeat(bugmap):
    history = set()
    encoding = encode(bugmap)
    while encoding not in history:
        history.add(encoding)
        bugmap = update(bugmap)
        encoding = encode(bugmap)
    return bugmap


def calc_biodiversity(bugmap):
    bugmap = run_until_repeat(bugmap)
    biodiversity = 0
    x_size = bugmap.shape[1]
    for y, x in np.argwhere(bugmap == 1):
        biodiversity += 2 ** (x + y * x_size)
    return biodiversity


def main():
    expected_out = 2129920
    with open('test.txt') as ifp:
        bugmap = ifp.readlines()
    bugmap = read_map(bugmap)
    biodiversity = calc_biodiversity(bugmap)
    assert(biodiversity == expected_out)

    with open('../input.txt') as ifp:
        bugmap = ifp.readlines()
    bugmap = read_map(bugmap)
    biodiversity = calc_biodiversity(bugmap)
    print(biodiversity)


if __name__ == '__main__':
    main()
