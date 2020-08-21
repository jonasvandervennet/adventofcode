"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 4484226
"""

from intcode import Intcode

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
        processor = Intcode(program)
        calculated_output = processor.result
        if calculated_output != output:
            raise AssertionError(f'{calculated_output} != {output}')

    with open('input.txt') as ifp:
        inputs = ifp.readlines()
    # cast read values to right format and type
    input_program = [
        [int(integer) for integer in program.split(',')]
        for program in inputs][0]

    # adapt the input program according to the exercise
    input_program[1] = 12
    input_program[2] = 2

    processor = Intcode(input_program)
    output = processor.result
    print(output[0])


if __name__ == '__main__':
    main()
