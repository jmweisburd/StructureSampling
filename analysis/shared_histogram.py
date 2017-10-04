import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from utility import *
from coords import *

def fill_maps(p1, b):
    complex_map = {}
    simple_map = {}
    same_map = {}
    with open(p1, "r") as f:
        for line in f:
            x,y,z = parse_line(line)
            exact_coord = CC(x,y,z)
            x_round, y_round, z_round = myround(x,2,b), myround(y,2,b), myround(z,2,b)
            round_coord = CC(x_round, y_round, z_round)
            if round_coord not in complex_map.keys():
                complex_map[round_coord] = [exact_coord]
            else:
                complex_map[round_coord].append(exact_coord)
    f.close()
    #with open(p2, "r") as f:
        #for line in f:
            #x,y,z = parse_line(line)
            #exact_coord = CC(x,y,z)
            #x_round, y_round, z_round = myround(x,2,b), myround(y,2,b), myround(z,2,b)
            #round_coord = CC(x_round, y_round, z_round)
            #if round_coord not in simple_map.keys():
                #simple_map[round_coord] = [exact_coord]
            #else:
                #simple_map[round_coord].append(exact_coord)
    #f.close()
    ys = []
    zs = []
    for key in complex_map.keys():
        l = complex_map[key]
        for v in l:
            ys.append(v.y)
            zs.append(v.z)
    return ys, zs

def calculate_y_bins(b):
    if b == 0.1:
        return np.arange(10.05,34.05,0.1)
    elif b == 0.25:
        return np.arange(10.125,34.125,0.25)
    else:
        #return np.arange(-3.25,34.25, 0.5)
        return np.arange(5.25,15.25,0.5)

def calculate_z_bins(b):
    if b == 0.1:
        return np.arange(-0.05,10.05,0.1)
    elif b == 0.25:
        return np.arange(-0.125, 10.125, 0.25)
    else:
        return np.arange(-0.25,6.25,0.5)

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
#distr = ['uni_uni', 'uni_nicked', 'worm_uni', 'worm_nicked']
distr = ['uni_uni', 'worm_uni']
for b in [0.5]:
    for d in distr:
        long_path = base + "/data/" + d + "/10.88" + "/short.txt"
        #short_path = base + "/data/" + str(yd) + "/short.txt"
        ys, zs = fill_maps(long_path, b)
        ybins, zbins = calculate_y_bins(b), calculate_z_bins(b)
        fig, ax = plt.subplots(tight_layout=True)
        hist = ax.hist2d(ys, zs, [ybins, zbins])
        #ax.set_title(str(yd) + ' distance apart ' + str(b) + 'bins')
        ax.set_ylabel('z (nm)')
        ax.set_xlabel('y (nm)')
        #colorbar(hist[3])
        plt.colorbar(hist[3])
        plt.savefig(str(d) + "_hist" + ".png")
        plt.close()
