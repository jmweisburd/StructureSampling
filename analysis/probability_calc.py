from coords import *
from utility import *
import math
import numpy as np

class ProbabilityCalculator:
    def __init__(self):
        self.long_map = {}
        self.short_map = {}
        self.same_map = {}
        self.bw = None
        self.num_colocating_bins = 0

    def reset_maps(self):
        self.short_map = {}
        self.long_map = {}
        self.same_map = {}

    def set_bw(self, bw):
        self.bw = bw

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
        thresh_vol_map = {}
        for k in self.short_map.keys():
            if k in self.long_map.keys():
                thresh_vol_map[k] = 1
                vs = self.short_map[k]
                for v in vs:
                    thresh_count = len(self.long_map[k])
                    next_to = self.generate_surrounding_keys(k)
                    for n in next_to:
                        if n != k:
                            try:
                                l = self.long_map[n]
                                l = list(filter(lambda x: v.distance(x) <= self.bw, l))
                                thresh_count += len(l)
                                thresh_vol_map[n] = 1
                            except KeyError:
                                pass
                    total_prob += thresh_count
        self.num_colocating_bins = len(thresh_vol_map.keys())
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

    def volume_estimate(self):
        same = []
        colocating_bins = 0
        for key in self.short_map.keys():
            if key in self.long_map.keys():
                same.extend(self.short_map[key])
                colocating_bins += 1
        print("NUMBER OF SHARED BINS: " + str(colocating_bins))
        print("VOL OF SHARED BINS: " + str(colocating_bins*pow(self.bw, 3)))
        len_s = (len(same)-1)
        same = sorted(same, key=lambda b: b.x)
        x_min, x_max = same[0].x, same[len_s].x
        same = sorted(same, key=lambda b: b.y)
        y_min, y_max = same[0].y, same[len_s].y
        same = sorted(same, key=lambda b: b.z)
        z_min, z_max = same[0].z, same[len_s].z

        print("X MIN: " + str(x_min))
        print("X MAX: " + str(x_max))
        print("Y MIN: " + str(y_min))
        print("Y MAX: " + str(y_max))
        print("Z MIN: " + str(z_min))
        print("Z MAX: " + str(z_max))

        x_diff = x_max - x_min
        y_diff = y_max - y_min
        z_diff = z_max - z_min

        return (x_diff * y_diff * z_diff)
