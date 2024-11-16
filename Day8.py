from collections import Counter

WIDTH = 25
HEIGHT = 6

def get_layer(data, l_num):
    return data[l_num*WIDTH*HEIGHT:(l_num+1)*WIDTH*HEIGHT]

f = open("resources/day8_input.txt", "r")
data = f.read()
f.close()

num_layers = int(len(data)/(WIDTH*HEIGHT))
min_zeroes = None
one_by_two = None
for x in range(num_layers):
    c = Counter(get_layer(data, x))
    if min_zeroes is None or c['0'] < min_zeroes:
        min_zeroes = c['0']
        one_by_two = c['1'] * c['2']
print("Ones by twos: ", one_by_two)

message = []
for y in range(HEIGHT):
    line = ''
    for x in range(WIDTH):
        for l in range(num_layers):
            item = get_layer(data, l)[y*WIDTH + x]
            if item in ('0', '1'):
                line += ' ' if item == '0' else '#'
                break
    message.append(line)
    print(line)




