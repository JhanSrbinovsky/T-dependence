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
from Tdep_KK import Tdep_KK_func, Set_bi

def Tdep_KK_main( T_leaf, Vcmax, Jcmax, K ):

   T_ref = 277.13 + 25. # reference temp. at 25 deg-C
   HowManyBiomes = 2 

   # KK(2007) actually gives values per plant
   class BiomeDepParams_KK(object):
      def __init__(self):
         #self.Vcmax_25 = [] 
         #self.Jmax_25  = [] 
         self.H_a      = []         # activation energy
         self.H_d      = []         # de-activation energy
         self.DeltaS   = []         # Entropy factor
   
   # insert a break from the CLI for reading output
   print "\n"
   #print "T_leaf ", T_leaf 
   #print "K ", K.R_gas
   
   ##instantiate classes
   ########################
   bi = []
   #pl = []
   
   for i in range( HowManyBiomes):
      bi.append( BiomeDepParams_KK() )
   #   pl.append( PlantDepParams_KK() )
   
   ########################
   
   # Set Biome dependent PArameters
   for i in range( HowManyBiomes):
      Set_bi( i,bi)

   # Vcmax & Jmax described by KK(2007) Eq.(1)
   
   # Kmax = K_25 * f(T_leaf) [ described by fn_T_L here ]

   # in the first instance eveluat f(T_leaf) and use prescribed values of K_25

   fn_T_L = []
   
   ### Call function 
   for i in range( len( T_leaf ) ):
      fn_T_L.append( Tdep_KK_func( 1, T_leaf[i],T_ref, K.R_gas, bi ) )

   
##if running purely as a script from the command line
#################################################################################
##if __name__ == "__main__":
##   main(sys.argv[1:])
#
################################################################################


