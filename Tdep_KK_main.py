#!/usr/bin/python 

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
#import sys
import numpy as np 
#import pylab as pl

#import local, application specific modules
from Tdep_KK_funcs import Tdep_KK_func, Set_bi

def Tdep_KK_main( T_leaf, Vcmax, Jcmax, K, nBiomes, nPlants ):

   T_ref = 277.13 + 25. # reference temp. at 25 deg-C

   # KK(2007) actually gives values per plant
   class BiomeDepParams_KK(object):
      def __init__(self):
         self.Vcmax_25 = 0. 
         self.Jmax_25  = 0. 
         self.H_a      = 0.      # activation energy
         self.H_d      = 0.      # de-activation energy
         self.DeltaS   = 0.      # Entropy factor

   class PlantDepParams_KK(object):
      def __init__(self):
         self.Vcmax_25 = 0. 
         self.Jmax_25  = 0. 
         self.H_a      = 0.      # activation energy
         self.H_d      = 0.      # de-activation energy
         self.DeltaS   = 0.      # Entropy factor
   
   # insert a break from the CLI for reading output
   print "\n"
   
   ##instantiate classes
   ########################
   bi = []
   pl = []
   
   for i in range( nBiomes):
      bi.append( BiomeDepParams_KK() )

   for i in range( nPlants):
      pl.append( PlantDepParams_KK() )
   
   ########################
   
   # Set Biome dependent PArameters
   for j in range( nBiomes):
      Set_bi( j, bi)

   # Vcmax & Jmax described by KK(2007) Eq.(1)
   
   # Kmax = K_25 * f(T_leaf) [ described by fn_T_L here ]

   # in the first instance eveluat f(T_leaf) and use prescribed values of K_25

   fn_T_L = np.zeros((nBiomes, len( T_leaf ) ))

   ## Call function 
   for j in range( nBiomes ):
      for i in range( len( T_leaf ) ):
         #fn_T_L.append( Tdep_KK_func( j, T_leaf[i], T_ref, K.R_gas, bi ) )
         fn_T_L[j][i] = Tdep_KK_func( j, T_leaf[i], T_ref, K.R_gas, bi,pl )
  
   #print "fn_T_L", type(fn_T_L) 
   #print "fn_T_L", fn_T_L[0] 
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   for j in range( nBiomes ):
      for i in range( len( T_leaf ) ):
         Vcmax[j][i]= bi[j].Vcmax_25 * fn_T_L[j][i]
         Vcmax[j][i]= fn_T_L[j][i]
         #print "Vcmax ", Vcmax[j][i]
         #print "V_25 ", bi[j].Vcmax_25
         #print "fn ", fn_T_L[j][i]
  
   #for i in range( nBiomes):
   #   for j in range( len( T_leaf ) ):
   #      Vcmax = Vcmax_25[i] * fn_T_L[j]


################################################################################



























