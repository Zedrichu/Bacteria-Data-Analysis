"""
    The main script of the project.
    The user interface is created here.
    Functionalities are located in the Extensions folder and imported in 
        the main script.
    The testing file for data loading is currently located in
        the Bacteria folder.
    (*)For future use place the file containing data in Bacteria folder 
        and use the path ./Bacteria/*filename*.txt or place it in the same
            folder as the main script and use the path *filename*.txt !!!
    
    HAVE FUN!
    
    @author: Adrian Zvizdenco & Felix Aertebjerg & Emilie Hansen 
"""
#Initialization of path and imports
import sys
sys.path.append('.')
sys.path.append('./Extensions')
import dataLoadExtension as dtload
import dataStatisticsExtension as dtstat
import numpy as np
import dataPlotExtension as dtplt
import dataFilterExtension as dtfilter
import displayMenuExtension as displayUI

#Are you ready?

print("Welcome to Bacteria Data Analysis!")


filterStr = ""
menuItems = np.array(['Load Data','Filter Data',
                      'Display Statistics','Generate Plots','Display Filtered Data','Quit'])
while True:
    choice = displayUI.displayMenu(menuItems)
    if choice == 1:
        print('Loading data procedure...')
        print('------------------------------')
        #Obtain valid path and load data
        path = displayUI.inputFilename("Enter relative path to file ")
        data = dtload.dataLoad(path)
        
        if (data == []):
            print("No valid data entered")
            continue
        
        #Initializing filter as entirely true
        
        filterCond = np.ones(np.shape(data)[0],dtype=bool)
        print ("Data loaded successfully.")
        print ('________________________________________')
                
        while True:
            choice = displayUI.displayMenu(menuItems)
            if choice == 1:
                print ("Reloading data....")
                print ("----------------------------")
                #Obtain valid path and reload data
                path = displayUI.inputFilename("Enter relative path to file ")
                data = dtload.dataLoad(path)

                #Initializing filter as entirely true
                filterCond = np.ones(np.shape(data)[0],dtype=bool)
                print ("Data reloaded successfully.")
                print ('________________________________________')
                
            elif choice == 2:
                print ("Filtering data....")
                print ("-----------------------")
                #Filtering data
                filtSolution = dtfilter.dataFilter(data,filterCond,filterStr) 
                filterCond = filtSolution[0]
                filterStr = filtSolution[1]
                print ("Data filtered successfully ")
                print (filterStr)
                print ("_______________________________________")
                
            elif choice == 3:
                print ("Displaying statistics....")
                print ("-----------------------")
                #Computing Statistics
                statistic = displayUI.inputStat("Choose a statistic option ")
                print (filterStr)
                print ("The result is ",
                       dtstat.dataStatistics(data[filterCond],statistic))
                print ("Display successful")
                print ("_______________________________________")
                
            elif choice == 4:
                print ("Generating the plots....")
                print ("-----------------------")
                #Generating Plots
                dtplt.dataPlot(data[filterCond])
                print (filterStr)
                print ("Plots generated successfully")
                print ("_______________________________________")
            
            elif choice == 5:
                print("Displaying data from the matrix :")
                print (filterStr)
                print(data[filterCond])
                print("Data displayed successfully")
                print("________________________________________")
            elif  choice == 6:
                print("Quitting the program.")
                print('_______________________________________')
                print("Thanks for using the program!")
                break
        break
        
    elif choice == 6:
        print("Quitting the program.")
        print('__________________________________')
        print("Thanks for using the program!")
        break
    
    else:
        print("Error : No data loaded. Please choose option 1 or quit!")
        print()