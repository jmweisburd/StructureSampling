import math
import random as rand
import constants

#Input: x,y,z cartesian coordinates
#Output: A PolarCords object representation of x,y,z coordinates
def cartesian_to_polar(x,y,z):
    if x == 0 and y == 0 and z == 0:
        return PolarCoords(0,0,0)
    else:
        radial = math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2))
        polar = math.acos(z/radial)
        azim = math.atan2(y/x)
        return PolarCoords(radial, polar, azim)

def polar_to_cartesian(r, polar, azim):
    x = r*math.sin(polar)*math.cos(azim)
    y = r*math.sin(polar)*math.sin(azim)
    z = r*math.cos(polar)
    return (x,y,z)

def random_vector_generation(radial):
    polar = 0
    azim = 0
    while (polar==0):
        polar = rand.uniform(0, math.pi)
    while (azim==0):
        azim = rand.uniform(0, 2*math.pi)
    return polar_to_cartesian(radial, polar, azim)

#Random Vector Generation with a positive z value
def random_vector_generation_pz(radial):
    polar = 0
    azim = 0
    while (polar == 0):
        polar = rand.uniform(0, (math.pi/2))
    while (azim == 0):
        azim = rand.uniform(0,2*math.pi)
    return polar_to_cartesian(radial, polar, azim)

def add_3d_vectors(v1, v2):
    return ((v1[0]+v2[0]), (v1[1] + v2[1]), (v1[2] + v2[2]))

class PolarCoords:
    def __init__(self, r, polar, azim):
        self.radial = r
        self.polar = polar
        self.azim = azim

    def __repr__(self):
        return polar_coords_string

    def polar_to_cartesian(self):
        x = self.radial*(math.sin(self.polar))*(math.cos(self.azim))
        y = self.radial*(math.sin(self.polar))*(math.cos(self.azim))
        z = self.radial*(math.cos(self.polar))
        return x,y,z

    def polar_coords_string(self):
        return 'Radial: %f \t Polar: %f \t Azimuth: %f' %(self.radial, self.polar, self.azim)

    def cartesian_coords_string(self):
        x,y,z = self.polar_to_cartesian()
        return 'X: %f \t Y: %f \t Z: %f' %(x,y,z)
