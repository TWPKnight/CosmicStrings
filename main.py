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

def PrintPnF(i,j,k):
    '''
    Prints the points of the cube around the bottom left identifiter ijk
    and also prints the string state of each face of that cube
    '''
    print
    print "P1:(0,0,0) = ",lattice.box[i,j,k]
    print "P2:(1,0,0) = ",lattice.box[i+1,j,k]
    print "P3:(1,0,1) = ",lattice.box[i+1,j,k+1]
    print "P4:(0,0,1) = ",lattice.box[i,j,k+1]
    print "P5:(0,1,0) = ",lattice.box[i,j+1,k]
    print "P6:(1,1,0) = ",lattice.box[i+1,j+1,k]
    print "P7:(1,1,1) = ",lattice.box[i+1,j+1,k+1]
    print "P8:(0,1,1) = ",lattice.box[i,j+1,k+1]
    print
    print "X(0,0,0) = ",lattice.yString[i,j,k]
    print "X(0,1,0) = ",lattice.yString[i,j+1,k]
    print "Y(0,0,0) = ",lattice.xString[i,j,k]
    print "Y(1,0,0) = ",lattice.xString[i+1,j,k]
    print "Z(0,0,0) = ",lattice.zString[i,j,k]
    print "Z(0,0,1) = ",lattice.zString[i,j,k+1]
    


class SpaceCube:
    
    def __init__(self, N):
        """
        Constructor that creates a cubic lattice (NxNxN) and assigns a random
        number (0, 1 or 2) to each point
        """
        box = np.zeros((N,N,N)) #(i, j, k) 
        yString = np.zeros((N-1,N,N-1))
        xString = np.zeros((N,N-1,N-1))
        zString = np.zeros((N-1,N-1,N))
        for i in xrange(len(box[:,0,0])):
            for j in xrange(len(box[0,:,0])):
                for k in xrange(len(box[0,0,:])):
                     box[i,j,k] = randint(0, 2)
        total =0 
        faceNum=0
        edge = False
        L=0
        length=[]
        self.L=L
        self.length=length
        self.box=box
        self.edge=edge  
        self.yString=yString
        self.xString=xString
        self.zString=zString 
        self.total=total   
        self.faceNum=faceNum  
            
        self.faceDict={ 0 : [1,2,3,4],     #bottom
                        1 : [1,4,8,5],    #left
                        2 : [1,5,6,2],    #front
                        3 : [5,6,7,8],    #top
                        4 : [2,3,7,6],    #right
                        5 : [4,8,7,3]}    #back
                        
        self.facepointsDict={ 1:np.array([0,0,0]),     #(  ni    ,  nj    ,  nk    )
                        2:np.array([1,0,0]),     #(  ni+1  ,  nj    ,  nk    )
                        3:np.array([1,0,1]),     #(  ni+1  ,  nj    ,  nk+1  )
                        4:np.array([0,0,1]),     #(  ni    ,  nj    ,  nk+1  )
                        5:np.array([0,1,0]),     #(  ni    ,  nj+1  ,  nk    )
                        6:np.array([1,1,0]),     #(  ni+1  ,  nj+1  ,  nk    )
                        7:np.array([1,1,1]),     #(  ni+1  ,  nj+1  ,  nk+1  )
                        8:np.array([0,1,1])}     #(  ni+1  ,  nj    ,  nk+1  )

        
    def yPlane(self):
        for j in xrange(len(self.box[0,:,0])):
            for k in xrange(len(self.box[0,0,:])-1):
                for i in xrange(len(self.box[:,0,0])-1):                                                                  
                    yFace = np.zeros(4)
                    for p in range(4): 
                        ycorner = self.faceDict[0][p]    
                        Iy = i + self.facepointsDict[ycorner][0] 
                        Jy = j + self.facepointsDict[ycorner][1] 
                        Ky = k + self.facepointsDict[ycorner][2] 
                        yFace[p] = self.box[Iy,Jy,Ky]
                    self.yString[i,j,k] = self.isString(yFace)
                    
    def xPlane(self):
        for i in xrange(len(self.box[:,0,0])):
            for j in xrange(len(self.box[0,:,0])-1):
                for k in xrange(len(self.box[0,0,:])-1):                                                                    
                    xFace = np.zeros(4)
                    for p in range(4): 
                        ycorner = self.faceDict[1][p]    
                        Ix = i + self.facepointsDict[ycorner][0] 
                        Jx = j + self.facepointsDict[ycorner][1] 
                        Kx = k + self.facepointsDict[ycorner][2] 
                        xFace[p] = self.box[Ix,Jx,Kx]
                    self.xString[i,j,k] = self.isString(xFace)    
                    
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
        
    def check_in_out_equal(self):
        s=0
        for i in xrange(len(self.box[:,0,0])-1):
            for j in xrange(len(self.box[0,:,0])-1):
                for k in xrange(len(self.box[0,0,:])-1):    
                    s += np.abs(self.xString[i+1,j,k]-self.xString[i,j,k] + self.zString[i,j,k+1]-self.zString[i,j,k] + self.yString[i,j+1,k]-self.yString[i,j,k])  
        print "S = ",s              
    
    def check_num_strings(self):
        num = 0
        n0 = 0
        n1 = 0
        n2 = 0
        n3 = 0
        for i in xrange(len(self.box[:,0,0])-1):
            for j in xrange(len(self.box[0,:,0])-1):
                for k in xrange(len(self.box[0,0,:])-1):    
                    num = np.abs(self.xString[i+1,j,k])+np.abs(self.xString[i,j,k]) + np.abs(self.zString[i,j,k+1])+np.abs(self.zString[i,j,k]) + np.abs(self.yString[i,j+1,k])+np.abs(self.yString[i,j,k])  
                    if (num == 0):
                        n0 += 1
                    elif (num == 2):
                        n1 += 1
                    elif (num ==4):
                        n2 += 1
                    elif (num ==6):
                        n3 += 1
                    else:
                        print "ERROR"
        print "n0 = ",n0  
        print "n1 = ",n1 
        print "n2 = ",n2 
        print "n3 = ",n3                                                                                                                                                                                                                                                                                                               
        
    def trackStrings(self):
        self.edge = True
        self.trackEdge() #Infinite Strings
        self.edge = False
        self.trackCentre() #Closed Strings
        
    def trackEdge(self):
        """Z-Edges"""
        for j in xrange(len(self.box[0,:,0])-1):
            for i in xrange(len(self.box[:,0,0])-1):
                k = 0
                if (self.zString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.zString,i,j,k)    
                    self.length.append(self.L)                                  
                k = N-1
                if (self.zString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.zString,i,j,k)
                    self.length.append(self.L)  
        """Y-Edges"""    
        for k in xrange(len(self.box[0,0,:])-1):
            for i in xrange(len(self.box[:,0,0])-1):   
                j = 0    
                if (self.yString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.yString,i,j,k) 
                    self.length.append(self.L)                                   
                j = N-1
                if (self.yString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.yString,i,j,k)
                    self.length.append(self.L)  
        """X-Edges"""    
        for j in xrange(len(self.box[0,:,0])-1):
            for k in xrange(len(self.box[0,0,:])-1):    
                i = 0    
                if (self.xString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.xString,i,j,k)  
                    self.length.append(self.L)                                   
                i = N-1
                if (self.xString[i,j,k] == 1):
                    """Follow"""
                    self.L=0
                    self.follow(self.xString,i,j,k)
                    self.length.append(self.L)  

                      
    def trackCentre(self):
        for i in xrange(1,len(self.box[:,0,0])-2):
            for j in xrange(1,len(self.box[0,:,0])-2):
                for k in xrange(1,len(self.box[0,0,:])-2):
                    if (self.zString[i,j,k] == 1):
                        """Follow"""
                        self.L=0
                        self.follow(self.zString,i,j,k)
                        self.length.append(self.L)  
                    if (self.yString[i,j,k] == 1):
                        """Follow"""
                        self.L=0
                        self.follow(self.yString,i,j,k)
                        self.length.append(self.L)  
                    if (self.xString[i,j,k] == 1):
                        """Follow"""
                        self.L=0
                        self.follow(self.xString,i,j,k)
                        self.length.append(self.L)  
                          
    def follow(self,xyz,i,j,k): 
        #Edge == True means looking for infinite strings
        #Edge == False means looking for closed strings
        n_i,n_j,n_k = self.followFunc(i,j,k)
        """Statement below equivalent? if (self.edge==False and n_i==i and n_j==j and n_k ==k):""" 
        if (self.edge==False and xyz[n_i,n_j,n_k] == 0): #if reach the starting point for a closed string -> stop 
            return
        if (self.edge==True and n_i==N-1 or n_j==N-1 or n_k ==N-1): #if reach the edge for infite strings -> stop 
            return
        else: 
            self.L += 1
            xyz[i,j,k]=0
            self.follow(xyz,i,j,k)
    
    def followFunc(self,i,j,k):
        #Virginia's Code
        return i,j,k
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
N = 5
lattice = SpaceCube(N)
lattice.xPlane()
lattice.yPlane()
lattice.zPlane()

#print lattice.yString
#print lattice.xString
#print lattice.zString
#PrintPnF(0,0,0)
lattice.check_in_out_equal()
lattice.check_num_strings()
print "Probability = ", (1.0 * lattice.total)/(1.0*lattice.faceNum)

lattice.trackStrings()




