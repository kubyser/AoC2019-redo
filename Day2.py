from IntCode import IntCode

PART2 = False
TARGET = 19690720
f = open("resources/day2_input.txt", "r")
lines = [int(x) for x in f.read().split(',')]
f.close()
data = {}

def init_data():
    global data
    data = lines.copy()

if not PART2:
    combs = [(12,2)]
else:
    combs = [(x, y) for x in range(100) for y in range(100)]
resComb = None
computer = IntCode()
for comb in combs:
    init_data()
    data[1] = comb[0]
    data[2] = comb[1]
    data = computer.run(data)
    if not PART2 or data[0] == TARGET:
        resComb = comb
        break
res = data[0]
combRes = 100 * resComb[0] + resComb[1]
print("Program finished. result: ", res, "combRes: ", combRes)


