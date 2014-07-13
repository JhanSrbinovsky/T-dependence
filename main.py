#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespcei. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 
import pylab as pl

#import local, application specific modules
from GlobalDataModule import SetIndependents
from Tdep_KK import Tdep_KK

#def main(argv):
    
# Declare global data

class GlobalDefs(object):
   def __init__(self):
      self.nIndeps = 10           #defines number of model configs
      self.nParConfigs = 100       #defines number of model configs
      self.nx = 10                #defines gradiation of model
      self.Tmin = 280.0
      self.Tmax = 330.0

class Constants(object):
   def __init__(self):
      self.R_gas = 8.314462175    # Universal Gas Constant 

class Independents(object):
   def __init__(self):
      self.T_leaf = []   # leaf temperature. set array of nx vals in 
                             # range(Tmin,Tmax)

# KK(2007) actually gives values per plant
class BiomeDepParams_KK(object):
   def __init__(self):
      self.T_ref_25 = 277.13 + 25.
      self.Vcmax_25 = [] 
      self.Jmax_25  = [] 
      self.H_a      = []         # activation energy
      self.H_d      = []         # de-activation energy
      self.DeltaS   = []         # Entropy factor

# KK(2007) actually gives values per plant
class PlantDepParams_KK(object):
   def __init__(self):
      self.H_a       = []         # activation energy
      self.H_d       = []         # de-activation energy
      self.DeltaS    = []         # Entropy factor


# insert a break from the CLI for reading output
print "\n"

#instantiate classes
#######################
ins = []
bi = []
pl = []

# there only needs be a single instance of these
K = Constants()    
gl = GlobalDefs()

# array for instances of model
#model = []

#arrays of X () instantiated classes
#for i in range(gl.nIndeps):
#   ins.append( Independents() )
ins = Independents() 

for i in range(gl.nParConfigs):
   bi.append( BiomeDepParams_KK() )
   pl.append( PlantDepParams_KK() )

#######################


## Call global_data 
SetIndependents( ins, gl )

## Call function 
Tdep_KK( ins, K, bi, pl )
   


#if running purely as a script from the command line
################################################################################
#if __name__ == "__main__":
#   main(sys.argv[1:])

################################################################################


