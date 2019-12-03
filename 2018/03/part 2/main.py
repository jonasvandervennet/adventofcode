"""
Written by: Jonas Vander Vennet
on: 2019/12/03
Answer: 113
"""

import numpy as np


def claim_to_numbers(claim):
    id_, _, offsets, dimensions = claim.split(' ')
    id_ = int(id_[1:])
    offsets = tuple([int(offset) for offset in offsets[:-1].split(',')])
    dimensions = tuple([int(dim) for dim in dimensions.split('x')])
    return id_, offsets, dimensions


def get_max_dimensions(claims):
    x, y = 0, 0
    for _, offsets, dimensions in claims:
        x_dim = offsets[0] + dimensions[0]
        y_dim = offsets[1] + dimensions[1]
        if x_dim > x:
            x = x_dim
        if y_dim > y:
            y = y_dim
    return x, y


def claim_region(cloth, claim):
    _, offsets, dimensions = claim
    is_overlap = False
    for i in range(offsets[0], offsets[0] + dimensions[0]):
        for j in range(offsets[1], offsets[1] + dimensions[1]):
            if cloth[i, j] == -1 or cloth[i, j] == 1:
                is_overlap = True
    for i in range(offsets[0], offsets[0] + dimensions[0]):
        for j in range(offsets[1], offsets[1] + dimensions[1]):
            cloth[i, j] = -1 if is_overlap else 1


def do_claims(claims):
    x, y = get_max_dimensions(claims)
    cloth = np.zeros((x, y))
    for claim in claims:
        claim_region(cloth, claim)
    return cloth


def check_claim(cloth, claim):
    _, offsets, dimensions = claim
    for i in range(offsets[0], offsets[0] + dimensions[0]):
        for j in range(offsets[1], offsets[1] + dimensions[1]):
            if cloth[i, j] == -1:
                return False
    return True


def get_non_overlapping_claim(claims):
    claims = [claim_to_numbers(claim) for claim in claims]
    cloth = do_claims(claims)
    for claim in claims:
        if check_claim(cloth, claim):
            return claim[0]


def main():
    with open('../input.txt') as ifp:
        claims = ifp.readlines()
    overlaps = get_non_overlapping_claim(claims)
    print(overlaps)


if __name__ == '__main__':
    main()
