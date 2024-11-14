from IntCode import IntCode

data = [1,9,10,3,2,3,11,0,99,30,40,50]
computer = IntCode()
data = computer.run(data)
print(data)

data = [1002,4,3,4,33]
data = computer.run(data)
print(data)

data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
data = computer.run(data)
print(data)
