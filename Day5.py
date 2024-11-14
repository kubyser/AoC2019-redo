from IntCode import IntCode

f = open("resources/day5_input.txt", "r")
data = [int(x) for x in f.read().split(',')]
f.close()
computer = IntCode()
computer.run(data)