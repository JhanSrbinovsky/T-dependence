#!/usr/bin/python 

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
import numpy as np 
import sys
#import pylab as pl

#import local, application specific modules
from Tdep_KK_funcs import Tdep_KK_func, Tdep_KK_func_pl
from Biomes_KK import Set_biomes
from Speices_KK import Set_plants
from DataSet import Read_dataset

def Tdep_KK_main( T_leaf, Vcmax, Vcmax_KK_Bi, K, nBiomes, nPlants, ifile, Vcmax_KK_pl ):
   nPlants_max = 1000 
   nBiomes_max = 1000 
   # insert a break from the CLI for reading output
   print "\n"
   
   # f^n, model parameter: Vcmax_25 reference, normalization Temperature
   T_ref = 277.13 + 25. # 25 deg-C #hardwired 0 deg-C (K)

   # Declare mutable object => lines read from config file
   nlines = []
   data = Read_dataset( nlines, ifile )

#########################################################################

 # KK(2007) actually gives values per plant
   class PlantDepParams_KK(object):
      def __init__(self):
         self.PlNumber = np.zeros( nPlants_max ) 
         self.BiNumber = np.zeros( nPlants_max ) 
         self.Vcmax_25 = np.zeros( nPlants_max ) 
         self.Jmax_25  = np.zeros( nPlants_max ) 
         self.H_a      = np.zeros( nPlants_max )    # activation energy
         self.H_d      = np.zeros( nPlants_max )    # de-activation energy
         self.DeltaS   = np.zeros( nPlants_max )    # Entropy factor
    
   class BiomeDepParams_KK(object):
      def __init__(self):
         self.BiNumber = np.zeros( nPlants_max ) 
         self.Vcmax_25 = np.zeros( nBiomes_max ) 
         self.Jmax_25  = np.zeros( nBiomes_max ) 
         self.H_a      = np.zeros( nBiomes_max )    # activation energy
         self.H_d      = np.zeros( nBiomes_max )    # de-activation energy
         self.DeltaS   = np.zeros( nBiomes_max )    # Entropy factor
    
#########################################################################
  
   # instantiate classes: for plants
   pl = []
   pl = PlantDepParams_KK()

   # hardwired 0 ~ bc 0th model here
   # Set Plant dependent PArameters
   nPlants.append( Set_plants( nlines[0], nBiomes, pl, data ) )

#########################################################################
   nmethods = 3
   bi = []
   for i in range( nmethods):
      bi.append( BiomeDepParams_KK() )
   
   Set_biomes( nBiomes[0], bi, nPlants[0], pl ) 
   
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   
   # Kmax = K_25 * f(T_leaf) [ described by fn_T_L here ]

   # eveluate f(T_leaf) per biome 
   fn_T_L = np.zeros((nBiomes[0], len( T_leaf ) ))

   ## Call function 
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         fn_T_L[j][i] = Tdep_KK_func( j, T_leaf[i], T_ref, K.R_gas, bi,pl )
  
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax[j][i]= bi[0].Vcmax_25[j] * fn_T_L[j][i]
         # normalized by Vcmax_25 per Biome
         Vcmax_KK_Bi[j][i]= fn_T_L[j][i]
         #print "Vcmax ", Vcmax[j][i]
         #print "V_25 ", bi[0].Vcmax_25[j]
         #print "V_25 ", pl.Vcmax_25[i]
         #print "fn ", fn_T_L[j][i]
  
   # eveluate f(T_leaf) per biome 
   gn_T_L = np.zeros((nPlants[0], len( T_leaf ) ))

   ## Call function 
   for j in range( nPlants[0] ):
      for i in range( len( T_leaf ) ):
         gn_T_L[j][i] = Tdep_KK_func_pl( j, T_leaf[i], T_ref, K.R_gas, bi,pl )
  
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   for j in range( nPlants[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax_KK_pl[j][i]= pl.Vcmax_25[j] * gn_T_L[j][i]

   #for i in range( len( T_leaf ) ):
   #   print "Vcmax_25 ", Vcmax[2][i] -  Vcmax[1][i]

   #for i in range( nBiomes):
   #   for j in range( len( T_leaf ) ):
   #      Vcmax = Vcmax_25[i] * fn_T_L[j]


################################################################################



























