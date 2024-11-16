from IntCode import IntCode

PART2 = True

f = open("resources/day7_input.txt", "r")
data = [int(x) for x in f.read().split(',')]
f.close()
computer = IntCode()

#data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,        27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

if PART2:
    init_choices = (5, 6, 7, 8, 9)
else:
    init_choices = (0, 1, 2, 3, 4)

def build_combs(sequence):
    if len(sequence) == 5:
        return [sequence]
    new_seq = []
    for x in init_choices:
        if x not in sequence:
            new_seq += build_combs(sequence + [x])
    return new_seq

combs = build_combs([])
#print(combs)
max_thrust = 0
for c in combs:
    res_stream = []
    computer.run_chain(5, c, data, [0], res_stream)
    if res_stream[0] > max_thrust:
        max_thrust = res_stream[0]

print("Max thrusters signal: ", max_thrust)