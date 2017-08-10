from coords import *
import random
from constants import DS_LENGTH, SS_LENGTH
import options
from wlc import

class DNA_Structure:
    def __init__(self, cart_coords, joint_list, domain_list):
        self.joint_list = joint_list
        self.domain_list = domain_list
        #tether_location is in cartesian coordinates (x,y,z)
        self.tether_location = cart_coords
        self.worm = False

    def move_y_tether(self, y_d):
        self.tether_location = CartesianCoords(0, y_d, 0)

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
                new_vector = random_vector_generation_pz(radial)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = add_3d_vectors(j.cart_coords, new_vector)
            else:
                current_vector = j.cart_coords
                next_domain = self.get_domain_by_id(j.up_domain)
                radial = next_domain.get_dna_length_nm()
                new_vector = random_vector_generation(radial)
                while (current_vector.z + new_vector.z) < 0:
                    new_vector = random_vector_generation(radial)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = add_3d_vectors(current_vector, new_vector)

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

    #Temporary unspecialized function for simple example structures
    def get_target_coords(self):
        j1, j2 = self.joint_list[len(self.joint_list)-2], self.joint_list[len(self.joint_list)-1]
        xm, ym, zm = (j1.cart_coords.x + j2.cart_coords.x)/2, (j1.cart_coords.y + j2.cart_coords.y)/2, (j1.cart_coords.z + j2.cart_coords.z)/2
        return CartesianCoords(xm, ym, zm)

    def get_joint_z_differences(self):
        z_diff = []
        for i in range(0, len(self.joint_list)-1):
            j = self.joint_list[i]
            d_next = self.get_domain_by_id(j.up_domain)
            j_next = self.get_joint_by_id(d_next.up_joint)
            diff = j_next.cart_coords[2] - j.cart_coords[2]
            z_diff.append(diff)
        return z_diff

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
        self.length = float(l)

    def get_dna_length_nm(self):
        if self.stranded == "D":
            return self.length*DS_LENGTH
        else:
            max_length = self.length*SS_LENGTH
            if self.wc:
                return get_a_wlc_sample(2, max_length)
            else:
                return random.uniform(0, max_length)
