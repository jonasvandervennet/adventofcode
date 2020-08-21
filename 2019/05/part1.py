"""
Written by: Jonas Vander Vennet
on: 2019/12/09
Answer: 9775037
"""

from intcode import Intcode


def main():
    with open('test1.txt') as ifp:
        test_inputs = ifp.readlines()
    # cast read values to right format and type
    test_inputs = [
        [
            [int(integer) for integer in program.split(',')]
            for program in line.split(' ')]
        for line in test_inputs]
    for program, output in test_inputs:
        calculated_output = Intcode(program).result
        if calculated_output != output:
            raise AssertionError(f'{calculated_output} != {output}')

    with open('input.txt') as ifp:
        inputs = ifp.readline()
    inputs.replace('\n', '')
    # cast read values to right format and type
    input_program = [int(integer) for integer in inputs.split(',')]

    stdin = [1]
    stdout = []

    output = Intcode(input_program, stdin, stdout).result
    print(stdout)


if __name__ == '__main__':
    main()
