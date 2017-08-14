import os
from utility import inter_vol
from coords import *
from probability_calc import ProbabilityCalculator

#dist = ['uni', 'worm']
dist = ['worm']

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
for d in dist:
    long_path = base + "/data/" + d + "/10.88" + "/long.txt"
    short_path = base + "/data/" + d + "/10.88" + "/short.txt"
    pc = ProbabilityCalculator()
    pc.set_bw(0.5)
    pc.read_files_to_maps(long_path, short_path)
    mins, maxs = pc.area_slice()
    print("MINS")
    for m in mins:
        print(m)
    print("MAXS")
    for m in maxs:
        print(m)
