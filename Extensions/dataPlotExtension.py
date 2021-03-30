# -*- coding: utf-8 -*-
"""
Extension for data plotting functions
"""

import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    
    """
    Created on Thu Oct 29 17:27:00 2020
    
    Plots the requested graphs in regards to given data.
    Plots are showed in the Plots section.
    
    Parameters
    ----------
    1. data : numpy array of N*3
                 the matrix containing the data
     
    
    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    """
    # First plot - Number of Bacteria
    # Creating the array with bacteria type names
    names = []
    
    if np.size(data)/3==1:
        if (data[0][2] == 1):
            names.append('Salmonella enterica')
        elif (data[0][2] == 2):
            names.append('Bacillus cereus')
        elif (data[0][2] == 3):
            names.append('Listeria')
        else:
            names.append('Brochotrix thermosphacta')
    else:
        for i in range(int(np.size(data)/3)):
            if (data[i][2] == 1):
                names.append('Salmonella enterica')
            elif (data[i][2] == 2):
                names.append('Bacillus cereus')
            elif (data[i][2] == 3):
                names.append('Listeria')
            else:
                names.append('Brochotrix thermosphacta')
    
    #Plotting the histogram - Number of Bacteria
    plt.title("Number of bacteria")
    plt.xlabel("Bacteria Type")
    plt.ylabel("Number")
    plt.hist(names,color="green", ec="red", align="mid", histtype="stepfilled")
    plt.grid()
    plt.show()
    
    #Second plot - Growth rate by temperature 
    if np.size(data)/3==1:
        btyp = int(data[0][2])
        plt.title("Growth rate by temperature")
        #Plotting the 4 graphs - Growth rate by temperature 
        plt.scatter(data[0][0],data[0][1],color='red')
        print(names)
        plt.legend(names,loc="best")
        plt.xlim([10,60])
        plt.ylim([0,1])
        plt.xlabel("Temperature")
        plt.ylabel("Growth rate")
        plt.show()
        
    else:
        btyp = data[:,2]
        #Creating a matrix for each specific bacteria type
        #Sorting the matrix by temperatures conserving the rows
        typei = [[],[],[],[]]
    
        for i in range(4):
            typei[i] = data[btyp == i+1]
            typei[i] = typei[i][typei[i][:,0].argsort()]
          
    
        plt.title("Growth rate by temperature")
        #Plotting the 4 graphs - Growth rate by temperature 
        colors = ["red","purple","orange","green"]
        lines = ['--','-.','-','-']
        for i in range(4):
            plt.plot(typei[i][:, 0], typei[i][:, 1],ls=lines[i],color=colors[i])
        
        plt.legend(['Salmonella enterica','Bacillus cereus','Listeria','Brochotrix thermosphacta'],loc="best")
        plt.xlim([10,60])
        plt.ylim([0,1])
        plt.xlabel("Temperature")
        plt.ylabel("Growth rate")
        plt.show()
    
    