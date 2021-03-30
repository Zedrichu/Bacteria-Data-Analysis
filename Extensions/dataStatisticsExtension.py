# -*- coding: utf-8 -*-
"""
Extension for data statistics functions
"""

import numpy as np

def dataStatistics(data,statistic):
    
    """
    Created on Thu Oct 29 14:20:43 2020
    
    Return the specified statistic regarding values in data

    Parameters
    ----------
    data : numpy array N*3 
            the matrix containing data values for the computation
    statistic : string
                the specific name for the computation
                'Mean Temperature'
                'Mean Growth rate'
                'Std Temperature'
                'Std Growth rate'
                'Rows'
                'Mean Cold Growth rate'
                'Mean Hot Growth rate'
    Returns
    -------
    result : numeric
            the specified computation result
            
            
    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen 
    """
    #Using the nested if-elif statements and numpy functions ...
    #...the statistic specified as parameter is computed
    if (statistic == 'Mean Temperature'):
        result = np.mean(data[ :, 0])
        
    elif (statistic == 'Mean Growth rate'):
        result = np.mean(data[ :, 1])
        
    elif (statistic == 'Std Temperature'):
        result = np.std(data[ :, 0])
        
    elif (statistic == 'Std Growth rate'):
        result = np.std(data[ :, 1])
    
    elif (statistic == 'Rows'):
        result = np.size(data) / 3
    
    elif (statistic == 'Mean Cold Growth rate'):
        # grt is the array of growth rate values
        # tem is the array of temperature values
        grt = data[ :, 1]
        tem = data[ :, 0]
        result = np.mean(grt[tem < 20.0])
    
    elif (statistic == 'Mean Hot Growth rate'):    
        # grt is the array of growth rate values
        # tem is the array of temperature values
        grt = data[ :, 1]
        tem = data[ :, 0]
        result = np.mean(grt[tem > 50.0])
    
    return result
