##########################################################################################
#
# Code for efficiently drawing samples from a worm-like chain distribution
#
# NB: for single-stranded DNA, we use persistance length s = 2 nm = 2e-9 m
#
# Written by Matt Lakin
##########################################################################################

import math
import random
import numpy
import scipy.integrate

# Compute probability density of worm-like chain (WLC) of length L with
# persistence length s being extended to length R.
# R, s, and L should all have the same length unit.
def wlc_prob_density(R, s, L):
    if R > L:
        raise ValueError('R > L')
    elif R == L:
        raise ValueError('R == L')
    R = float(R)
    s = float(s)
    L = float(L)
    t = L / s
    r = R / L
    A = ((4.0 * ((0.75*t)**1.5) * math.exp(0.75*t)) /
         ((math.pi**1.5) * (4.0 + 12/(0.75*t) + 15/((0.75*t)**2))))
    res = (1.0 / L) * ((4.0*math.pi*A*(r**2)*math.exp(-0.75*t/(1.0-(r**2)))) /
                       ((1.0-r**2)**4.5))
    return res

# This global variable is a cache for precomputed WLC cumulative probability distributions
__wlc_cache__ = {}

# This function serves as an interface to get WLC cumulative probability distributions
# If nothing is stored in the cache for the supplied argument combination, the cumulative probabilities are computed and stored in the cache
# If there is an entry in the cache for the supplied argument combination, it is simply returned
def get_wlc_cumul_probs(s, L, num_slices):
    global __wlc_cache__
    if (s,L,num_slices) not in __wlc_cache__:
        these_xs = []
        these_probs = []
        delta = L / num_slices
        x = delta
        while True:
            cumul_prob = scipy.integrate.quad(lambda R: wlc_prob_density(R,s,L), 0.0, x)[0]
            these_xs += [x]
            these_probs += [cumul_prob]
            if x >= L:
                break
            x = L if x+delta > L else x+delta
        __wlc_cache__[(s,L,num_slices)] = (list(these_xs), list(these_probs))
    return __wlc_cache__[(s,L,num_slices)]

# Sample a single value from the WLC distribution with persistence length s and maximum length L.
# s and L should both have the same length unit.
# Assume that the distribution has been approximated via discretization into num_slices slices (default 1000).
def get_a_wlc_sample(s, L, num_slices=1000):
    (xs, cumul_probs) = get_wlc_cumul_probs(s, L, num_slices=num_slices)
    pGenerated = float(random.random())
    res = numpy.interp(pGenerated, cumul_probs, xs)
    return res
