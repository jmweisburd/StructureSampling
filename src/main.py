import string_dna_parser
import coords
import math
import matplotlib.pyplot as plt

#J(id, down_domain, up_domain)
#D(id, stranded, down_joint, up_joint, length)
s1 = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,D,1,2,35);J(2,1,2);D(2,S,2,3,5);J(3,2,3);D(3,D,3,4,35);J(4,3,4);D(4,S,4,5,2.5);J(5,4,_)"
s2 = "(0,30,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,S,1,2,5);J(2,1,_)"

dna_struct = string_dna_parser.parse_string(s1)
f = open('long.txt', 'w')
i = 0
while i < 1000000:
    dna_struct.simulate_structure()
    cs = dna_struct.get_target_coords()
    f.write(str(cs)+"\n")
    i+= 1
f.close()

dna_struct = string_dna_parser.parse_string(s2)
f = open('short.txt', 'w')
i = 0
while i < 1000000:
    dna_struct.simulate_structure()
    cs = dna_struct.get_target_coords()
    f.write(str(cs)+"\n")
    i+= 1
f.close()
