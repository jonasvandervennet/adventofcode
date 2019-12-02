"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 82516
"""


def frequency_repeating_value(operations):
    """
    Return the frequency first seen twice when
    repeatedly looping over the given operations.
    """
    total = 0
    seen_values = set([total])
    while True:
        for op in operations:
            if op[0] == '+':
                total += int(op[1:])
            elif op[0] == '-':
                total -= int(op[1:])
            else:
                raise ValueError(f'Recieved wrong operation "{op}"')
            if total in seen_values:
                return total
            seen_values.add(total)


def main():
    test_values = [
        (['+1', '-1'], 0),
        (['+3', '+3', '+4', '-2', '-4'], 10),
        (['-6', '+3', '+8', '+5', '-6'], 5),
        (['+7', '+7', '-2', '-7', '-4'], 14),
    ]
    for test_input, test_output in test_values:
        assert(frequency_repeating_value(test_input) == test_output)

    with open('../input.txt') as ifp:
        inputs = ifp.readlines()
    print(f'First repeating frequency: {frequency_repeating_value(inputs)}')


if __name__ == '__main__':
    main()
