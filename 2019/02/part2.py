"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 5696
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

    GOAL = 19690720

    for noun in range(100):  # [0, 99] inclusive
        for verb in range(100):  # [0, 99] inclusive
            # don't change the original memory structure
            current_program = input_program.copy()

            # adapt the program according to the exercise
            current_program[1] = noun
            current_program[2] = verb
            
            processor = Intcode(current_program)
            output = processor.result

            if output[0] == GOAL:
                print(f'Reached the goal using noun: {noun} and verb: {verb}')
                print(f'Answer: {100 * noun + verb}')


if __name__ == '__main__':
    main()
