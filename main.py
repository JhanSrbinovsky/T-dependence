#!/usr/bin/python
__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 
#import pylab as pl

#import local, application specific modules
from GlobalDataModule import SetIndependents
#from module_func import function 


def main(argv):
    
    # Declare global data
    
    class Independents(object):
        def __init__(self):
            # Check per line "label" in configfile defining the type
            # of the following argument 
    #        self.ClassArray =  [ "egName", "egPath" ]
    #        # Declare ClassArray as mutable here so can be modified 
    #        # by a called function:
            self.np.Temperature = []
            self.T_ref 
    
    # insert a break from the CLI for reading output
    print "\n"
  
    # Call global_data 
    SetIndependents( Independents )
    print '\n Temperature: ', Independents.Temperature 
    print '\n T_ref: ', Independents.T_ref
    
    # Call function 
    #function(arg, arg )
   


################################################################################
if __name__ == "__main__":
   main(sys.argv[1:])

################################################################################


