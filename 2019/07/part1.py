"""
Written by: Jonas Vander Vennet
on: 2020/08/21
Answer: 77500
"""
from itertools import permutations
from intcode import Intcode

def thruster_settings(program):
    max_thrust = 0
    for phases in permutations(range(5, 10)):
        stdin = []
        stdout = [0]
        for phase in phases:
            stdin = [phase, stdout[0]]
            stdout = []
            input_program = program.copy()

            Intcode(input_program, stdin, stdout)
        max_thrust = max(max_thrust, stdout[0])
    return max_thrust

def main():
    with open('test.txt') as ifp:
        test_inputs = ifp.readlines()
    # cast read values to right format and type
    test_inputs = [
        [
            [int(integer) for integer in program.split(',')]
            for program in line.split(' ')]
        for line in test_inputs]
    for program, output in test_inputs:
        output = output[0]
        calculated_output = thruster_settings(program)
        if calculated_output != output:
            raise AssertionError(f'{calculated_output} != {output}')

    with open('input.txt') as ifp:
        inputs = ifp.readline()
    inputs.replace('\n', '')
    # cast read values to right format and type
    input_program = [int(integer) for integer in inputs.split(',')]

    output = thruster_settings(input_program)
    print(output)


if __name__ == '__main__':
    main()
