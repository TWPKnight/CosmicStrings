"""
RHUL PH4100 - Major Project
Cosmic Strings
Started: 14/10/2017
Thomas Hyatt & Virginia d'Emilio
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random
from random import randint
random.seed(987654321) 
np.set_printoptions(threshold='nan')


class SpaceCube:
    
    def __init__(self, N):
        """
        Constructor that creates a cubic lattice (NxNxN) and assigns a random
        number (0, 1 or 2) to each point
        """
        box = np.zeros((N,N,N)) #(i, j, k) 
        xString = np.zeros((N-1,N,N-1))
        yString = np.zeros((N,N-1,N-1))
        zString = np.zeros((N-1,N-1,N))
        for i in xrange(len(box[:,0,0])):
            for j in xrange(len(box[0,:,0])):
                for k in xrange(len(box[0,0,:])):
                     box[i,j,k] = randint(0, 2)
        total =0
        faceNum=0
        self.box=box  
        self.xString=xString
        self.yString=yString
        self.zString=zString 
        self.total=total   
        self.faceNum=faceNum  
            
        self.faceDict={ 0 : [1,2,3,4],     #bottom
                        1 : [1,4,8,5],    #left
                        2 : [1,2,6,5],    #front
                        3 : [5,6,7,8],    #top
                        4 : [2,3,7,6],    #right
                        5 : [4,3,7,8]}    #back
                        
        self.facepointsDict={ 1:np.array([0,0,0]),     #(  ni    ,  nj    ,  nk    )
                        2:np.array([1,0,0]),     #(  ni+1  ,  nj    ,  nk    )
                        3:np.array([1,0,1]),     #(  ni+1  ,  nj    ,  nk+1  )
                        4:np.array([0,0,1]),     #(  ni    ,  nj    ,  nk+1  )
                        5:np.array([0,1,0]),     #(  ni    ,  nj+1  ,  nk    )
                        6:np.array([1,1,0]),     #(  ni+1  ,  nj+1  ,  nk    )
                        7:np.array([1,1,1]),     #(  ni+1  ,  nj+1  ,  nk+1  )
                        8:np.array([0,1,1])}     #(  ni+1  ,  nj    ,  nk+1  )

        
    def xPlane(self):
        for j in xrange(len(self.box[0,:,0])):
            for k in xrange(len(self.box[0,0,:])-1):
                for i in xrange(len(self.box[:,0,0])-1):                                                                  
                    xFace = np.zeros(4)
                    for p in range(4): 
                        xcorner = self.faceDict[0][p]    
                        Ix = i + self.facepointsDict[xcorner][0] 
                        Jx = j + self.facepointsDict[xcorner][1] 
                        Kx = k + self.facepointsDict[xcorner][2] 
                        xFace[p] = self.box[Ix,Jx,Kx]
                    self.xString[i,j,k] = self.isString(xFace)
                    
    def yPlane(self):
        for i in xrange(len(self.box[:,0,0])):
            for j in xrange(len(self.box[0,:,0])-1):
                for k in xrange(len(self.box[0,0,:])-1):                                                                    
                    yFace = np.zeros(4)
                    for p in range(4): 
                        ycorner = self.faceDict[1][p]    
                        Iy = i + self.facepointsDict[ycorner][0] 
                        Jy = j + self.facepointsDict[ycorner][1] 
                        Ky = k + self.facepointsDict[ycorner][2] 
                        yFace[p] = self.box[Iy,Jy,Ky]
                    self.yString[i,j,k] = self.isString(yFace)    
                    
    def zPlane(self):
        for k in xrange(len(self.box[0,0,:])):
            for j in xrange(len(self.box[0,:,0])-1):
                for i in xrange(len(self.box[:,0,0])-1):                                                                    
                    zFace = np.zeros(4)
                    for p in range(4): 
                        zcorner = self.faceDict[2][p]  
                        Iz = i + self.facepointsDict[zcorner][0] 
                        Jz = j + self.facepointsDict[zcorner][1] 
                        Kz = k + self.facepointsDict[zcorner][2] 
                        zFace[p] = self.box[Iz,Jz,Kz]
                    self.zString[i,j,k] = self.isString(zFace)                              
                                                                                                    
    def isString(self,face):   
        phase = 0   
        self.faceNum+=1
        if (np.mod(face[3] - face[0],3) == 1): #test right-most and left-most values                            
            phase += 3
        elif (np.mod(face[3] - face[0],3) == 2): #test right-most and left-most values
            phase -= 3                       
        for p in xrange(0,len(face[:]) - 1): #cycle through the rest            
            if (np.mod(face[p] - face[p+1],3) == 1):
                phase += 3 
            elif (np.mod(face[p] - face[p+1],3) == 2):
                phase -= 3              
        if (phase == 9):
            self.total +=1
            return -1 #left handed
        elif (phase == -9 ):
            self.total +=1
            return 1 #right handed            
        else:
            return 0  #no string
        
                                                                                                                                                                   
                                                                                                                                                           
N = 15
lattice = SpaceCube(N)
lattice.xPlane()
lattice.yPlane()
lattice.zPlane()

#print lattice.xString
#print lattice.yString
#print lattice.zString
print "Probability = ", (1.0 * lattice.total)/(1.0*lattice.faceNum)
