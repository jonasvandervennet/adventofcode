"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 578
"""


def frequency_drift_result(operations):
    total = 0
    for op in operations:
        if op[0] == '+':
            total += int(op[1:])
        elif op[0] == '-':
            total -= int(op[1:])
        else:
            raise ValueError(f'Recieved wrong operation "{op}"')
    return total


def main():
    with open('../input.txt') as ifp:
        inputs = ifp.readlines()

    print(f'Resulting frequency: {frequency_drift_result(inputs)}')


if __name__ == '__main__':
    main()
