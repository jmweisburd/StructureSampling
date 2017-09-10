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

#dist = ['uni_uni', 'uni_nicked', 'worm_uni', 'worm_nicked']
#dist = ['uni_uni', 'uni_nicked']
dist = ['worm_uni', 'worm_nicked']
#dist = ['wc']

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
worm_uni = []
worm_nicked = []
for d in dist:
    long_path = base + "/data/" + d + "/10.88" + "/long.txt"
    short_path = base + "/data/" + d + "/10.88" + "/short.txt"
    pc = ProbabilityCalculator()
    pc.set_bw(0.5)
    pc.read_files_to_maps(long_path, short_path)
    mins, maxs = pc.area_slice_long()
    maxs = list(reversed(maxs))
    mins.extend(maxs)
    mins.append(mins[0])
    if d == 'worm_nicked':
        worm_nicked = mins
    else:
        worm_uni = mins

nicked_points_x = list(map(lambda k: k.y, worm_nicked))
nicked_points_y = list(map(lambda k: k.z, worm_nicked))
uni_points_x = list(map(lambda k: k.y, worm_uni))
uni_points_y = list(map(lambda k: k.z, worm_uni))

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.scatter(nicked_points_x, nicked_points_y, c = 'r')
worm_vol = ax.plot(nicked_points_x, nicked_points_y, 'r', label = 'woorm, nicked')
ax.scatter(uni_points_x, uni_points_y, c = 'b')
uni_vol = ax.plot(uni_points_x, uni_points_y, 'b', label = 'worm, uni')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("z position (nm)")
ax.set_xlabel("y position (nm)")
plt.savefig("slice_long_nicked.png")
