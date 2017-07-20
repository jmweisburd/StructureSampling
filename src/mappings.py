from coords import *

def myround(x, prec=2, base=0.5):
    return round(base * round(float(x)/base),prec)

def parse_line(s):
    split_array = s.split(",")
    x, y, z = split_array[0], split_array[1], split_array[2]
    return float(x), float(y), float(z)

longs = []
shorts = []

with open("long.txt", "r") as f:
    for line in f:
        x,y,z = parse_line(line)
        longs.append(CartesianCoords(x,y,z))
f.close()

with open("short.txt", "r") as f:
    for line in f:
        x,y,z = parse_line(line)
        shorts.append(CartesianCoords(x,y,z))
f.close()

l_map = {}
for l in longs:
    x_round = myround(l.x)
    y_round = myround(l.y)
    z_round = myround(l.z)
    round_coord = CartesianCoords(x_round, y_round, z_round)
    if round_coord not in l_map.keys():
        l_map[round_coord] = 1
    else:
        l_map[round_coord] += 1

s_map = {}
for s in shorts:
    x_round = myround(s.x)
    y_round = myround(s.y)
    z_round = myround(s.z)
    round_coord = CartesianCoords(x_round, y_round, z_round)
    if round_coord not in s_map.keys():
        s_map[round_coord] = 1
    else:
        s_map[round_coord] += 1

t_map = {}
for key, value in l_map.items():
    if key in s_map:
        if key not in t_map.keys():
            t_map[key] = 1
        else:
            t_map[key] += 1

for key, value in t_map.items():
    print(str(key) + ": " + str(value))
