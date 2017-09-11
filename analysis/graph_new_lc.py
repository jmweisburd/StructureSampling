import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time
from random import shuffle

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
y_ds = [10.88]
bins = [0.5]
#distr = ['uni_uni', 'worm_uni']
distr = ['uni_uni']

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
zip_list = None

for d in distr:
    print(d)
    for y in y_ds:
        print(str(y))
        for b in bins:
            long_path = base + "/data/" + d + "/" + str(y) + "/long.txt"
            short_path = base + "/data/" + d + "/" + str(y) + "/short.txt"
            pc = ProbabilityCalculator()
            pc.set_bw(b)
            pc.read_files_to_maps(long_path, short_path)

            zip_list = pc.plot_lc()
            shuffle(zip_list)

xs = list(map(lambda d: d[0].y, zip_list))
ys = list(map(lambda d: d[0].z, zip_list))
c_map = list(map(lambda d: d[1], zip_list))

plt.scatter(xs,ys,c=c_map, alpha=0.3)
plt.colorbar()
plt.xlabel("Y Axis (nm)")
plt.ylabel("Z Axis (nm)")
plt.title("y,z position vs local concentrations")
plt.savefig("uu_colormap.png")
