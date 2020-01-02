"""
Written by: Jonas Vander Vennet
on: 2019/12/09
Answer: 9775037
"""


def get_operand(program: list, idx: int, mode: str):
    if mode == '0':
        return program[program[idx]]
    elif mode == '1':
        return program[idx]
    else:
        raise ValueError(f'Recieved invalid parameter mode {mode}')


def execute_intcode(program: list, stdin=[], stdout=[]):
    """
    Execute an intcode program:
    opcode 1: sum values at indices given by next to values,
              store at index of the third value
    opcode 2: multiply values at indices given by next to values,
              store at index of the third value
    opcode 3: store input value at position given by only parameter
    opcode 4: output value stored at position given by only parameter
    5,6,7,8
    opcode 99: halt


    Potential issue: should third parameters also
                     be checked with get_operand()?
    """
    i = 0
    while i < len(program):
        instruction = str(program[i])
        instruction = instruction.zfill(5)
        opcode = int(instruction[-2:])
        mode_3, mode_2, mode_1 = instruction[:-2]
        if opcode == 99:
            return program

        if opcode == 1:
            left = get_operand(program, i + 1, mode_1)
            right = get_operand(program, i + 2, mode_2)
            location = get_operand(program, i + 3, mode_3)
            result = left + right
            program[location] = result
            i += 4
        elif opcode == 2:
            left = get_operand(program, i + 1, mode_1)
            right = get_operand(program, i + 2, mode_2)
            location = get_operand(program, i + 3, mode_3)
            result = left * right
            program[location] = result
            i += 4
        elif opcode == 3:
            input_value = stdin.pop(0)  # pop front
            program[program[i + 1]] = input_value
            i += 2
        elif opcode == 4:
            output_value = get_operand(program, i + 1, mode_1)
            stdout.append(output_value)
            if output_value != 0:
                return  # shouldn't happend, this is meant for debugging
            i += 2
        elif opcode == 5:
            condition = get_operand(program, i + 1, mode_1)
            destination = get_operand(program, i + 2, mode_2)
            if condition != 0:
                i = destination
            else:
                i += 3
        elif opcode == 6:
            condition = get_operand(program, i + 1, mode_1)
            destination = get_operand(program, i + 2, mode_2)
            if condition == 0:
                i = destination
            else:
                i += 3
        elif opcode == 7:
            left = get_operand(program, i + 1, mode_1)
            right = get_operand(program, i + 2, mode_2)
            location = get_operand(program, i + 3, mode_3)
            to_store = int(left < right)
            program[location] = to_store
            i += 4
        elif opcode == 8:
            left = get_operand(program, i + 1, mode_1)
            right = get_operand(program, i + 2, mode_2)
            location = get_operand(program, i + 3, mode_3)
            to_store = int(left == right)
            program[location] = to_store
            i += 4
        else:
            raise Exception(f'invalid opcode received: {opcode}')


def main():
    with open('test.txt') as ifp:
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
        print(stdin)
        calculated_output = execute_intcode(program, stdin, stdout)
        print(stdout)
        # if stdout != output:
        #     raise AssertionError(f'{stdout} != {output}')

    with open('../input.txt') as ifp:
        inputs = ifp.readline()
    inputs.replace('\n', '')
    # cast read values to right format and type
    input_program = [int(integer) for integer in inputs.split(',')]

    stdin = [5]
    stdout = []

    output = execute_intcode(input_program, stdin, stdout)
    print(stdout)


if __name__ == '__main__':
    main()
