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
np.set_printoptions(threshold='nan') 

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


class FCC_Lattice:
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
        
        
    def phaseTotal(self):
            for plane in xrange(len(self.plaquet[:,0,0,0,0])):
                for layer in xrange(len(self.plaquet[0,:,0,0,0])):
                    for d1 in xrange(len(self.plaquet[0,0,:,0,0])):
                        for d2 in xrange(len(self.plaquet[0,0,0,:,0])):    
                            phase = 0     
                            for p in xrange(len(self.plaquet[0,0,0,0,:]) - 1): 
                                if (self.plaquet[plane,layer,d1,d2,p] - self.plaquet[plane,layer,d1,d2,p+1] == 1) or (self.plaquet[plane,layer,d1,d2,3] - self.plaquet[plane,layer,d1,d2,0] == 1):
                                    phase += 3 
                                elif (self.plaquet[plane,layer,d1,d2,p] - self.plaquet[plane,layer,d1,d2,p+1] == -1) or (self.plaquet[plane,layer,d1,d2,3] - self.plaquet[plane,layer,d1,d2,0] == -1):
                                    phase -= 3
                                else:
                                    phase += 0      
                            if (phase == 9):
                                self.plaquet[plane,layer,d1,d2] = 5 #each value replaced with 5 if right handed
                                self.total +=1
                            elif (phase == -9 ):
                                self.plaquet[plane,layer,d1,d2] = 6 #each value replaced with 6 if right handed
                                self.total +=1
                            else:
                                self.plaquet[plane,layer,d1,d2] = 7 #if no string through face each value replaced with 7
            
            
        
        
N = 10
space = SpaceCube(N)
#print lattice.box
lattice = FCC_Lattice(N)
print lattice.faces
