#import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

def read_angles():
    angles = []
    with open('angles.tsv') as f:
        next(f)
        for line in f:
            data = line.split("\t")
            angles.append(float(data[0]))
    angles = angles[1:]
    return np.array(angles)


#pandas unfortunately is not on the CS machines
#def read_angles():
    #colnames = ['tethered','deleted']
    #data = pd.read_csv('angles.tsv', sep='\t', header=0, names=colnames)
    #angles = data.tethered.tolist()
    #return np.array(angles)

class NickedDistribution:
    def __init__(self):
        self.angles = read_angles()
        self.x_grid = np.linspace(min(self.angles), max(self.angles), len(self.angles))
        self.kdepdf = self.kde(self.angles, self.x_grid, bandwith=0.1)
        self.cdf = self.initalize_cdf()

    def kde(self, x,x_grid,bandwith=0.2, **kwargs):
        #Kernel Density Estimation with scipy
        kde = gaussian_kde(x,bw_method=bandwith/x.std(ddof=1),**kwargs)
        return kde.evaluate(x_grid)

    def initalize_cdf(self):
        cdf = np.cumsum(self.kdepdf)
        cdf = cdf / cdf[-1]
        return cdf

    def generate_rand_from_pdf(self):
        values = np.random.rand()
        value_bins = np.searchsorted(self.cdf, values)
        random_from_cdf = self.x_grid[value_bins]
        return random_from_cdf

#random_from_kde = generate_rand_from_pdf(kdepdf, x_grid)


#plt.hist(angles,36)
#plt.show()
