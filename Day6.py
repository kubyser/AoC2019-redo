f = open("resources/day6_input.txt", "r")
lines = f.read().splitlines()
f.close()
data = {}
for l in lines:
    c = l.split(')')[0]
    p = l.split(')')[1]
    if c not in data:
        data[c] = [[p], None]
    else:
        data[c][0].append(p)
    if p not in data:
        data[p] = [[], c]
    else:
        data[p][1] = c
dist = {}
curDist = 0
queue = ['COM']
while len(queue) > 0:
    newQueue = []
    while len(queue) > 0:
        x = queue.pop()
        dist[x] = curDist
        newQueue += data[x][0]
    curDist += 1
    queue = newQueue
sumOrbits = sum([x for x in dist.values()])
print('Sum of orbits: ', sumOrbits)
y = data['YOU'][1]
s = data['SAN'][1]
yTree = [y]
p = y
while data[p][1] is not None:
    p = data[p][1]
    yTree = [p] + yTree
sTree = [s]
p = s
while data[p][1] is not None:
    p = data[p][1]
    sTree = [p] + sTree
p = 0
while yTree[p+1] == sTree[p+1]:
    p += 1
jumpDist = dist[y] - dist[yTree[p]] + dist[s] - dist[yTree[p]]
print('NUmber of jumps: ', jumpDist)


