import string_dna_parser as dnap
import coords
#from mappings import *
import math
import matplotlib.pyplot as plt
import os

#J(id, down_domain, up_domain)
#D(id, stranded, down_joint, up_joint, length)
s1 = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,D,1,2,35);J(2,1,2);D(2,S,2,3,5);J(3,2,3);D(3,D,3,4,35);J(4,3,4);D(4,S,4,5,2.5);J(5,4,_)"
s2 = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,S,1,2,5);J(2,1,_)"

dna1 = dnap.parse_string(s1)
dna2 = dnap.parse_string(s2)

base = os.path.normpath(os.getcwd() + os.sep + os.pardir)
for y_d in range(0, 35, 5):
    path = base + '/data/'+ str(y_d)
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path + "/long.txt"
    f = open(file_path, 'w')
    i = 0
    while i < 2:
        dna1.simulate_structure()
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
    while i < 2:
        dna2.simulate_structure()
        cs = dna2.get_target_coords()
        f.write(str(cs)+"\n")
        i+= 1
    f.close()
