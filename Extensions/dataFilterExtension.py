# -*- coding: utf-8 -*-
"""
Extension for data filtering functions
"""


import numpy as np
from displayMenuExtension import *

def dataFilter(data,prevFilter,filtString):
    """
    Created on Thu Oct 29 20:54:05 2020

    Filters the data stored in matrix by temperature or growth rate range or
    selection of a certain bacteria type
    
    Parameters:
    --------------
    1. data - numpy array N*3
                stores the data in a matrix
    2. prevFilter - bool vector
                    stores the previous filter condition
    3. filtString - string
                    contains previously defined filter message

    Returns:
    1. newFilter - numpy array of bool 
                stores the bool condition vector for further use
    2. filtString - string
                    contains the filter message to be displayed in submenus

    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen
    """
    
    
    
    #Menu selection for the kind of filter user wants to create
    menuFilter = ['Bacteria Type','Temperature Range',
                  'Growth Rate Range','Reset Filter']
    
    choice = displayMenu(menuFilter)
    
    if choice == 1:
        #Applying Bacteria Type filter
        #Another menu selection for the specific name of the bacteria
        menuBacteria = ['Salmonella enterica','Bacillus cereus',
                        'Listeria','Brochotrix thermosphacta']
        btype = displayMenu(menuBacteria)
        
        #Bacteria type row
        bac = data[:, 2]
        #Generating the filter condition as a bool vector
        newFilter = (bac == btype)
        filtString += "Filter Applied : Bacteria = {}".format(menuBacteria[btype-1]) + '\n'
        
    elif choice == 2:
        #Applying Temperature Range filter
        lim1 = inputValue("Please enter the lower limit for temperature ")
        lim2 = inputValue("Please enter the upper limit for temperature ")
        #Temperature row
        temp = data[:, 0]
        #Generating filter condition
        newFilter = np.logical_and( temp >= lim1 , temp <= lim2)
        filtString += "Filter Applied : {} <= Temperature => {}".format(lim1,lim2) + '\n'
    
    elif choice == 3:
        #Applying Growth Rate Range filter
        lim1 = inputValue("Please enter the lower limit for growth rate ")
        lim2 = inputValue("Please enter the upper limit for growth rate ")
        #Growth rate row
        grt = data[:, 1]
        #Generating filter condition
        newFilter = np.logical_and( grt >= lim1 , grt <= lim2)
        filtString += "Filter Applied : {} <= Growth rate => {}".format(lim1,lim2) + '\n'
        
    elif choice == 4:
        #Resetting the filter so it includes all rows
        newFilter = np.ones(np.shape(data)[0],dtype=bool)
        print ("Filter Reset - all rows displayed")
        filtString = ""
        return (newFilter,filtString)
        
    #Combining the previously applied filter with the newly created one
    newFilter = (newFilter & prevFilter)        
    return (newFilter,filtString)