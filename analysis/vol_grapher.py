import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

bins = [0.25,0.5,0.75,1.0,1.25]
sphere_vols = [337.17, 337.17,337.17,337.17,337.17]
bin_vols_uni = [137.9,273.9,349.3,408.0,466.8]
thresh_vols_uni = [182.375, 395.875, 558.984375, 718.0,906.25]
bin_vols_wc = [128.5, 251.75,321.9,388.0,447.3]
thresh_vols_wc = [160.5,366.5,526.078125,704.0,888.671875]

fig = plt.figure()
ax = fig.add_subplot(111)
s_vol = ax.plot(bins, sphere_vols, 'go-', label ='hemi-sphere vol')
b_vol_uni = ax.plot(bins, bin_vols_uni, 'bo-', label = 'add bins vol, uni')
t_vol_uni = ax.plot(bins, thresh_vols_uni, 'b^-', label = "add thresh vol, uni")
b_vol_wc = ax.plot(bins, bin_vols_wc, 'ro-', label='add bins vol, wc')
t_vol_wc = ax.plot(bins, thresh_vols_wc, 'r^-', label = 'add thresh vol, wc')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_ylabel("Volume (nm^3)")
ax.set_xlabel("Bin Size (nm)")
plt.show()

#bins = [0.25,0.5,0.75,1.0,1.25]
#bin_probs_uni = [1.082797e-06,8.668436e-06,2.8725208e-05,6.6454799e-05,0.000125970797]
#thresh_probs_uni = [3.608861e-06,3.6685876e-05,0.000122787771,0.000286049165,0.000547720289]
#bin_probs_wc = [1.188032e-06,9.49249e-06,3.1728269e-05,7.4373222e-05,0.000143244812]
#thresh_probs_wc = [4.065663e-06,4.0283696e-05,0.000135294528,0.000317016218,0.000610234721]

#bin_vol_uni = list(map(lambda x: 27644.185*x, bin_probs_uni))
#thresh_vol_uni = list(map(lambda x: 27644.185*x, thresh_probs_uni))
#bin_vol_wc = list(map(lambda x: 27644.185*x, bin_probs_wc))
#thresh_vol_wc = list(map(lambda x: 27644.185*x, thresh_probs_wc))

#fig = plt.figure()
#ax = fig.add_subplot(111)
#b_vol_uni = ax.plot(bins, bin_vol_uni, 'bo-', label = 'bins uni')
#t_vol_uni = ax.plot(bins, thresh_vol_uni, 'b^-', label = 'thresh uni')
#b_vol_wc = ax.plot(bins, bin_vol_wc, 'ro-', label='bins wc')
#t_vol_wc = ax.plot(bins, thresh_vol_wc, 'r^-', label = 'thresh uni')
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels)
#ax.set_ylabel("Volume (nm^3)")
#ax.set_xlabel("Bin Size (nm)")
#ax.set_title('Reactive volume necessary for 60069.7 nM local concentration')
#plt.show()
