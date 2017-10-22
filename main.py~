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



N = 10
lattice = SpaceCube(N)
print lattice.box