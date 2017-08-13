import os
from probability_calc import ProbabilityCalculator, total_area
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time
from utility import total_area

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
#y_ds = [5.44,10.88,12.0,13.5,21.76]
y_ds = [10.88]
bins = [0.25,0.5,0.75,1.0,1.25]
distr = ['uni', 'wc']

LONG_MAX = 17.68
SHORT_MAX = 5.44

L_S_DIFF = LONG_MAX - SHORT_MAX
L_S_SUM = LONG_MAX + SHORT_MAX

with open('out_vol_lc.txt', 'w') as f:
    for d in distr:
        f.write("### " + d + " ###\n")
        f.write("\n")
        for y in y_ds:
            f.write("### TOEHOLD DISTANCE " + str(y) + " nm ###\n")
            f.write("\n")
            if y <= L_S_DIFF:
                sphere_vol = inter_vol(L_S_DIFF, LONG_MAX, SHORT_MAX)
            elif y >= L_S_SUM:
                sphere_vol = 0
            else:
                sphere_vol = inter_vol(y, LONG_MAX, SHORT_MAX)

            f.write("OVERLAPPING SPHERE VOLUME: " + str(sphere_vol) + "\n")
            f.write("\n")

            long_path = base + "/data/" + d + "/" + str(y) + "/long.txt"
            short_path = base + "/data/" + d + "/" + str(y) + "/short.txt"

            for b in bins:
                print("DISTRIBUTION " + str(d))
                print("DISTANCE" + str(y))
                print("BIN SIZE " + str(b))
                pc = ProbabilityCalculator()
                pc.set_bw(b)
                pc.read_files_to_maps(long_path, short_path)

                f.write("### BIN/THRESHOLD VALUE: " + str(b) + " nm ###\n")
                f.write("\n")

                bprob = pc.calculate_bin_probability()
                f.write("BINS PROBABILITY: " + str(bprob) + "\n")
                bvol = pc.calculate_colocating_volume()
                if bvol != 0:
                    f.write("ADD BINS VOLUME: " + str(bvol) + "\n")
                    b_add_lc = (bprob/bvol) * 1660577881
                    f.write("BINS LC W/ ADD BINS VOL: " + str(b_add_lc) + "\n")
                else:
                    f.write("BINS VOLUME: 0\n")
                    f.write("BINS LC W/ BINS: 0\n")
                if sphere_vol != 0:
                    b_hemi_lc = (bprob/sphere_vol) * 1660577881
                    f.write("BINS LC W/ SPHERE VOL: " + str(b_hemi_lc) + "\n")
                else:
                    f.write("BINS LC W/ SPHERE VOL: 0\n")
                f.write("\n")

                tprob = pc.calculate_threshold_probability()
                f.write("THRESH PROBABILITY: " + str(tprob) + "\n")
                tvol = pc.calculate_colocating_volume()
                if tvol != 0:
                    f.write("ADD THRESH VOLUME: " + str(tvol) + "\n")
                    t_add_lc = (tprob/tvol) * 1660577881
                    f.write("THRESH LC W/ ADD THRESH VOL: " + str(t_add_lc) + "\n")
                else:
                    f.write("THRESH VOLUME: 0\n")
                    f.write("BINS LC W/ ADD THRESH VOL: 0\n")
                if sphere_vol != 0:
                    t_hemi_lc = (tprob/sphere_vol) * 1660577881
                    f.write("THRESH LC W/ SPHERE VOL: " + str(t_hemi_lc) + "\n")
                else:
                    f.write("THRESH LC W/ SPHERE VOL: 0\n")
                f.write("\n")

f.close()
