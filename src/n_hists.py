#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from nicked_distribution import NickedDistribution
from random import shuffle

def read_angles():
    angles = []
    with open('angles.tsv') as f:
        next(f)
        for line in f:
            data = line.split("\t")
            angles.append(float(data[0]))
    angles = angles[1:]
    return np.array(angles)

nd = NickedDistribution()

angles = read_angles()
nd_data = []
i = 0
while i < len(angles):
    nd_data.append(nd.generate_rand_from_pdf())
    i += 1

plt.subplot(111)
plt.hist(angles, 72, edgecolor='black', linewidth=1, alpha=0.2, color='blue', label='from paper')
plt.hist(nd_data, 72, edgecolor='black', linewidth=1, alpha=0.2, color='red', label='from estimated distribution')
plt.legend()
plt.show()
