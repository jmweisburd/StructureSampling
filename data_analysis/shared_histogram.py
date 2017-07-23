import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def myround(x, prec=2, base=0.5):
    return round(base * round(float(x)/base),prec)

class CartesianCoords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return(str(self.x) + "," + str(self.y) + "," + str(self.z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        x_bool = (self.x == other.x)
        y_bool = (self.y == other.y)
        z_bool = (self.z == other.z)
        return (x_bool and y_bool and z_bool)

def parse_line(s):
    split_array = s.split(",")
    x, y, z = split_array[0], split_array[1], split_array[2]
    return float(x), float(y), float(z)

complex_map = {}
simple_map = {}
same_map = {}

with open("long.txt", "r") as f:
    for line in f:
        x,y,z = parse_line(line)
        exact_coord = CartesianCoords(x,y,z)
        x_round, y_round, z_round = myround(x), myround(y), myround(z)
        round_coord = CartesianCoords(x_round, y_round, z_round)
        if round_coord not in complex_map.keys():
            complex_map[round_coord] = [exact_coord]
        else:
            complex_map[round_coord].append(exact_coord)
f.close()

with open("short.txt", "r") as f:
    for line in f:
        x,y,z = parse_line(line)
        exact_coord = CartesianCoords(x,y,z)
        x_round, y_round, z_round = myround(x), myround(y), myround(z)
        round_coord = CartesianCoords(x_round, y_round, z_round)
        if round_coord not in simple_map.keys():
            simple_map[round_coord] = [exact_coord]
        else:
            simple_map[round_coord].append(exact_coord)
f.close()

ys = []
zs = []

for key in complex_map.keys():
    if key in simple_map.keys():
        l = complex_map[key]
        s = simple_map[key]
        for v in l:
            ys.append(v.y)
            zs.append(v.z)
        for v in s:
            ys.append(v.y)
            zs.append(v.z)

#for key in complex_map.keys():
    #if key in simple_map.keys():
        #same_map[key] = complex_map[key].extend(simple_map[key])

#yz = []
#zs = []

#for key, value in same_map.items():
    #print(key)
    #for v in value:
        #print(v)
    #yz.append(value.y)
    #zs.append(value.z)

heatmap, xedges, yedges = np.histogram2d(ys, zs, bins=(16,16))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(heatmap, extent=extent)
plt.colorbar()
plt.ylabel('z (nm)')
plt.xlabel('y (nm)')
plt.savefig("heatmap.png")
