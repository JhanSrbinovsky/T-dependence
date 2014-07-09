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
            self.T_ref = 25.0
            self.Temperature = [] 
    
    class GlobalDefs(object):
        def __init__(self):
            self.nx = 100 
            self.Tmin = 0.0
            self.Tmax = 360.0
       
    # insert a break from the CLI for reading output
    print "\n"
  
    #instantiate class
    indies = Independents( )
    globs = GlobalDefs()
    
    ## Call global_data 
    SetIndependents( indies, globs )
    print '\n Temperature: ', indies.Temperature 
    print '\n T_ref: ', indies.T_ref
    
    ## Call function 
    ##function(arg, arg )
   


################################################################################
if __name__ == "__main__":
   main(sys.argv[1:])

################################################################################


