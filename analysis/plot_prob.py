import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
#for t in [0.1,0.25,0.5]:
    #xs = []
    #probs = []
    #for yd in yds :
        #print("GRAPHING DISTANCE " + str(yd) + " NEAREST N "+ str(t))
        #xs.append(yd)
        #long_path  = base + "/data/" + str(yd) + "/long.txt"
        #short_path = base + "/data/" + str(yd) + "/short.txt"
        #pc = ProbabilityCalculator(t)
        #pc.read_files_to_maps(long_path, short_path)
        #probs.append(pc.calculate_threshold_probability())
        #probs.append(pc.calculate_bin_probability())
    #title = str(t) + "thresh_prob_graph.png"
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    ##ax.set_title('Distance vs. Prob with Bins of ' + str(t) + 'nm')
    #ax.set_title('Distance vs. Prob of Two Points Within ' + str(t) + ' of Each Other')
    #ax.plot(xs,probs,'o-')
    #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    #ax.set_ylabel("Probability")
    #ax.set_xlabel("Distance between tow tethers (nm)")
    #plt.savefig(title)

xs = [5.44,10.88,16.32]
bins_01 = [2.44154e-07,7.1411e-08,6.01e-10]
thresh_01 = [7.11586e-07,2.24083e-07,1.86e-09]

bins_25 = [3.84465e-06,1.105611e-06,9.498e-09]
thresh_25 = [1.6279584e-05,4.733552e-06,4.0869e-08]

bins_5 = [3.0169692e-05, 8.762293e-06,7.7192e-08]
thresh_5 = [0.000129316425, 3.753394e-05, 3.3717e-07]

fig = plt.figure()
ax = fig.add_subplot(111)
bins = ax.plot(xs, bins_5, 'ro-', label='bin')
thresh = ax.plot(xs, thresh_5, 'bo-', label='threshold')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_ylabel("Probability")
ax.set_xlabel("Distance between toeholds (nm)")
ax.set_title('Distance vs. Probability. 0.5 nm bins/threshold')
plt.show()
