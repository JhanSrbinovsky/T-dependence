#!/usr/bin/python 

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
import numpy as np 
import sys
#import pylab as pl

#import local, application specific modules
from Tdep_KK_funcs import Tdep_KK_func
from Biomes_KK import Set_biomes
from Speices_KK import Set_plants
from DataSet import Read_dataset

def Tdep_KK_main( T_leaf, Vcmax, Jcmax, K, nBiomes, nPlants, ifile ):

   # insert a break from the CLI for reading output
   print "\n"
   
   # f^n, model parameter: Vcmax_25 reference, normalization Temperature
   T_ref = 277.13 + 25. # 25 deg-C #hardwired 0 deg-C (K)
  
   Read_dataset( nPlants, nBiomes, ifile )

#########################################################################

 # KK(2007) actually gives values per plant
   class PlantDepParams_KK(object):
      def __init__(self):
         self.PlNumber = np.zeros( nPlants ) 
         self.BiNumber = np.zeros( nPlants ) 
         self.Vcmax_25 = np.zeros( nPlants ) 
         self.Jmax_25  = np.zeros( nPlants ) 
         self.H_a      = np.zeros( nPlants )    # activation energy
         self.H_d      = np.zeros( nPlants )    # de-activation energy
         self.DeltaS   = np.zeros( nPlants )    # Entropy factor
    
   class BiomeDepParams_KK(object):
      def __init__(self):
         self.BiNumber = np.zeros( nPlants ) 
         self.Vcmax_25 = np.zeros( nBiomes ) 
         self.Jmax_25  = np.zeros( nBiomes ) 
         self.H_a      = np.zeros( nBiomes )    # activation energy
         self.H_d      = np.zeros( nBiomes )    # de-activation energy
         self.DeltaS   = np.zeros( nBiomes )    # Entropy factor
    
#########################################################################
  
   # instantiate classes: for plants
   pl = []
   pl = PlantDepParams_KK()

   # Set Plant dependent PArameters
   Set_plants( nPlants, nBiomes, pl ) 


   sys.exit()
   # BiomeIndex is the plants per biome in the KK dataset
   # jhan: implement more consistet way of doing this 
   BiomeIndex = np.zeros( nBiomes ) 
   BiomeIndex[0] = 17 - 0
   BiomeIndex[1] = 26 - 18
   BiomeIndex[2] = 53 - 27

#########################################################################
  
   bi = []
   for i in range( nBiomes ):
      bi.append( BiomeDepParams_KK() )
   Set_biomes( nBiomes, bi, nPlants, pl, BiomeIndex ) 
   
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   
   # Kmax = K_25 * f(T_leaf) [ described by fn_T_L here ]

   # eveluate f(T_leaf) per biome 
   fn_T_L = np.zeros((nBiomes, len( T_leaf ) ))

   ## Call function 
   for j in range( nBiomes ):
      for i in range( len( T_leaf ) ):
         fn_T_L[j][i] = Tdep_KK_func( j, T_leaf[i], T_ref, K.R_gas, bi,pl )
  
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   for j in range( nBiomes ):
      for i in range( len( T_leaf ) ):
         Vcmax[j][i]= bi[j].Vcmax_25 * fn_T_L[j][i]
         print "Vcmax_25 ", bi[j].Vcmax_25
         # normalized by Vcmax_25 per Biome
         Vcmax[j][i]= fn_T_L[j][i]
         #print "Vcmax ", Vcmax[j][i]
         #print "V_25 ", bi[j].Vcmax_25
         #print "fn ", fn_T_L[j][i]
  
   #for i in range( nBiomes):
   #   for j in range( len( T_leaf ) ):
   #      Vcmax = Vcmax_25[i] * fn_T_L[j]


################################################################################



























