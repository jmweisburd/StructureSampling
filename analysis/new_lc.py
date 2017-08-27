import os
import math
from probability_calc import ProbabilityCalculator
from utility import total_area

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
#y_ds = [5.44,10.88,12.0,13.5,21.76]
y_ds = [10.88]
bins = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
distr = ['uni', 'wc']

with open('new_lc.txt', 'w') as f:
    for d in distr:
        f.write("### " + d + " ###\n")
        f.write("\n")
        for y in y_ds:
            f.write("### TOEHOLD DISTANCE " + str(y) + " nm ###\n")
            f.write("\n")

            long_path = base + "/data/" + d + "/" + str(y) + "/long.txt"
            short_path = base + "/data/" + d + "/" + str(y) + "/short.txt"

            for b in bins:
                print("DISTRIBUTION " + str(d))
                print("DISTANCE" + str(y))
                print("BIN SIZE " + str(b))
                reactive_vol = (4/3) * math.pi * pow(b, 3)
                pc = ProbabilityCalculator()
                pc.set_bw(b)
                pc.read_files_to_maps(long_path, short_path)

                f.write("### BIN/THRESHOLD VALUE: " + str(b) + " nm ###\n")
                f.write("\n")

                lc = pc.new_local_conc()
                f.write("VOL: " + str(reactive_vol) + "\n")
                f.write("LC: " + str(lc) + "\n")
                f.write("\n")

f.close()
