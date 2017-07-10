import polar_cords as pc
import random
from constants import DS_LENGTH, SS_LENGTH

class DNA_Structure:
    def __init__(self, cart_coords, joint_list, domain_list):
        self.joint_list = joint_list
        self.domain_list = domain_list
        #tether_location is in cartesian coordinates (x,y,z)
        self.tether_location = (cart_coords[0], cart_coords[1], cart_coords[2])

    def get_joint_by_id(self, id_to_find):
        joint = None
        for j in self.joint_list:
            if j.id == id_to_find:
                joint = j
        return joint

    def get_domain_by_id(self, id_to_find):
        domain = None
        for d in self.domain_list:
            if d.id == id_to_find:
                domain = d
        return domain

    def simulate_structure(self):
        next_domain = None
        for i in range(0, len(self.joint_list)-1):
            j = self.joint_list[i]
            if j.id == 0:
                j.cart_coords = (self.tether_location)
                next_domain = self.get_domain_by_id(j.up_domain)
                radial = next_domain.get_dna_length_nm()
                new_vector = pc.random_vector_generation_pz(radial)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = pc.add_3d_vectors(j.cart_coords, new_vector)
            else:
                current_vector = j.cart_coords
                next_domain = self.get_domain_by_id(j.up_domain)
                radial = next_domain.get_dna_length_nm()
                new_vector = pc.random_vector_generation(radial)
                while (current_vector[2] + new_vector[2]) < 0:
                    new_vector = pc.random_vector_generation(radial)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = pc.add_3d_vectors(current_vector, new_vector)

    def print_joints(self):
        for j in self.joint_list:
            print(j.cart_coords)

    def print_domains(self):
        for d in self.domain_list:
            print(d.id, d.stranded, d.down_joint, d.up_joint, d.length)

    def get_xs_zs(self):
        xs = []
        zs = []
        for j in self.joint_list:
            xs.append(j.cart_coords[0])
            zs.append(j.cart_coords[2])
        return xs, zs

    def get_last_joint_coords(self):
        last_j = self.joint_list[len(self.joint_list)-1]
        return last_j.cart_coords

class Joint:
    def __init__(self, j_id, dd, ud):
        self.id = j_id
        self.down_domain = dd
        self.up_domain = ud
        self.cart_coords = None

class Domain:
    def __init__(self, d_id, ds, dj, up, l):
        self.id = d_id
        self.stranded = ds
        self.down_joint = dj
        self.up_joint = up
        self.length = int(l)

    def get_dna_length_nm(self):
        if self.stranded == "D":
            return self.length*DS_LENGTH
        else:
            max_length = self.length*SS_LENGTH
            return random.uniform(0, max_length)
