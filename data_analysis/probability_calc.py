from coords import *
from utility import *
import numpy as np

class ProbabilityCalculator:
    def __init__(self, bin_width):
        self.complex_map = {}
        self.simple_map = {}
        self.same_map = {}
        self.bw = bin_width

    def fill_in_maps(self, path1, path2):
        with open(path1, "r") as f:
            for line in f:
                x,y,z = parse_line(line)
                x_round, y_round, z_round = myround(x,2,self.bw), myround(y,2,self.bw), myround(z,2,self.bw)
                round_coord = CartesianCoords(x_round, y_round, z_round)
                if round_coord not in self.complex_map.keys():
                    self.complex_map[round_coord] = 1
                else:
                    self.complex_map[round_coord] += 1
        f.close()
        with open(path2, "r") as f:
            for line in f:
                x,y,z = parse_line(line)
                x_round, y_round, z_round = myround(x), myround(y), myround(z)
                round_coord = CartesianCoords(x_round, y_round, z_round)
                if round_coord not in self.simple_map.keys():
                    self.simple_map[round_coord] = 1
                else:
                    self.simple_map[round_coord] += 1

        for key in self.complex_map.keys():
            if key in self.simple_map.keys():
                self.same_map[key] = 1

    def calculate_probability(self):
        complex_count = []
        simple_count = []
        for key in self.same_map.keys():
            complex_count.append(self.complex_map[key])
            simple_count.append(self.simple_map[key])

        total_prob = 0
        for i in range(len(complex_count)):
            total_prob += complex_count[i]*simple_count[i]
        return(total_prob/(pow(1000000,2)))
