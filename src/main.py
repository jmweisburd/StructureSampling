import string_dna_parser as dnap
import coords
import numpy as np
import math
import os
from nicked_distribution import NickedDistribution
from options import *

#J(id, down_domain, up_domain)
#D(id, stranded, down_joint, up_joint, length)
s1 = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,D,1,2,18);J(2,1,2);D(2,D,2,3,18);J(3,2,3);D(3,S,3,4,6);J(4,3,_)"
s2 = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,S,1,2,6);J(2,1,_)"
y_ds = [5.44,10.88,12.0,13.5,21.76]

args = parser.parse_args()

if not args.worm:
    ss_distr = "uni"
else:
    ss_distr = "worm"
if not args.nicked:
    a_distr = "uni"
else:
    a_distr = "nicked"

dna1 = dnap.parse_string(s1, args.worm, args.nicked)
dna2 = dnap.parse_string(s2, args.worm, args.nicked)

if args.nicked:
    nd = NickedDistribution()
    dna1.nd = nd
    dna2.nd = nd

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)

for y_d in y_ds:
    path = base + '/data/' + ss_distr + '_' + a_distr + '/' + str(y_d)

    if not os.path.exists(path):
        os.makedirs(path)

    file_path = path + "/long.txt"
    f = open(file_path, 'w')
    i = 0
    while i < 1000000:
        dna1.number_nicked = 0
        dna1.simulate_structure()
        #print(dna1.number_nicked)
        cs = dna1.get_target_coords()
        f.write(str(cs)+"\n")
        i+= 1
    f.close()

    file_path = path + "/short.txt"
    dna2.move_y_tether(y_d)
    print("Moving short to " + str(y_d) + "y position")
    f = open(file_path, 'w')
    i = 0
    print("Simulating Short Structure")
    while i < 1000000:
        dna2.number_nicked = 0
        dna2.simulate_structure()
        #print(dna2.number_nicked)
        cs = dna2.get_target_coords()
        f.write(str(cs)+"\n")
        i+= 1
    f.close()
