import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
y_ds = [10.88]
bins = [0.5]
distr = ['wc']

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

xs = list(map(lambda d: d[0].y, zip_list))
ys = list(map(lambda d: d[0].z, zip_list))
c_map = list(map(lambda d: d[1], zip_list))

plt.scatter(xs,ys,c=c_map)
plt.savefig("colormap_scatter_test.png")
