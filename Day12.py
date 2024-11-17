import numpy

f = open("resources/day12_input.txt", "r")
lines = f.read().splitlines()
f.close()
data = []
init_state = []
for line in lines:
    line = line.replace("<", "").replace(">", "").replace("x=", "").replace("y=", "").replace("z=", "").split(',')
    pos = [int(line[0]), int(line[1]), int(line[2])]
    data.append([pos, [0, 0, 0]])
    init_state.append([pos.copy(), [0, 0, 0]])
print(data)
num_moons = len(data)
NUM_STEPS = 1000
steps = 0
rep_steps = [0]*3
#for step in range(NUM_STEPS):
while True:
#    gravity = [[0, 0, 0]]*num_moons
    for a in range(num_moons-1):
        for b in range(a+1, num_moons):
            for c in range(3):
                mod = 1 if data[a][0][c] < data[b][0][c] else -1 if data[a][0][c] > data[b][0][c] else 0
                data[a][1][c] += mod
                data[b][1][c] -= mod
    for i in range(num_moons):
        for c in range(3):
            data[i][0][c] += data[i][1][c]
    steps += 1
#    if steps == 1386:
#        print("init=======", data)
#        print("data=======", data)
#        input(">>")
#    if all(x[1] == [0, 0, 0] for x in data):
#        print("Returned to stopped state! steps=", steps, ", interval: ", steps-rep_steps)
#        rep_steps = steps
    for c in range(3):
        all_equal = True
        for m in range(num_moons):
            if (data[m][0][c] != init_state[m][0][c]) or (data[m][1][c] != init_state[m][1][c]):
                all_equal = False
                break
        if all_equal:
#            if rep_steps[c] != steps-rep_steps[c]:
#                print("coordinate ", c, " returned! steps=", steps, ", interval: ", steps-rep_steps[c])
            rep_steps[c] = steps
            res = rep_steps[0]*rep_steps[1]*rep_steps[2]
            if res > 0:
                lcm = numpy.lcm.reduce(rep_steps)
                print("LCM: ", lcm)
                exit()

energy = 0
for i in range(num_moons):
    pot = 0
    kin = 0
    for c in range(3):
        pot += abs(data[i][0][c])
        kin += abs(data[i][1][c])
    energy += pot*kin
print("Total energy: ", energy)


