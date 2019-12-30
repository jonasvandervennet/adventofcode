"""
Written by: Jonas Vander Vennet
on: 2019/12/30
Answer: kfaby
"""

import numpy as np


def to_layers(image: str, height: int, width: int):
    layer_size = height * width
    num_layers = int(len(image) / layer_size)
    image = np.array([int(i) for i in image]).reshape((num_layers, height, width))
    return image


def first_non_two(sequence):
    for i in sequence:
        if i != 2:
            return i


def to_string(image):
    image = image.flatten()
    string = ''
    for i in image:
        string += str(i)
    return string


def answer(image):
    num_layers, height, width = image.shape
    result = np.zeros((height, width)).astype(int)
    for i in range(height):
        for j in range(width):
            result[i, j] = first_non_two(image[:, i, j])
    print(result)
    return to_string(result)


def main():
    expected_output = '0110'
    with open('test.txt') as ifp:
        height, width, image_data = ifp.readline().split(' ')
    output = answer(to_layers(image_data, int(height), int(width)))
    assert(output == expected_output)

    with open('../input.txt') as ifp:
        height, width, image_data = ifp.readline().split(' ')
    output = answer(to_layers(image_data, int(height), int(width)))
    print(output)


if __name__ == '__main__':
    main()
