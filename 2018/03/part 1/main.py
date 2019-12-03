"""
Written by: Jonas Vander Vennet
on: 2019/12/03
Answer: 111485
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
    for i in range(offsets[0], offsets[0] + dimensions[0]):
        for j in range(offsets[1], offsets[1] + dimensions[1]):
            cloth[i, j] += 1


def do_claims(claims):
    x, y = get_max_dimensions(claims)
    cloth = np.zeros((x, y))
    for claim in claims:
        claim_region(cloth, claim)
    return cloth


def get_claim_overlap(claims):
    claims = [claim_to_numbers(claim) for claim in claims]
    cloth = do_claims(claims)
    return (cloth > 1).sum()


def main():
    test_values = [
        (['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 4),
    ]

    for claims, answer in test_values:
        overlaps = get_claim_overlap(claims)
        print(overlaps, answer)
        assert(overlaps == answer)

    with open('../input.txt') as ifp:
        claims = ifp.readlines()
    overlaps = get_claim_overlap(claims)
    print(overlaps)


if __name__ == '__main__':
    main()
