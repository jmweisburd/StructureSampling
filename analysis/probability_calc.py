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

    def new_local_conc(self):
        local_concs = []
        for k in self.short_map.keys():
            if k in self.long_map.keys():
                vs = self.short_map[k]
                for v in vs:
                    thresh_count = len(self.long_map[k])
                    for n in self.generate_surround_keys(k):
                        if n != k:
                            try:
                                l = self.long_map[n]
                                l = list(filter(lambda x: v.distance(x) <= self.bw, l))
                                thresh_count += len(l)
                                prob = (thresh_count / 1000000)
                                lc = (prob / ((4/3) * math.pi * pow(self.bw, 3)))
                                lc = lc * 1660577881
                                local_concs.append(lc)
                            except KeyError:
                                pass
        total_lc = sum(local_concs)/len(local_concs)
        return total_lc

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

    def area_slice(self):
        common_keys = []
        for key in self.short_map.keys():
            if key in self.long_map.keys():
                common_keys.append(key)
        x_slice = list(filter(lambda k: k.x == 0, common_keys))
        x_slice = sorted(x_slice, key=lambda k: k.y)
        y_min = x_slice[0].y
        y_max = x_slice[-1].y
        curr = y_min
        mins = []
        maxs = []
        while curr <= y_max:
            key_list = []
            y_slice = list(filter(lambda k: k.y == curr, x_slice))
            y_slice = sorted(y_slice, key=lambda k: k.z)
            key_list.append(y_slice[0])
            key_list.append(y_slice[-1])
            z_min, z_max = self.get_points(key_list)
            mins.append(z_min)
            maxs.append(z_max)
            curr += self.bw
        return mins, maxs

    def get_points(self, key_list):
        z_min = None
        z_max = None
        all_points = []
        for k in key_list:
            short_list = self.short_map[k]
            long_list = self.long_map[k]
            all_points.extend(short_list)
            all_points.extend(long_list)
        all_points = sorted(all_points, key=lambda k: k.z)
        z_max = all_points[-1]
        z_min = all_points[0]
        return z_min, z_max

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
