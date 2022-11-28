# By: Tim Tarver also known as CryptoKeyPlayer

# This script is to demonstrate how to visualize data
# from a CSV file in the realm of Machine Learning

# Best viewed running in Jupyter Notebooks; one method per cell. 

import matplotlib.pyplot as plt
import pandas

# We begin by reading the provided csv file to see what is in it!

def __init__(self, vehicles):

    self.vehicles = vehicles
    return vehicles

# Now, we will plot the data via Relationship, Distribution, Comparison & Composition Visualization!
# --------------------------------------------------------------------------------------------------   

# This method plots the Relationship Visualization via Scatter Plot

def relationship_visualization(): 

    vehicles = pandas.read_csv("vehicles.csv")
    vehicles.head()
    plot1 = vehicles.plot(kind = 'scatter', x = 'citympg', y = 'co2emissions')
    return vehicles, plot1

# This method plots the Distribution Visualization of CO-2 Emissions via Histogram

def distribution_visualization():

    vehicles = pandas.read_csv("vehicles.csv")
    vehicles.head()
    plot2 = vehicles['co2emissions'].plot(kind = 'hist')
    return vehicles, plot2
    
# This method prints the Comparison Visualization comparing different drives.

def comparison_visualization():

    vehicles = pandas.read_csv("vehicles.csv")
    vehicles.head()
    plot3 = vehicles.pivot(columns = 'drive', values = 'co2emissions')
    plot4 = vehicles.pivot(columns =  'drive', values = 'co2emissions').plot(kind = 'box',
                                                                             figsize = (10, 6))
    return vehicles, plot3, plot4

# This method will print the Composition Visualization via Box plot.

def composition_visualization():

    vehicles = pandas.read_csv("vehicles.csv")
    vehicles.head()
    plot5 = vehicles.groupby('year')['drive'].value_counts()
    plot6 = vehicles.groupby('year')['drive'].value_counts().unstack()
    plot7 = vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind = 'bar',
                                                                            stacked = True,
                                                                            figsize = (10, 6))
    return vehicles, plot5, plot6, plot7
    

    
# By the way, make sure each print line has its own cell as well (Jupyter Notebooks)        
print(relationship_visualization())
print(distribution_visualization())
print(comparison_visualization())
print(composition_visualization())

    
