#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespcei. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 

#import local, application specific modules
from Tdep_KK_main import Tdep_KK_main

HowManyModels = 2

#commented to run interactively
#def main(argv):
    
class Models(object):
   def __init__(self):
      self.x = []
      self.y = []

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

#######################

# Set domain of Leaf Temperature (Kelvin) with nx grads from Tmin:Tmax
Tmin = 290. 
Tmax = 330.
nx = 10

model[0].x = np.linspace(Tmin, Tmax, nx)


# call model(s)
#######################
Tdep_KK_main( model[0].x, model[0].y, model[1].y, K )
#######################

# plot model(s)
#######################
#plotT-dep_KK( model[1].x, model[1].y )

#######################

#if running purely as a script from the command line
################################################################################
#if __name__ == "__main__":
#   main(sys.argv[1:])

################################################################################


