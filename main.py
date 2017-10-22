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
        for n in xrange(0,len(self.cells[:,0,0])):      
            for f in xrange(0,len(self.cells[0,:,0])):  
                 
                            phase = 0 
                            
                            if (np.mod(self.cells[n,f,3] - self.cells[n,f,0],3) == 1):                                
                                phase += 3
                                #print self.cells[n,f] 
                            elif (np.mod(self.cells[n,f,3] - self.cells[n,f,0],3) == 2):
                                phase -= 3  
                                #print self.cells[n,f] 
                                
                                
                            for p in xrange(0,len(self.cells[0,0,:]) - 1): 
                                #print self.cells[n,f,p], self.cells[n,f,p+1]
                                if (np.mod(self.cells[n,f,p] - self.cells[n,f,p+1],3) == 1):
                                    phase += 3 
                                    #print self.cells[n,f] 
                                elif (np.mod(self.cells[n,f,p] - self.cells[n,f,p+1],3) == 2):
                                    phase -= 3
                                    #print self.cells[n,f] 
  
                            #print "Phase: ",phase         
                            if (phase == 9):
                                self.stringpresent[n,f] = 1 #left handed
                                self.total +=1
                            elif (phase == -9 ):
                                self.stringpresent[n,f] = 2 #right handed
                                self.total +=1
                            else:
                                self.stringpresent[n,f] = 0  #no string
            
            
        
        
N = 10
space = SpaceCube(N)
#print lattice.box
lattice = FCC_Lattice(N)
print lattice.faces
