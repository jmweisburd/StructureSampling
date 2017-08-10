from dna_structure import *
from coords import CartesianCoords

def id_parse(s):
    if s != "_":
        return int(s)
    else:
        return -1

def coords_parse(s):
    coord_strings = (s[s.find("(")+1:s.find(")")]).split(",")
    coord_list = list(map(lambda x: int(x), coord_strings))
    return CartesianCoords(coord_list[0], coord_list[1], coord_list[2])

def parse_string(dna_string, wormlike):
    dna_string_split = dna_string.split(";")
    cart_coords = coords_parse(dna_string_split[0])
    domain_joint_list = dna_string_split[1::]
    joints = []
    domains = []
    for dj in domain_joint_list:
        if dj[0] == "J":
            joint_args = (dj[dj.find("(")+1:dj.find(")")]).split(",")
            j_id, dd, ud = joint_args[0],joint_args[1], joint_args[2]
            joints.append(Joint(id_parse(j_id), id_parse(dd), id_parse(ud)))
        else:
            args = (dj[dj.find("(")+1:dj.find(")")]).split(",")
            d_id, ds, dj, uj, l = args[0], args[1], args[2], args[3], args[4]
            domains.append(Domain(id_parse(d_id), ds, id_parse(dj), id_parse(uj), l))

    return DNA_Structure(cart_coords, joints, domains, wormlike)
