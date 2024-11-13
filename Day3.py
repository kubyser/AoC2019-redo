PART2= True
f = open("resources/day3_input.txt", "r")
lines = f.read().splitlines()
f.close()
wire1 = []
pos = (0, 0)
distance = 0
path1 = lines[0].split(',')
for seg in path1:
    direction = seg[0]
    length = int(seg[1:])
    if direction == 'U':
        endPos = (pos[0], pos[1]+length)
    elif direction == 'D':
        endPos = (pos[0], pos[1]-length)
    elif direction == 'L':
        endPos = (pos[0]-length, pos[1])
    elif direction == 'R':
        endPos = (pos[0]+length, pos[1])
    else:
        print("error")
        exit(-1)
    wire1.append((direction, pos, endPos, distance))
    pos = endPos
    distance += length
pos = (0, 0)
distance = 0
path2 = lines[1].split(',')
intersections = {}
for seg in path2:
    direction = seg[0]
    length = int(seg[1:])
    if direction == 'U':
        endPos = (pos[0], pos[1]+length)
    elif direction == 'D':
        endPos = (pos[0], pos[1]-length)
    elif direction == 'L':
        endPos = (pos[0]-length, pos[1])
    elif direction == 'R':
        endPos = (pos[0]+length, pos[1])
    else:
        print("error")
        exit(-1)
    for seg1 in wire1:
        if direction in ('U', 'D'):
            if (seg1[0] in ('R', 'L') and min(pos[1], endPos[1]) <= seg1[1][1] <= max(pos[1], endPos[1]) and
                    min(seg1[1][0], seg1[2][0]) <= pos[0] <= max(seg1[1][0], seg1[2][0])):
                newInt = (pos[0], seg1[1][1])
                wire1Dist = seg1[3] + ((newInt[0] - seg1[1][0]) if seg1[0] == 'R' else (seg1[1][0] - newInt[0]))
                wire2Dist = distance + ((newInt[1] - pos[1]) if direction == 'U' else (pos[1] - newInt[1]))
                if newInt not in intersections or intersections[newInt] > wire1Dist+wire2Dist:
                    intersections[newInt] = wire1Dist+wire2Dist
        else:
            if (seg1[0] in ('U', 'D') and min(pos[0], endPos[0]) <= seg1[1][0] <= max(pos[0], endPos[0]) and
                    min(seg1[1][1], seg1[2][1]) <= pos[1] <= max(seg1[1][1], seg1[2][1])):
                newInt = (seg1[1][0], pos[1])
                wire1Dist = seg1[3] + ((newInt[1] - seg1[1][1]) if seg1[0] == 'U' else (seg1[1][1] - newInt[1]))
                wire2Dist = distance + ((newInt[0] - pos[0]) if direction == 'R' else (pos[0] - newInt[0]))
                if newInt not in intersections or intersections[newInt] > wire1Dist+wire2Dist:
                    intersections[newInt] = wire1Dist+wire2Dist
    pos = endPos
    distance += length
print(intersections)
minDist = None
for cross in intersections:
    if cross == (0, 0):
        continue
    dist = abs(cross[0]) + abs(cross[1]) if not PART2 else intersections[cross]
    if minDist is None or dist < minDist:
        minDist = dist
print("Minimum distance: ", minDist)


