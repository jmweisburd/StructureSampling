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
dist = ['uni_uni', 'uni_nicked']
#dist = ['wc']

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
uni_uni = []
uni_nicked = []
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
    if d == 'uni_nicked':
        uni_nicked = mins
    else:
        uni_uni = mins

nicked_points_x = list(map(lambda k: k.y, uni_nicked))
nicked_points_y = list(map(lambda k: k.z, uni_nicked))
uni_points_x = list(map(lambda k: k.y, uni_uni))
uni_points_y = list(map(lambda k: k.z, uni_uni))

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.scatter(nicked_points_x, nicked_points_y, c = 'r')
worm_vol = ax.plot(nicked_points_x, nicked_points_y, 'r', label = 'uni, nicked')
ax.scatter(uni_points_x, uni_points_y, c = 'b')
uni_vol = ax.plot(uni_points_x, uni_points_y, 'b', label = 'uni, uni')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("z position (nm)")
ax.set_xlabel("y position (nm)")
plt.savefig("slice_long_nicked.png")
