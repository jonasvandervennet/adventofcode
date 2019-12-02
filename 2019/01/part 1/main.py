"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 3330521
"""


def mass_to_fuel(mass):
    return int(mass / 3) - 2


def main():
    with open('test.txt') as ifp:
        test_inputs = ifp.readlines()
    # cast read values to int
    test_inputs = [[int(val) for val in line.split()] for line in test_inputs]
    for mass, answer in test_inputs:
        assert(mass_to_fuel(mass) == answer)

    with open('../input.txt') as ifp:
        inputs = ifp.readlines()
    # cast read values to int
    inputs = [int(val) for val in inputs]
    # Sum of all fuel needs
    print(sum([mass_to_fuel(mass) for mass in inputs]))


if __name__ == '__main__':
    main()
