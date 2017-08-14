import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from utility import inter_vol
from coords import *
from probability_calc import ProbabilityCalculator

#dist = ['uni', 'worm']
dist = ['wc']

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
worm_points = []
uni_points = []
for d in dist:
    long_path = base + "/data/" + d + "/10.88" + "/long.txt"
    short_path = base + "/data/" + d + "/10.88" + "/short.txt"
    pc = ProbabilityCalculator()
    pc.set_bw(0.5)
    pc.read_files_to_maps(long_path, short_path)
    mins, maxs = pc.area_slice()
    maxs = list(reversed(maxs))
    mins.extend(maxs)
    mins.append(mins[0])
    if d == 'wc':
        worm_points = mins
    else:
        uni_points = mins

worm_points_x = list(map(lambda k: k.y, worm_points))
worm_points_y = list(map(lambda k: k.z, worm_points))
uni_points_x = list(map(lambda k: k.y, uni_points))
uni_points_y = list(map(lambda k: k.z, uni_points))

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.scatter(worm_points_x, worm_points_y, c = 'r')
worm_vol = ax.plot(worm_points_x, worm_points_y, 'r', label = 'worm-chain')
ax.scatter(uni_points_x, uni_points_y, c = 'b')
uni_vol = ax.plot(uni_points_x, uni_points_y, 'r', label = 'ideal-chain')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("z position (nm)")
ax.set_xlabel("y position (nm)")
plt.savefig("area_slice.png")
