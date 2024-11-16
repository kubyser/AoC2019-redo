from IntCode import IntCode

f = open("resources/day9_input.txt", "r")
data = [int(x) for x in f.read().split(',')]
f.close()
computer = IntCode()
computer.run(data)
exit()

data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
computer.run(data)

data = [1102,34915192,34915192,7,4,7,99,0]
computer.run(data)

data = [104,1125899906842624,99]
computer.run(data)

