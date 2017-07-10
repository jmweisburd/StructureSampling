import string_dna_parser
import polar_cords as pc
import math
import matplotlib.pyplot as plt

#J(id, down_domain, up_domain)
#D(id, stranded, down_joint, up_joint, length)
example = "(0,0,0);J(0,_,0);D(0,S,0,1,5);J(1,0,1);D(1,D,1,2,35);J(2,1,2);D(2,S,2,3,5);J(3,2,3);D(3,D,3,4,35);J(4,3,4);D(4,S,4,5,5);J(5,4,_)"
struct = string_dna_parser.parse_string(example)
struct.simulate_structure()
cs = struct.get_last_joint_coords()

i = 0
f = open('data.txt', 'w')
while i < 2:
    struct.simulate_structure()
    cs = struct.get_last_joint_coords()
    f.write(str(cs[0]) + "," + str(cs[1]) + "," +str(cs[2]) + "\n")
    i+= 1

f.close()

##GRAPHING STUFF###

#first = struct.simulate_structure()
#xs1, zs1 = struct.get_xs_zs()
#second = struct.simulate_structure()
#xs2, zs2 = struct.get_xs_zs()
#third = struct.simulate_structure()
#xs3, zs3 = struct.get_xs_zs()

#circle = plt.Circle((0,0), 34, color='black', fill=False)
#ax = plt.gca()
#ax.cla()

#ax.set_xlim((-34,34))
#ax.set_ylim((0,34))
#ax.plot(xs1,zs1, 'r-', xs2, zs2, 'b-', xs3,zs3,'g-')
#plt.xlabel('x axis (nm)')
#plt.ylabel('z axis (nm)')
#ax.add_artist(circle)
#plt.show()
