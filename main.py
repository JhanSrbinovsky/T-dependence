#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespcei. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 
import matplotlib.pyplot as plt

#import local, application specific modules
from Tdep_KK_main import Tdep_KK_main

HowManyModels = 2

# Set domain model[0].x: Leaf Temperature (Kelvin) 
# with nx grads from Tmin:Tmax
T0_degC = 277.13
Tmin0_decC = 0.
Tmax0_decC = 40.
Tmin0 = Tmin0_decC + T0_degC 
Tmax0 = Tmax0_decC + T0_degC 
nT_L = 100
nBiomes_KK = 3 
nPlants_KK =  54 


#commented to run interactively
#def main(argv):
    
class Models(object):
   def __init__(self):
      self.x = np.zeros(nT_L) 
      self.y = np.zeros( (nBiomes_KK, nT_L) ) # assumes1:1 mapping b/n x&y

class Constants(object):
   def __init__(self):
      self.R_gas = 8.314462175    # Universal Gas Constant 

# insert a break from the CLI for reading output
print "\n"

# instantiate classes
#######################

K = Constants()    

model= []
for i in range(HowManyModels):
   model.append( Models() )

########################
#
# Set domain of Leaf Temperature (Kelvin) with nx grads from Tmin:Tmax
model[0].x = np.linspace(Tmin0, Tmax0, nT_L)
#print model[0].x

## call model(s)
########################
Tdep_KK_main( model[0].x, model[0].y, model[1].y, K, nBiomes_KK, nPlants_KK )
########################
#
## plot model(s)
########################
#
## plot generically x against y
##plot_generic( model[0].x, model[0].y )
##import pylab as pl
x= model[0].x - T0_degC 
y= model[0].y[0]

#x= np.array( range(20))
#y=x 
#y = np.model[0].y

#plt.plot( x, y, 'bo' )
#plt.show()

#######################

#if running purely as a script from the command line
################################################################################
#if __name__ == "__main__":
#   main(sys.argv[1:])

################################################################################


