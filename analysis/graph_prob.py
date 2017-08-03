import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import time

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
yds = np.arange(0,35,5.44)
start = time.time()
y_ds = [5.44,10.88,12.0,13.5,21.76]
for t in [0.1,0.25,0.5]:
    print(t)
    bin_probs = []
    thresh_probs = []
    for y_d in y_ds:
        print(y_d)
        long_path = base + "/data/" + str(y_d) + "/long.txt"
        short_path = base + "/data/" + str(y_d) + "/short.txt"
        pc = ProbabilityCalculator(t)
        pc.read_files_to_maps(long_path, short_path)
        bin_probs.append(pc.calculate_bin_probability())
        thresh_probs.append(pc.calculate_threshold_probability())
    title = "bin_v_thresh_" + str(t)+"nm.png"
    fig = plt.figure()
    ax =  fig.add_subplot(111)
    bins = ax.plot(y_ds, bin_probs, 'ro-', label ='bin')
    thresh = ax.plot(y_ds, thresh_probs, 'bo-', label='threshold')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    ax.set_ylabel("Probability")
    ax.set_xlabel("Distance between toeholds (nm)")
    ax.set_title('Distance vs. Probability. ' + str(t) + ' nm bins/threshold')
    plt.savefig(title)

end = time.time()
print("")
print("PROCESS TOOK: " + str(end-start))
