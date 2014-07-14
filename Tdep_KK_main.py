#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespcei. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
#import sys
import numpy as np 
#import pylab as pl

#import local, application specific modules
from GlobalDataModule import SetIndependents
from Tdep_KK import Tdep_KK

def Tdep_KK_main(T_leaf,Vcmax,Jcmax,K ):

   # KK(2007) actually gives values per plant
   class BiomeDepParams_KK(object):
      def __init__(self):
         self.T_ref_25 = 277.13 + 25.
         self.Vcmax_25 = [] 
         self.Jmax_25  = [] 
         self.H_a      = []         # activation energy
         self.H_d      = []         # de-activation energy
         self.DeltaS   = []         # Entropy factor
   
   ## KK(2007) actually gives values per plant
   #class PlantDepParams_KK(object):
   #   def __init__(self):
   #      self.H_a       = []         # activation energy
   #      self.H_d       = []         # de-activation energy
   #      self.DeltaS    = []         # Entropy factor
   
   
   # insert a break from the CLI for reading output
   print "\n"
   print "T_leaf ", T_leaf 
   print "K ", K.R_gas
   
   ##instantiate classes
   ########################
   #bi = []
   #pl = []
   #
   ## there only needs be a single instance of these
   #K = Constants()    
   #gl = GlobalDefs()
   #
   ## array for instances of model
   ##model = []
   #
   ##arrays of X () instantiated classes
   ##for i in range(gl.nIndeps):
   ##   ins.append( Independents() )
   #ins = Independents() 
   #
   #for i in range(gl.nParConfigs):
   #   bi.append( BiomeDepParams_KK() )
   #   pl.append( PlantDepParams_KK() )
   #
   ########################
   #
   ### Call function 
   #Tdep_KK( ins, K, bi, pl )
   #   
   #
   #
##if running purely as a script from the command line
#################################################################################
##if __name__ == "__main__":
##   main(sys.argv[1:])
#
################################################################################


