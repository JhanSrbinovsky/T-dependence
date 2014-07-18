#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespce. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 
import matplotlib.pyplot as plt

#import local, application specific modules
from Tdep_KK_main import Tdep_KK_main
from DataSet import Read_dataset

# End python header
#########################################################################

# GLOBAL model parmeters

HowManyModels  = 2

# Set domain model[0].x: Leaf Temperature (Kelvin) 
# with nT_L grads from Tmin:Tmax
nT_L = 100
nBiomes_max = 20
# 0 deg-C in K
T0C_degK = 277.13

# model uses Kelvin but plots in degress-C
Tmin0_degC = 0.; Tmax0_degC = 40.
Tmin0 = Tmin0_degC + T0C_degK 
Tmax0 = Tmax0_degC + T0C_degK 

# End Model Header
#########################################################################

# commented to run interactively
#def main(argv):

# GLOBAL decs so cn bring back various model data to here and manipulate

# class containing x & y data to plot    
class Models(object):
   def __init__(self):
      self.x = np.zeros(nT_L) 
      self.y = np.zeros( (nBiomes_max, nT_L) ) # assumes1:1 mapping b/n x&y

# class containing constants 
class Constants(object):
   def __init__(self):
      self.R_gas = 8.314462175    # Universal Gas Constant 

# End global class declarations
#########################################################################

# instantiate classes

K = Constants()    

model= []
for i in range(HowManyModels):
   model.append( Models() )

# Set domain of Leaf Temperature (Kelvin) with nx grads from Tmin:Tmax
model[0].x = np.linspace(Tmin0, Tmax0, nT_L)

#########################################################################

# insert a break from the CLI for reading output
print "\n"

# Model 1 - KK T-dependence

# Fix nBiomes[0], nPlants[0] from dataSet
nBiomes     = [] 
nPlants     = [] 

# Dataset to read 
ifile = "KK_dataset.txt"

# call model(s)

# KK Temperature dependence model
Tdep_KK_main( model[0].x, model[0].y, model[1].y, K, nBiomes, nPlants, ifile )

sys.exit()

#########################################################################

# plot model(s)

# plot generically x against y
#plot_generic( model[0].x, model[0].y )


# plot First Biome, T-dependence KK 
x= model[0].x - T0C_degK 
y= model[0].y[0]     #this is first dim(biome)=0
plt.plot( x, y, '-', linewidth=1 )

# plot Second Biome, T-dependence KK 
y= model[0].y[1]     #this is first dim(biome)=1
plt.plot( x, y, 'r-', linewidth=1 )
#plt.plot( x, y, 'rs' )

# plot Third Biome, T-dependence KK 
y= model[0].y[2]     #this is first dim(biome)=2
plt.plot( x, y, 'g-', linewidth=1 )
#plt.plot( x, y, 'go' )

plt.show()

#######################

#if running purely as a script from the command line
################################################################################
#if __name__ == "__main__":
#   main(sys.argv[1:])

################################################################################


