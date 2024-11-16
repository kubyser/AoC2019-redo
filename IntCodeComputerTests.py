from IntCode import IntCode

data = [1,9,10,3,2,3,11,0,99,30,40,50]
computer = IntCode()
#data = computer.run(data)
#print(data)

data = [1002,4,3,4,33]
#data = computer.run(data)
#print(data)

data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#data = computer.run(data)
#print(data)

in_data = [7,87]
out_data = []
data = [3,50,4,50,3,50,4,50,99] + [0]*50
#data = computer.run(data, in_data, out_data)
#print(data, out_data)

data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
init_values = [4,3,2,1,0]
res_stream = []
#computer.run_chain(5, init_values, data, [0], res_stream)
#print(init_values, res_stream)


data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
        27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
init_values = [9,8,7,6,5]
res_stream = []
computer.run_chain(5, init_values, data, [0], res_stream)
print(res_stream)

exit()

data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
init_values = [5,4,3,2,1]
res_stream = []
computer.run_chain(5, init_values, data, [0], res_stream)
print(init_values, res_stream)

data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
        101,5,23,23,1,24,23,23,4,23,99,0,0]
init_values = [0,1,2,3,4]
res_stream = []
computer.run_chain(5, init_values, data, [0], res_stream)
print(res_stream)

data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
        1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
init_values = [1,0,4,3,2]
res_stream = []
computer.run_chain(5, init_values, data, [0], res_stream)
print(res_stream)
