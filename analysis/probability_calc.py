from coords import *
from utility import *
import math
import numpy as np

#Calculates the area of intersection between two hemispheres
#d: distance between the center of two spheres
#R: Radius of sphere 1
#r: Radius of sphere 2
def total_area(d, R, r):
    term1 = (R+r-(pow(d,2)))
    term2 = ((pow(d,2))+(2*d*r)-(3*(pow(r,2))) + (2 * d * R) + (6*r*R) - (3*(pow(R,2))))
    term3 = (12 * d)
    return (math.pi * term1 * term2)/(2*term3)

class ProbabilityCalculator:
    def __init__(self, bin_width):
        self.long_map = {}
        self.short_map = {}
        self.same_map = {}
        self.bw = bin_width
        self.num_colocating_bins = 0

    def read_files_to_maps(self, path1, path2):
        with open(path1, "r") as f:
            for line in f:
                x,y,z = parse_line(line)
                exact_coord = CC(x,y,z)
                x_round, y_round, z_round = myround(x,2,self.bw), myround(y,2,self.bw), myround(z,2,self.bw)
                round_coord = CC(x_round, y_round, z_round)
                if round_coord not in self.long_map.keys():
                    self.long_map[round_coord] = [exact_coord]
                else:
                    self.long_map[round_coord].append(exact_coord)
        f.close()
        with open(path2, "r") as f:
            for line in f:
                x,y,z = parse_line(line)
                exact_coord = CC(x,y,z)
                x_round, y_round, z_round = myround(x,2,self.bw), myround(y,2,self.bw), myround(z,2,self.bw)
                round_coord = CC(x_round, y_round, z_round)
                if round_coord not in self.short_map.keys():
                    self.short_map[round_coord] = [exact_coord]
                else:
                    self.short_map[round_coord].append(exact_coord)

    def calculate_threshold_probability(self):
        total_prob = 0
        self.num_colocating_bins = 0
        for k in self.short_map.keys():
            if k in self.long_map.keys():
                self.num_colocating_bins += 1
                vs = self.short_map[k]
                for v in vs:
                    thresh_count = len(self.long_map[k])
                    next_to = self.generate_surrounding_keys(k)
                    for n in next_to:
                        if n != k:
                            try:
                                self.num_colocating_bins += 1
                                l = self.long_map[n]
                                l = list(filter(lambda x: v.distance(x) <= self.bw, l))
                                thresh_count += len(l)
                            except KeyError:
                                pass
                    total_prob += thresh_count
        return total_prob/(pow(1000000,2))

    def generate_surrounding_keys(self, key):
        keys = []
        xs = [key.x-self.bw, key.x, key.x+self.bw]
        ys = [key.y-self.bw, key.y, key.y+self.bw]
        zs = [key.z-self.bw, key.z, key.z+self.bw]
        for x in xs:
            for y in ys:
                for z in zs:
                    keys.append(CC(x,y,z))
        return keys

    def calculate_bin_probability(self):
        total_prob = 0
        self.num_colocating_bins = 0
        for key in self.short_map.keys():
            if key in self.long_map.keys():
                self.num_colocating_bins += 1
                total_prob += (len(self.short_map[key])) * (len(self.long_map[key]))
        return(total_prob/(pow(1000000,2)))

    def calculate_colocating_volume(self):
        return (pow(self.bw,3)*self.num_colocating_bins)
