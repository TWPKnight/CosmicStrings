"""
RHUL PH4100 - Major Project
Cosmic Strings
Started: 14/10/2017
Tom Hyatt & Virginia d'Emilio
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint 

N = 10
box = np.zeros((N,N,N))
for i in range(len(box[:,0,0])):
    for j in range(len(box[0,:,0])):
        for k in range(len(box[0,0,:])):
            box[i,j,k] = randint(0,2)
print box
