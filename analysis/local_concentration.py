import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
start = time.time()
#y_ds = [5.44,10.88,12.0,13.5,21.76]
y_d = 10.88
ts = [0.1,0.25,0.5]
bin_local = []
thresh_local = []
for t in ts:
    print(t)
    long_path = base + "/data/1mil/" + str(y_d) + "/long.txt"
    short_path = base + "/data/1mil/" + str(y_d) + "/short.txt"
    pc = ProbabilityCalculator(t)
    pc.read_files_to_maps(long_path, short_path)
    
    bprob = pc.calculate_bin_probability()
    print("NUMBER OF BIN BINS: " + str(pc.num_colocating_bins)
    lc = pc.calculate_colocating_volume()*1660577881
    bin_local.append(lc)
    print("BIN " + str(t) + " LC: " + str(lc))

    tprob = pc.calculate_threshold_probability()
    print("NUMBER OF THRESH BINS: " + str(pc.num_colocating_bins)
    lc = pc.calculate_colocating_volume()*1660577881
    thresh_local.append(lc)
    print("THRESH " + str(t) + " LC: " + str(lc))

title = "lc_v_binthreshsize.png"
fig = plt.figure()
ax =  fig.add_subplot(111)
bins = ax.plot(ts, bin_local, 'ro-', label ='bin')
thresh = ax.plot(ts, thresh_local, 'bo-', label='threshold')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_ylabel("Local Concentration")
ax.set_xlabel("Bin/Threshold Size")
ax.set_title('Local Concentration of Hairpins 10.88nm Apart')
plt.savefig(title)

end = time.time()
print("")
print("PROCESS TOOK: " + str(end-start))
