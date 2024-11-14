from tkinter.tix import IMMEDIATE
from wsgiref.validate import validator


class IntCode:
    NUM_ARGS = 'NUM_ARGS'
    NUM_RESULTS = 'NUM_RESULTS'
    METHOD = 'METHOD'

    MODE_IMMEDIATE = 1
    MODE_POSITION = 0

    memory = []

    def value(self, arg):
        par = arg[0]
        par_mode = arg[1]
        if par_mode == IntCode.MODE_IMMEDIATE:
            return par
        elif par_mode == IntCode.MODE_POSITION:
            return self.memory[par]
        else:
            print("Unknown parameter mode: ", par_mode)
            exit(-1)

    def op_sum(self, args):
        arg1 = self.value(args[0])
        arg2 = self.value(args[1])
        res = arg1 + arg2
        ret = args[2][0]
        self.memory[ret] = res

    def op_mult(self, args):
        arg1 = args[0]
        arg2 = args[1]
        ret = args[2][0]
        self.memory[ret] = self.value(arg1) * self.value(arg2)

    def op_input(self, args):
        arg = args[0][0]
        value = input('>>> ')
        self.memory[arg] = int(value)

    def op_output(self, args):
        print('<<< ', self.value((args[0])))

    def op_jump_if_true(self, args):
        args = [self.value(x) for x in args]
        if args[0] != 0:
            return args[1]

    def op_jump_if_false(self, args):
        args = [self.value(x) for x in args]
        if args[0] == 0:
            return args[1]

    def op_less_than(self, args):
        values = [self.value(x) for x in args[:2]]
        ret = args[2][0]
        if values[0] < values[1]:
            self.memory[ret] = 1
        else:
            self.memory[ret] = 0

    def op_equals(self, args):
        values = [self.value(x) for x in args[:2]]
        ret = args[2][0]
        if values[0] == values[1]:
            self.memory[ret] = 1
        else:
            self.memory[ret] = 0


    operations = {1: {NUM_ARGS: 3, METHOD: op_sum},
                  2: {NUM_ARGS: 3, METHOD: op_mult},
                  3: {NUM_ARGS: 1, METHOD: op_input},
                  4: {NUM_ARGS: 1, METHOD: op_output},
                  5: {NUM_ARGS: 2, METHOD: op_jump_if_true},
                  6: {NUM_ARGS: 2, METHOD: op_jump_if_false},
                  7: {NUM_ARGS: 3, METHOD: op_less_than},
                  8: {NUM_ARGS: 3, METHOD: op_equals}
                  }

    def parse_opcode(self, opcode):
        op = opcode%100
        if op not in self.operations:
            print("Unknown operation op = ", op, ' memory dump: ', self.memory)
            exit(-1)
        modes = int(opcode/100)
        flags = []
        for i in range(self.operations[op][IntCode.NUM_ARGS]):
            flags.append(modes%10)
            modes = int(modes/10)
        return op, flags

    def run(self, program):
        self.memory = program
        pos = 0
        while True:
            opcode = self.memory[pos]
            if opcode == 99:
                break
            op, flags = self.parse_opcode(opcode)
            args = []
            for i in range(self.operations[op][IntCode.NUM_ARGS]):
                args.append((self.memory[pos+1+i], flags[i]))
            res = self.operations[op][IntCode.METHOD](self, args)
            if res is not None:
                pos = res
            else:
                pos += self.operations[op][IntCode.NUM_ARGS] + 1
        return self.memory
