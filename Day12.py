import itertools
from functools import reduce
from operator import mul

import numpy

f = open("resources/day12_input.txt", "r")
lines = f.read().splitlines()
f.close()
data = []
init_state = []
for line in lines:
    line = line.replace("<", "").replace(">", "").replace("x=", "").replace("y=", "").replace("z=", "").split(',')
    pos = [int(x) for x in line]
    data.append([pos, [0]*3])
    init_state.append([pos.copy(), [0]*3])
print(data)
num_moons = len(data)
NUM_STEPS = 1000
PART2 = False
steps = 0
rep_steps = [0]*3
#for step in range(NUM_STEPS):
while True:
    for a,b in [(data[i],data[j]) for i,j in itertools.combinations(range(num_moons), 2)]:
        mod = [1 if a[0][c] < b[0][c] else -1 if a[0][c] > b[0][c] else 0 for c in range(3)]
        a[1] = [x+y for x,y in zip(a[1], mod)]
        b[1] = [x-y for x,y in zip(b[1], mod)]
    for i in data:
        i[0] = [x+y for x,y in zip(i[0], i[1])]
    steps += 1
    if not PART2:
        if steps == NUM_STEPS:
            break
    else:
        for c in range(3):
            if all([(d[0][c] == i[0][c]) and (d[1][c] == i[1][c]) for d,i in zip(data, init_state)]):
                rep_steps[c] = steps
                if all([r != 0 for r in rep_steps]):
                    lcm = numpy.lcm.reduce(rep_steps)
                    print("LCM: ", lcm)
                    exit()

energy = sum([reduce(mul, [sum([abs(m[x][c]) for c in range(3)]) for x in [0,1]]) for m in data])
print("Total energy: ", energy)


