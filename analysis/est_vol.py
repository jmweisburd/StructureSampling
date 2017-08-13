import os
from utility import inter_vol
from probability_calc import ProbabilityCalculator

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)

long_path = base + "/data" + "/uni" + "/10.88" + "/long.txt"
short_path = base + "/data" + "/uni" + "/10.88" + "/short.txt"

pc = ProbabilityCalculator()
pc.set_bw(0.5)
pc.read_files_to_maps(long_path, short_path)

vol = pc.volume_estimate()
print("")
print("VOLUME ESTIMATE: " + str(vol))
