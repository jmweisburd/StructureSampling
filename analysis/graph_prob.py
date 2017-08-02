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
for t in [0.1,0.25,0.5]:
    xs = []
    probs = []
    for yd in yds :
        print("GRAPHING DISTANCE " + str(yd) + " NEAREST N "+ str(t))
        xs.append(yd)
        long_path  = base + "/data/" + str(yd) + "/long.txt"
        short_path = base + "/data/" + str(yd) + "/short.txt"
        pc = ProbabilityCalculator(t)
        #pc.read_files_to_maps(long_path, short_path)
        probs.append(pc.calculate_threshold_probability())
        probs.append(pc.calculate_bin_probability())
    title = str(t) + "thresh_prob_graph.png"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.set_title('Distance vs. Prob with Bins of ' + str(t) + 'nm')
    ax.set_title('Distance vs. Prob of Two Points Within ' + str(t) + ' of Each Other')
    ax.plot(xs,probs,'o-')
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    ax.set_ylabel("Probability")
    ax.set_xlabel("Distance between tow tethers (nm)")
    plt.savefig(title)

end = time.time()
print("")
print("PROCESS TOOK: " + str(end-start))
