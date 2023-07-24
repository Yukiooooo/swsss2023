#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Yu Hong'
__email__ = 'yu.hong@mavs.uta.edu'

# import shits
from math import pi
import math
import numpy as np
import matplotlib.pyplot as plt  # use for plot

def spher2carn(r, phi, theta):
    '''
    This funct is used for converting spherical 
    coordinate into cartesian coordinate
    '''
    #%%
    x = r * np.sin(phi) * np.cos(theta) # x - component
    y = r * np.sin(phi) * np.sin(theta) # y - component
    z = r * np.cos(phi) # z - component
    
    return x, y, z

#%% test the code
carn_coor = spher2carn(1, pi,pi)
#print (carn_coor[0])

ref = (0,0,-1)
assert np.allclose((carn_coor[0],carn_coor[1],carn_coor[2]), ref)
print (np.allclose((carn_coor[0],carn_coor[1],carn_coor[2]), ref))

# number = 42
# assert number > 0, f"number greater than 0 expected, got: {number}"


def spherical_cartesian(radius, azimuth, zentith):
    """Convert spherical coordinates to cartesian"""
    x = radius*np.sin(zentith)*np.cos(azimuth)
    y = radius*np.sin(zentith)*np.sin(azimuth)
    z = radius*np.cos(zentith)
    return x, y, z

fig = plt.figure()  # better control
axes = fig.gca(projection='3d')  # make 3d axes
r = np.linspace(0, 1)
theta = np.linspace(0, np.pi)
phi = np.linspace(0, np.pi)
x, y, z = spherical_cartesian(r, theta, phi)
axes.plot(x, y, z)











