import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

f = open("resources/day10_input.txt", "r")
lines = f.read().splitlines()
f.close()
data = set()
WIDTH = len(lines[0])
HEIGHT = len(lines)
y = 0
for l in lines:
    x = 0
    for a in l:
        if lines[y][x] == '#':
            data.add((x, y))
        x += 1
    y += 1
vis_count = {}
for p in data:
    wdata = data.copy()
    wdata.remove(p)
    vis_count[p] = 0
    while len(wdata) > 0:
        c = wdata.pop()
        xc = c[0] - p[0]
        yc = c[1] - p[1]
        cand_set = wdata.copy()
        for t in cand_set:
            xt = t[0] - p[0]
            yt = t[1] - p[1]
            if (xc == 0 and xt == 0 and yc*yt > 0) or (yc == 0 and yt == 0 and xc*xt > 0) or (xc != 0 and yc != 0 and p[1] + yc * xt / xc == t[1] and xc*xt > 0):
                wdata.remove(t)
        vis_count[p] += 1
position = sorted(vis_count.items(), reverse = True, key = lambda item: item[1])[0][0]
print("Best position for monitoring station:", position)
angles = {}
data.remove(position)
for a in data:
    #a = (position[0], position[1] - 5)
    x = a[0] - position[0]
    y = a[1] - position[1]
    dist, angle = cart2pol(x,y)
    angle += np.pi/2
    if angle < 0:
        angle += np.pi*2
    if angle in angles:
        angles[angle].append((a, dist))
    else:
        angles[angle] = [(a, dist)]
    #break
#print(angles)
fin_angles = {}
for ang in angles:
    lang = sorted(angles[ang], key = lambda x: x[1])
    for i in range(len(lang)):
        new_angle = ang + np.pi*2*i
        if new_angle in fin_angles:
            print("Uh-oh, angle already in fin_angles: ", new_angle)
            exit(-1)
        fin_angles[new_angle] = lang[i]
#print(fin_angles)
order_of_destruction = [v for k, v in sorted(fin_angles.items(), key = lambda x: x[0])]
#print('-------')
code = order_of_destruction[199][0][0]*100 + order_of_destruction[199][0][1]
print('Code of 200th asteroid: ', code)