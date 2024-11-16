class IntCode:
    NUM_ARGS = 'NUM_ARGS'
    NUM_RESULTS = 'NUM_RESULTS'
    METHOD = 'METHOD'

    MODE_IMMEDIATE = 1
    MODE_POSITION = 0

    memory = []
    position = 0
    input_stream = []
    output_stream = []

    pause_flag = False
    pause_on_input = False

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
        if self.input_stream is None or len(self.input_stream) == 0:
            if self.pause_on_input:
                self.pause_flag = True
                return
            value = input('>>> ')
        else:
            value = self.input_stream.pop(0)
        self.memory[arg] = int(value)

    def op_output(self, args):
        if self.output_stream is None:
            print('<<< ', self.value((args[0])))
        else:
            self.output_stream.append(self.value((args[0])))

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

    def run(self, program, input_stream = None, output_stream = None, pause_on_input = False):
        self.pause_on_input = pause_on_input
        if not self.pause_flag:
            self.memory = program.copy()
            self.position = 0
        self.input_stream = input_stream
        self.output_stream = output_stream
        self.pause_flag = False
        while True:
            opcode = self.memory[self.position]
            if opcode == 99:
                break
            op, flags = self.parse_opcode(opcode)
            args = []
            for i in range(self.operations[op][IntCode.NUM_ARGS]):
                args.append((self.memory[self.position+1+i], flags[i]))
            res = self.operations[op][IntCode.METHOD](self, args)
            if self.pause_flag:
                break
            if res is not None:
                self.position = res
            else:
                self.position += self.operations[op][IntCode.NUM_ARGS] + 1
        return self.memory, self.pause_flag

    def run_chain(self, num_computers, init_values, program, input_stream, output_stream):
        inp_stream = [init_values[0]] + input_stream
        comps = []
        for x in range(num_computers):
            comps.append(IntCode())
        first_run = True
        while True:
            for x in range(num_computers):
                out_stream = []
                mem, paused = comps[x].run(program, inp_stream, out_stream, True)
                if x == num_computers-1 and not paused:
                    output_stream += out_stream
                    return
                else:
                    if first_run and x != num_computers-1:
                        inp_stream = [init_values[x+1]] + out_stream
                    else:
                        inp_stream = out_stream
            first_run = False
