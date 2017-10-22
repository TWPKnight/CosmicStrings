"""
RHUL PH4100 - Major Project
Cosmic Strings
Started: 14/10/2017
Thomas Hyatt & Virginia d'Emilio
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint 

class SpaceCube:

    def __init__(self, N):
        """
        Constructor that creates a cubic lattice (NxNxN) and 
        assigns a random number (0, 1 or 2) to each point
        """
        box = np.zeros((N,N,N))
        for i in range(len(box[:,0,0])):
            for j in range(len(box[0,:,0])):
                for k in range(len(box[0,0,:])):
                    box[i,j,k] = randint(0,2)
        self.box=box


class Lattice:
    def __init__(self, N):
        """
        Defining lattice with phase points at the centre of each face
        0th elem. vertical faces
        1st elem. central faces
        2nd elem. horizontal faces
        """
        faces = np.zeros(((N-1)**3,3))
        n=-1
        for i in range(len(space.box[:,0,0])-1):
            for j in range(len(space.box[0,:,0])-1):
                for k in range(len(space.box[0,0,:])-1):
                    n=n+1
                    faces[n,0]= space.box[i+1,j,k]
                    faces[n,1]=space.box[i,j+1,k]
                    faces[n,2]=space.box[i,j,k+1]
                    
                    
        self.faces=faces
N = 10
space = SpaceCube(N)
print lattice.box
lattice = Lattice(N)
print lattice.faces
