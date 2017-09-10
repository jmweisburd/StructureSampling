from coords import *
import random
from constants import DS_LENGTH, SS_LENGTH
import options
from wlc import *
from nicked_distribution import *

class DNA_Structure:
    def __init__(self, cart_coords, joint_list, domain_list, wormlike, nicked):
        self.joint_list = joint_list
        self.domain_list = domain_list
        #tether_location is in cartesian coordinates (x,y,z)
        self.tether_location = cart_coords
        self.worm = wormlike
        self.nicked = nicked
        self.number_nicked = 0
        if nicked:
            self.nd = NickedDistribution()

    #Moves the toe-hold of the tether along the y-axis
    #y_d: distance (in nm) to move the toe-hold
    def move_y_tether(self, y_d):
        self.tether_location = CartesianCoords(0, y_d, 0)

    #Goes through the joint_list and returns the joint which matches the argument id
    #id_to_find: id of the joint to find
    def get_joint_by_id(self, id_to_find):
        joint = None
        for j in self.joint_list:
            if j.id == id_to_find:
                joint = j
        return joint

    #Goes through the domain_list and return the domain which matches the argument id
    #id_to_find: id of the domain to find
    def get_domain_by_id(self, id_to_find):
        domain = None
        for d in self.domain_list:
            if d.id == id_to_find:
                domain = d
        return domain

    #Simulates the structure by generating random vectors and adding them together
    def simulate_structure(self):
        next_domain = None
        for i in range(0, len(self.joint_list)-1):
            j = self.joint_list[i]
            if j.id == 0:
                j.cart_coords = (self.tether_location)
                next_domain = self.get_domain_by_id(j.up_domain)
                radial = next_domain.get_dna_length_nm(self.worm)
                new_vector = random_vector_pz(radial)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = add_3d_vectors(j.cart_coords, new_vector)
            else:
                current_vector = j.cart_coords
                next_domain = self.get_domain_by_id(j.up_domain)
                radial = next_domain.get_dna_length_nm(self.worm)
                last_domain = self.get_domain_by_id(j.down_domain)
                both_ds = (next_domain.stranded == "D") and (last_domain.stranded == "D")
                if both_ds:
                    self.number_nicked += 1
                new_vector = self.vector_generator(radial,both_ds)
                while (current_vector.z + new_vector.z) < 0:
                    new_vector = self.vector_generator(radial,both_ds)
                next_joint = self.get_joint_by_id(next_domain.up_joint)
                next_joint.cart_coords = add_3d_vectors(current_vector, new_vector)

    def vector_generator(self, radial, both_ds):
        if self.nicked and both_ds:
            ang = self.nd.generate_rand_from_pdf()
            new_vector = random_vector_nicked_dist(radial, ang)
        else:
            new_vector = random_vector(radial)
        return new_vector

    #Gets the last joint in the DNA structures
    def get_last_joint_coords(self):
        last_j = self.joint_list[len(self.joint_list)-1]
        return last_j.cart_coords

    #Temporary unspecialized function for simple example structures
    #Returns the midpoint in cartesian coordinates of the target domain
    def get_target_coords(self):
        j1, j2 = self.joint_list[len(self.joint_list)-2], self.joint_list[len(self.joint_list)-1]
        xm, ym, zm = (j1.cart_coords.x + j2.cart_coords.x)/2, (j1.cart_coords.y + j2.cart_coords.y)/2, (j1.cart_coords.z + j2.cart_coords.z)/2
        return CartesianCoords(xm, ym, zm)

#Class representation of a joint within the DNA structure
class Joint:
    #id = joint_id within the structure
    #down_domain = DNA domain downards (-z) of the joint
    #up_domain = DNA domain upwards (+z) of the joint_args
    #cart_coords = cartesian coordinate joint position in 3d space
    def __init__(self, j_id, dd, ud):
        self.id = j_id
        self.down_domain = dd
        self.up_domain = ud
        self.cart_coords = None

#Class representation of a DNA domain within the DNA structure
class Domain:
    #id = domian_id within the structure
    #stranded = string "D" or "S" for "double" or "single" stranded
    #down_joint = joint downards (-z) of the domain
    #up_joint = joint upwards (+z) of the domain
    #length = length (in nucleotides) of the DNA domain
    def __init__(self, d_id, ds, dj, up, l):
        self.id = d_id
        self.stranded = ds
        self.down_joint = dj
        self.up_joint = up
        self.length = float(l)

    #returns the length of a DNA domain in nm
    #if double stranded, returns the length of a rigid rigid rod
    #if single stranded, returns the length based on a uniform distribution or worm-chain distribution
    #   based on command line arguments
    def get_dna_length_nm(self, worm):
        if self.stranded == "D":
            return self.length*DS_LENGTH
        else:
            max_length = self.length*SS_LENGTH
            if worm:
                return get_a_wlc_sample(2, max_length)
            else:
                return random.uniform(0, max_length)
