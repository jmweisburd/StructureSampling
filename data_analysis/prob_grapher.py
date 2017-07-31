import os
from probability_calc import ProbabilityCalculator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
#for b in [0.1, 0.25, 0.5]:
    #xs = []
    #probs = []
    #for yd in range(0,35,5):
        #xs.append(yd)
        #long_path = base + "/data/" + str(yd) + "/long.txt"
        #short_path = base + "/data/" + str(yd) + "/short.txt"
        #pc = ProbabilityCalculator(b)
        #pc.fill_in_maps(long_path, short_path)
        #probs.append(pc.calculate_probability())
    #title = str(b)+"bins_prob_graph.png"
    #fig =plt.figure()
    #ax = fig.add_subplot(111)
    #ax.set_title('Distance vs. Shared Locality Probability (' + str(b)+ ' nm bins)')
    #ax.plot(xs,probs, 'o-')
    #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    #ax.set_ylabel("Probability")
    #ax.set_xlabel("Distance between two tethers")
    #plt.savefig(title)

for d in [0.1,0.25,0.5]:
    xs = []
    probs = []
    for yd in range(0,35,5):
        print("GRAPHING DISTANCE " + str(yd) + " NEAREST N "+ str(d))
        xs.append(yd)
        long_path  = base + "/data/" + str(yd) + "/long.txt"
        short_path = base + "/data/" + str(yd) + "/short.txt"
        pc = ProbabilityCalculator(d)
        pc.read_files_into_CC(long_path, short_path)
        probs.append(pc.calculate_distance_probability())
    title = str(d) + "nearest_prob_graph.png"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Distance vs. Prob of Two Points Within ' + str(d) + ' of Each Other')
    ax.plot(xs,probs,'o-')
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    ax.set_ylabel("Probability")
    ax.set_xlabel("Distance between tow tethers (nm)")
    plt.savefig(title)
