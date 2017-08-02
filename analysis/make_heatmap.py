import matplotlib.pyplot as plt
import numpy as np

xs = []
ys = []
zs = []

def parse_line(s):
    split_array = s.split(",")
    x, y, z = split_array[0], split_array[1], split_array[2]
    return float(x), float(y), float(z)

with open("short.txt", "r") as f:
    for line in f:
        x,y,z = parse_line(line)
        xs.append(x)
        ys.append(y)
        zs.append(z)


#heatmap, xedges, yedges = np.histogram2d(ys, zs, bins=(128,128))
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plt.clf()
#plt.ylabel('z (nm)')
#plt.xlabel('y (nm)')
#plt.imshow(heatmap, extent=extent)
#plt.show()

n, bins, patches = plt.hist(zs, 64,facecolor="blue", alpha=0.5)
plt.xlabel('z (nm)')
plt.show()
