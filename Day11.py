from IntCode import IntCode

def printData(data):
    minX = min([x for x, y in data])
    maxX = max([x for x, y in data])
    minY = min([y for x, y in data])
    maxY = max([y for x, y in data])
    for y in range(maxY, minY-1, -1):
        s = ''
        for x in range(minX, maxX+1):
            if (x, y) in data:
                s += '#' if data[(x, y)] == 1 else ' '
            else:
                s += ' '
        print(s)

PART2 = True
TURNS = {(0, 1): ((-1, 0), (1, 0)),
         (1, 0): ((0, 1), (0, -1)),
         (0, -1): ((1, 0), (-1, 0)),
         (-1, 0): ((0, -1), (0, 1))}

f = open("resources/day11_input.txt", "r")
program = [int(x) for x in f.read().split(',')]
f.close()

data = {}
pos = (0, 0)
direction = (0, 1)
comp = IntCode()
stopped = False
input_stream = []
output_stream = []
if PART2:
    data[pos] = 1
while not stopped:
    if pos in data:
        input_stream.append(data[pos])
    else:
        input_stream.append(0)
    memory, pause_flag = comp.run(program, input_stream, output_stream, pause_on_input=True)
    color = output_stream.pop(0)
    data[pos] = color
    turn = output_stream.pop(0)
    direction = TURNS[direction][turn]
    pos = (pos[0]+direction[0], pos[1]+direction[1])
    if not pause_flag:
        stopped = True
res = len(data)
print("Number of painted tiles: ", res)
printData(data)