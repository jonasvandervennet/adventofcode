class Intcode():
    def __init__(self, program):
        self.program = program
        self.index = 0
        self.finished = False

        self.run()
    
    def run(self):
        while not self.finished:
            self.execute_step()
    
    def execute_step(self):
        opcode = self.program[self.index]

        if opcode == 1:
            # ADD
            num_params = 3
            left = self.program[self.program[self.index + 1]]
            right = self.program[self.program[self.index + 2]]
            self.program[self.program[self.index + 3]] = left + right
        elif opcode == 2:
            # MULTIPLY
            num_params = 3
            left = self.program[self.program[self.index + 1]]
            right = self.program[self.program[self.index + 2]]
            self.program[self.program[self.index + 3]] = left * right
        elif opcode == 99:
            # HALT OPERATION
            self.finished = True
            return

        self.index += num_params + 1
    
    @property
    def result(self):
        return self.program