class Intcode():
    def __init__(self, program, inputs=[], outputs=[]):
        self.program = program
        self.inputs = inputs
        self.outputs = outputs
        self.index = 0
        self.finished = False

        self.run()
    
    def run(self):
        while not self.finished:
            self.execute_step()
        
        # if len(self.outputs) > 0 and self.outputs.count(0) != len(self.outputs) - 1:
        #     raise ValueError(f"Error code: {self.outputs}")
    
    def get_parameter(self, value, mode):
        if mode == '0':
            return self.program[self.program[value]]
        elif mode == '1':
            return self.program[value]
    
    def execute_step(self):
        instruction = str(self.program[self.index])
        instruction = instruction.zfill(5)
        opcode = int(instruction[-2:])
        mode_3, mode_2, mode_1 = instruction[:-2]

        if opcode == 1:
            # ADD
            num_params = 3
            left = self.get_parameter(self.index + 1, mode_1)
            right = self.get_parameter(self.index + 2, mode_2)
            self.program[self.program[self.index + 3]] = left + right
        elif opcode == 2:
            # MULTIPLY
            num_params = 3
            left = self.get_parameter(self.index + 1, mode_1)
            right = self.get_parameter(self.index + 2, mode_2)
            self.program[self.program[self.index + 3]] = left * right
        elif opcode == 3:
            # STORE
            num_params = 1
            self.program[self.program[self.index + 1]] = self.inputs.pop(0)
        elif opcode == 4:
            # LOAD
            num_params = 1
            self.outputs.append(self.get_parameter(self.index + 1, mode_1))
        elif opcode == 5:
            # JUMP IF TRUE
            num_params = 2
            condition = self.get_parameter(self.index + 1, mode_1)
            if condition != 0:
                self.index = self.get_parameter(self.index + 2, mode_2)
                return
        elif opcode == 6:
            # JUMP IF FALSE
            num_params = 2
            condition = self.get_parameter(self.index + 1, mode_1)
            if condition == 0:
                self.index = self.get_parameter(self.index + 2, mode_2)
                return
        elif opcode == 7:
            # LESS THAN
            num_params = 3
            left = self.get_parameter(self.index + 1, mode_1)
            right = self.get_parameter(self.index + 2, mode_2)
            self.program[self.program[self.index + 3]] = int(left < right)
        elif opcode == 8:
            # EQUAL
            num_params = 3
            left = self.get_parameter(self.index + 1, mode_1)
            right = self.get_parameter(self.index + 2, mode_2)
            self.program[self.program[self.index + 3]] = int(left == right)
        elif opcode == 99:
            # HALT OPERATION
            self.finished = True
            return
        else:
            raise ValueError(f"OPCODE: {opcode}")

        self.index += num_params + 1
    
    @property
    def result(self):
        return self.program