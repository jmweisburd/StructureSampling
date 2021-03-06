import math
import numpy as np
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

def polar_to_cartesian(r, incl, azim):
    x = r*math.sin(incl)*math.cos(azim)
    y = r*math.sin(incl)*math.sin(azim)
    z = r*math.cos(incl)
    return CartesianCoords(x,y,z)

def random_vector(radial):
    incl = 0
    azim = 0
    while (incl==0):
        r = np.random.rand()
        incl = math.acos((2*r)-1)
    while (azim==0):
        r = np.random.rand()
        azim = 2 * math.pi * r
    return polar_to_cartesian(radial, incl, azim)

def random_vector_nicked(radial, ang_in_degrees):
    incl = math.radians(ang_in_degrees)
    azim = 0
    while (azim==0):
        r = np.random.rand()
        azim = rand.uniform(0, 2*math.pi)
    return polar_to_cartesian(radial, incl, azim)

#Generate random vector with a positive z value
#def random_vector_pz(radial):
    #polar = 0
    #azim = 0
    #while (polar == 0):
        #r = np.random.rand()
        #polar = math.acos((2*r)-1)
        #polar = rand.uniform(0, (math.pi/2))
    #while (azim == 0):
        #r = np.random.rand()
        #azim = 2 * math.pi * r
        #azim = rand.uniform(0,2*math.pi)
    #return polar_to_cartesian(radial, polar, azim)

#Adds two CartesianCoords objects together and the CartesianCoords ojbect sum
def add_3d_vectors(v1, v2):
    return CartesianCoords((v1.x + v2.x), (v1.y+v2.y), (v1.z+v2.z))

#Simple class for representing cartesian coordinates in 3D space
class CartesianCoords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return(str(self.x) + "," + str(self.y) + "," + str(self.z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        x_bool = (self.x == other.x)
        y_bool = (self.y == other.y)
        z_bool = (self.z == other.z)
        return (x_bool and y_bool and z_bool)

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
