"""
Written by: Jonas Vander Vennet
on: 2019/12/30
Answer: 1716
"""


def to_layers(image: str, height: int, width: int):
    layer_size = height * width
    num_layers = int(len(image) / layer_size)
    layers = []
    for i in range(num_layers):
        layer = []
        for j in range(height):
            layer.append([])
            for k in range(width):
                layer[-1].append(int(image[i*layer_size+j*width+k]))
        layers.append(layer)
    return layers


def answer(layers):
    amount_of_zeros = None
    ans = None
    for layer in layers:
        num_zeros = 0
        new_ans = (0, 0)
        for row in layer:
            num_zeros += row.count(0)
            new_ans = (new_ans[0] + row.count(1), new_ans[1] + row.count(2))
        if amount_of_zeros is None or num_zeros < amount_of_zeros:
            amount_of_zeros = num_zeros
            ans = new_ans
    return ans[0]*ans[1]


def main():
    expected_output = 1
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
