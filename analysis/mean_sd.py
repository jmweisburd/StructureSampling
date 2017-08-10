import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time
from coords import CC
from utility import *

def cart_coord_from_line(l):
    x,y,z = parse_line(line)
    return CC(x,y,z)

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
start = time.time()
y_ds = [5.44,10.88,12.0,13.5,21.76]
types = ['uni','wc']
long_uni = []
short_uni = []
long_wc = []
short_wc = []
for t in types:
    for y in y_ds:
        long_path = base + "/data/" + t + "/" + str(y) + "/long.txt"
        short_path = base + "/data/" + t + "/" + str(y) + "/short.txt"
        long_location = CC(0,0,0)
        short_location = CC(0,y,0)
        with open(long_path, "r") as f:
            for line in f:
                cc = cart_coord_from_line(line)
                distance = cc.distance(long_location)
                if t == 'uni':
                    long_uni.append(distance)
                else:
                    long_wc.append(distance)
        f.close()
        with open(short_path, "r") as f:
            for line in f:
                cc = cart_coord_from_line(line)
                distance = cc.distance(short_location)
                if t == 'uni':
                    short_uni.append(distance)
                else:
                    short_wc.append(distance)
        f.close()

long_uni_mean, long_uni_sd = np.mean(long_uni), np.std(long_uni)
long_wc_mean, long_wc_sd = np.mean(long_wc), np.std(long_wc)
short_uni_mean, short_uni_sd = np.mean(short_uni), np.std(short_uni)
short_wc_mean, short_wc_sd = np.mean(short_wc), np.std(short_wc)

print("### MEANS LONG ###")
print("Uniform: " + str(long_uni_mean))
print("Worm: "+ str(long_wc_mean))
print()
print("### MEANS SHORT ###")
print("Uniform: " + str(short_uni_mean))
print("Worm: " + str(short_wc_mean))
print()
print("### SD LONG ###")
print("Uniform: " + str(long_uni_sd))
print("Worm: "+ str(long_wc_sd))
print()
print("### SD SHORT ###")
print("Uniform: " + str(short_uni_sd))
print("Worm: " + str(short_wc_sd))

save_as = "mean_sd.png"
fig = plt.figure()
ax =  fig.add_subplot(111)
fig.suptitle("Mean Length of Long/Short DNA Structures with Standard Deviation")
ys = np.array([long_uni_mean, long_wc_mean, short_uni_mean, short_wc_mean])
xs = np.array([1,2,3,4])
e = np.array([long_uni_sd, long_wc_sd, short_uni_sd, short_worm_sd])
my_xticks = np.array(['Long Uniform', 'Long Worm', 'Short Uniform', 'Short Worm'])
plt.ylabel('Mean Strucutre Length (nm)')
plt.xticks(xs, my_xticks)
ax.set_xlim(0.5,4.5)
plt.errorbar(xs,ys, e, linestyle='None', marker='^')
fig.savefig(save_as)

end = time.time()

print("PROCESS TOOK: " + str(end-start))
