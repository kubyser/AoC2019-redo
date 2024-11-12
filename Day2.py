PART2 = True
TARGET = 19690720
f = open("resources/day2_input.txt", "r")
lines = f.read().split(',')
f.close()
data = {}

def init_data():
    global data
    data = {}
    pos = 0
    for l in lines:
        data[pos] = int(l)
        pos += 1

if not PART2:
    combs = [(12,2)]
else:
    combs = [(x, y) for x in range(100) for y in range(100)]
resComb = None
for comb in combs:
    init_data()
    data[1] = comb[0]
    data[2] = comb[1]
    pos = 0
    while True:
        op = data[pos]
        if op == 99:
            break
        arg1 = data[pos+1]
        arg2 = data[pos+2]
        arg3 = data[pos+3]
        if op == 1:
            res = data[arg1] + data[arg2]
        elif op == 2:
            res = data[arg1] * data[arg2]
        else:
            print("Error at pos ", pos, " op = ", op)
            exit(-1)
        data[arg3] = res
        pos += 4
    if not PART2 or data[0] == TARGET:
        resComb = comb
        break
res = data[0]
combRes = 100 * resComb[0] + resComb[1]
print("Program finished. result: ", res, "combRes: ", combRes)


