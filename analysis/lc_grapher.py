import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

#worm_chain_bin = [5.851026629767063, 46.750265794858684, 156.26089771606556, 366.28617955036356, 705.4769649201172]
#worm_chain_thresh = [20.023284289193093, 198.3961526637674, 666.3220234722344, 1561.2966095071854, 3005.39009301052]
#ideal_bin = [5.332746998087497, 42.69182132672477, 141.47090057641367, 327.2881526969119, 620.4028913530788]
#ideal_thresh = [17.773546347344006, 180.6769829536009, 604.7265712798477, 1408.7846807473472, 2697.508145069082]

uni_lcs = [114500.90254527864,111153.68935404066,106626.58843062635,101917.11498741005]
wc_lcs = [125666.21222456795,123096.75847684802,119388.63442135429,115162.8909401902]
ideal = [60069.7,60069.7,60069.7,60069.7]
bins = [0.5,1.0,1.5,2.0]

fig = plt.figure()
ax = fig.add_subplot(111)
ulcs = ax.plot(bins, uni_lcs, 'ro-', label = 'uniform')
wlcs = ax.plot(bins, wc_lcs, 'bo-', label='worm chain')
idls = ax.plot(bins, ideal, 'g-', label='experimental value')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("Local Concentration (nM)")
ax.set_xlabel("Threshold Size (nm)")
plt.show()
