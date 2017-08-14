import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

worm_chain_bin = [5.851026629767063, 46.750265794858684, 156.26089771606556, 366.28617955036356, 705.4769649201172]
worm_chain_thresh = [20.023284289193093, 198.3961526637674, 666.3220234722344, 1561.2966095071854, 3005.39009301052]
ideal_bin = [5.332746998087497, 42.69182132672477, 141.47090057641367, 327.2881526969119, 620.4028913530788]
ideal_thresh = [17.773546347344006, 180.6769829536009, 604.7265712798477, 1408.7846807473472, 2697.508145069082]

bins = [0.25,0.5,0.75,1.0,1.25]

fig = plt.figure()
ax = fig.add_subplot(111)
wcb = ax.plot(bins, worm_chain_bin, 'ro-', label ='worm chain, bin')
wct = ax.plot(bins, worm_chain_thresh, 'bo-', label = 'worm chain, thresh')
ib = ax.plot(bins, ideal_bin, 'r^-', label='ideal chain, bin')
it = ax.plot(bins, ideal_thresh, 'b^-', label='ideal chain, thresh')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("Local Concentration (nM)")
ax.set_xlabel("Bin/Threshold Size (nm)")
plt.show()
