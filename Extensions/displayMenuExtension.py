# -*- coding: utf-8 -*-
"""
Extension with UI Utilities for the main script

"""

#Source code found in the python modules book and used as extension

"""
INPUTNUMBER Prompts user to input a number

Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
 number. Repeats until user inputs a valid number.

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015

---------------------------------------------------------------------------

DISPLAYMENU Displays a menu of options, ask the user to choose an item
 and returns the number of the menu item chosen.

Usage: choice = displayMenu(options)

Input options Menu options (array of strings)
Output choice Chosen option (integer)

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015

"""
#Source code **********
import numpy as np

def inputNumber(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Error: Please enter a number as your choice")
            print()
            pass
    return num


def displayMenu(options):
    
    print("Menu: ")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1,options[i]))
    
    choice = 0
    
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
        print()
    return choice 
#******************
    
#Other functions created for the interface 
def inputStat(prompt):
    """
    Gets the user input to find the chosen statistic option

    Parameters
    ------------
    1. prompt : string
            text to be displayed when asking for statistic option
            @author: Adrian Zvizdenco & Felix Aertebjerg
    """
    #Gets the user's choice for statistic option
    options = np.array(['Mean Temperature','Mean Growth rate',
                        'Std Temperature','Std Growth rate','Rows',
                        'Mean Cold Growth rate','Mean Hot Growth rate'])
    choice = displayMenu(options)
    return options[choice-1]

def inputValue(prompt):
    """
    Gets the user to input a valid number value
    
    Parameters:
        prompt : string
                text to be displayed when asking for value
                
    Returns:
        num : float
            valid value for further computing
    @author: Zvizdenco Adrian
    """
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Error: Please enter a number as value")
            print()
            pass
    return num


def inputFilename(prompt):
    """
    Gets the user input for a valid relative file path

    Parameters:
        prompt : string
                text to be displayed when asking for a filename
    ------------d
    Returns:
        filepath : string
                    contains the relative path of the file
    @author: Adrian Zvizdenco & Emilie Hansen
    """
    while True:
        try:
            #If file opens without any exception raised it exits the loop
            filepath = input(prompt)
            file = open(filepath,"r")
            break
        except FileNotFoundError:
            #If file doesn't open properly the user input is prompted again
            print("Error:Invalid relative path to the main script entered")
            print()
            pass
    #The valid path is returned so it can load data
    return filepath

def checkType(var,type):
    """
    Checks if value stored in var is of certain type 'type'

    Parameters:
        var : value to be checked
        type : type to be checked
    ------------
    Returns:
        bool : value True - if valid and False otherwise
    @author: Adrian Zvizdenco 
    """
    try:
        if (type == float):
            float(var)
        elif (type == int):
            int(var)
        return True

    except ValueError:
        return False
    