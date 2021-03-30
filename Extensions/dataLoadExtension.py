# -*- coding: utf-8 -*-
"""
Extension for data loading functions
"""
import numpy as np
from displayMenuExtension import *
def dataLoad(filename):
    
    """
    Created on Thu Oct 29 12:27:00 2020
    
    Loads data from the file 'filename' into the variable 'data'.
    
    Parameters
    ----------
    1. filename : string 
                 the path to the specific file containing the data
    
    Returns
    -------
    data : numpy array with dimensions N*3
            the matrix containing only specified correct values 
    
    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    
    """
    
    #Opening the file and reading the lines into an array
    filein = open(filename,"r")
    lines = filein.readlines()
    data = []
    
    #Iterating through the lines and splitting the string into 3 floats
    for i in range(len(lines)):
        
        values = lines[i].split()
    
        #Error Handling for the 3 types of values
        if not checkType(
                values[0],float) or checkType(
                    values[0], float) and (
                        float(values[0]) < 10 or float(values[0]) > 60):
            print("Line {} ".format(i))
            print("Error: INVALID Temperature (*must be within range 10-60)")
            print("Found -> {} ".format(values[0]))
            continue
        
        if not checkType(
                values[1],float) or checkType(
                    values[1], float) and float(values[1]) < 0:
            print("Line {} ".format(i))
            print("Error: INVALID Growth Rate (*must be positive)")
            print("Found -> {} ".format(values[1]))
            continue
        
        if not checkType(
                values[2],int) or checkType(
                    values[2], int) and (int(
                        values[2]) < 1 or int(values[2]) > 4):
            print("Line {} ".format(i))
            print("Error: INVALID Bacteria Type (*must be in range 1-4)")
            print("Found -> {} ".format(values[2]))
            continue
        
        #Rendering the type of values into cells
        values[0] = float(values[0])
        values[1] = float(values[1])
        values[2] = int(values[2])
        #The first line becomes the first row of the matrix data
        if (i == 0):
            data = np.array(values)
        #Vertical stacking to form the final matrix data
        else: 
            data = np.vstack((data,np.array(values)))
            
    return data 

