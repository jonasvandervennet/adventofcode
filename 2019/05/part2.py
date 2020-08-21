"""
Written by: Jonas Vander Vennet
on: 2020/08/21
Answer: 15586959
"""

from intcode import Intcode

def main():
    with open('test2.txt') as ifp:
        test_inputs = ifp.readlines()
    # cast read values to right format and type
    test_inputs = [
        [
            [int(integer) for integer in program.split(',')]
            for program in line.split(' ')]
        for line in test_inputs]
    inputs = [[7], [8], [9]]
    for stdin, (program, output) in zip(inputs, test_inputs):
        stdout = []
        calculated_output = Intcode(program, stdin, stdout).result
        if stdout != output:
            raise AssertionError(f'{stdout} != {output}')

    with open('input.txt') as ifp:
        inputs = ifp.readline()
    inputs.replace('\n', '')
    # cast read values to right format and type
    input_program = [int(integer) for integer in inputs.split(',')]

    stdin = [5]
    stdout = []

    output = Intcode(input_program, stdin, stdout).result
    print(stdout[0])


if __name__ == '__main__':
    main()
