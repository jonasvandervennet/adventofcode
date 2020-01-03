"""
Written by: Jonas Vander Vennet
on: 2020/01/02
Answer: 899155
"""

import numpy as np
from glob import glob


def done(needed_materials, recipies, phase=1):
    for material, amount in needed_materials.items():
        if material in recipies.keys() and amount > 0 and material != 'ore':
            return False
    return True


def create_fuel(recipies):
    """
    recipies: dict with materials as keys,
    values are lists of tuples (inputs, output_amount). Inputs is a dictionary
    mapping materials to their needed/produced amount.
    """
    needed = recipies['fuel'][0]
    while not done(needed, recipies):
        new_needed = {k: v for k, v in needed.items()}
        for material, amount in needed.items():
            if amount <= 0:
                continue
            if material in recipies.keys():
                extra_needed, amount_got = recipies[material]
                iterations = int(np.ceil((amount * 1.0) / (amount_got * 1.0)))
                for extra_material, extra_amount in extra_needed.items():
                    if extra_material not in new_needed.keys():
                        new_needed[extra_material] = 0
                    for _ in range(iterations):
                        new_needed[extra_material] += extra_amount
                new_needed[material] -= iterations * amount_got
        needed = new_needed
    return needed['ore']


def load_mat_amount(input_text):
    amount, mat = input_text.split(' ')
    return (mat.lower(), int(amount))


def read_recipies(recipies_raw):
    recipies = {}
    for line in recipies_raw:
        line = line.replace('\n', '')
        inputs, outputs = line.split(' => ')
        out_mat, out_amount = load_mat_amount(outputs)
        if out_mat not in recipies.keys():
            recipies[out_mat] = {}, out_amount
        for material_def in inputs.split(', '):
            d = recipies[out_mat][0]
            mat, amount = load_mat_amount(material_def)
            if mat not in d.keys():
                d[mat] = 0
            d[mat] += amount
    return recipies


def main():
    outputs = [82892753, 5586022, 460664]
    for expected_out, filename in zip(outputs, sorted(glob('test*.txt'))):
        with open(filename) as ifp:
            recipies = ifp.readlines()
        recipies = read_recipies(recipies)
        num_ore = create_fuel(recipies)
        print(num_ore, expected_out)

    with open('../input.txt') as ifp:
        recipies = ifp.readlines()
    recipies = read_recipies(recipies)
    num_ore = create_fuel(recipies)
    print(num_ore)


if __name__ == '__main__':
    main()
