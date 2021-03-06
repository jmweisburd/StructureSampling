import os
import math
from data_analyst import DataAnalyst

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
#y_ds = [5.44,10.88,12.0,13.5,21.76]
y_ds = [10.88]
bins = [0.5,1.0,1.5,2.0]
dist = ['uni_uni', 'worm_uni']

#dist = 'uni_uni'
#dist = 'uni_nicked'
#dist = 'worm_uni'
#dist = 'worm_nicked'

for d in dist:
    with open(d+'.txt', 'w') as f:
        f.write("### " + dist + " ###\n")
        f.write("\n")
        for y in y_ds:
            f.write("### TOEHOLD DISTANCE " + str(y) + " nm ###\n")
            f.write("\n")

            long_path = base + "/data/" + dist + "/" + str(y) + "/long.txt"
            short_path = base + "/data/" + dist + "/" + str(y) + "/short.txt"

            for b in bins:
                print("DISTRIBUTION " + str(dist))
                print("DISTANCE" + str(y))
                print("BIN SIZE " + str(b))
                reactive_vol = (4/3) * math.pi * pow(b, 3)
                da = DataAnalyst()
                da.set_bw(b)
                da.read_files_to_maps(long_path, short_path)

                f.write("### BIN/THRESHOLD VALUE: " + str(b) + " nm ###\n")
                f.write("\n")

                lc = da.local_conc()
                f.write("VOL: " + str(reactive_vol) + "\n")
                f.write("LC: " + str(lc) + "\n")
                f.write("\n")

f.close()
