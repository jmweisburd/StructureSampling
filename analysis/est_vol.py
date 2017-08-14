import os
from utility import inter_vol
from probability_calc import ProbabilityCalculator

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)

long_path = base + "/data" + "/uni" + "/10.88" + "/long.txt"
short_path = base + "/data" + "/uni" + "/10.88" + "/short.txt"

for b in [0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.5]:
    print("")
    print(str(b) + " nm BIN WIDTH")
    print("")
    pc = ProbabilityCalculator()
    pc.set_bw(b)
    pc.read_files_to_maps(long_path, short_path)
    #vol = pc.volume_estimate()
    #print("VOLUME ESTIMATE " + str(vol))
    #print("")
    prob = pc.calculate_bin_probability()
    print("PROBABLITY " + str(prob))
    print("")
