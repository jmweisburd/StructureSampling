import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

x = [0,5,10,15,20,25,30]
y = [2.7436347e-05, 1.3386696e-05, 4.641307e-06, 2.129796e-06, 1.339994e-06, 3.70225e-07, 1.706e-09]

#plt.plot(x,y, 'ro-')
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.grid(True)
#plt.show()

fig =plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, 'o-')
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_ylabel("Probability")
ax.set_xlabel("Short Structure Distance from Long Structure")

plt.show()
