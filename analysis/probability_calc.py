from coords import *
from utility import *
import numpy as np

class ProbabilityCalculator:
    def __init__(self, bin_width):
        self.long_map = {}
        self.short_map = {}
        self.same_map = {}
        self.bw = bin_width

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
        for k,vs in self.short_map.items():
            for v in vs:
                try:
                    thresh_count = len(self.long_map[k])
                except KeyError:
                    thresh_count = 0
                next_to = self.generate_surrounding_keys(k)
                for n in next_to:
                    if n != k:
                        try:
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
        for key in self.short_map.keys():
            if key in self.long_map.keys():
                total_prob += (len(self.short_map[key])) * (len(self.long_map[key]))
        return(total_prob/(pow(1000000,2)))
