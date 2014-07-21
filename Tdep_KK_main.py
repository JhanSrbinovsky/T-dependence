#!/usr/bin/python 

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
import numpy as np 
import sys
import matplotlib.pyplot as plt

#import local, application specific modules
from Tdep_KK_funcs import Tdep_KK_func, Tdep_KK_func_pl
from Biomes_KK import Set_biomes
from Speices_KK import Set_plants
from DataSet import Read_dataset
from main_data import PlantDepParams_KK, BiomeDepParams_KK
from main_data import pl, bi, T0C_degK 
from main_data import nPlants_max, nBiomes_max 

def Tdep_KK_main( T_leaf, Vcmax, Vcmax_KK_Bi, K, nBiomes, nPlants, ifile, Vcmax_KK_pl ):
 
   # insert a break from the CLI for reading output
   print "\n"
   
   # f^n, model parameter: Vcmax_25 reference, normalization Temperature
   T_ref = 277.13 + 25. # 25 deg-C #hardwired 0 deg-C (K)

   # Declare mutable object => lines read from config file
   nlines = []
   data = Read_dataset( nlines, ifile )
 
   # instantiate classes: for plants
   #pl = []
   pl = PlantDepParams_KK()

   # hardwired 0 ~ bc 0th model here
   # Set Plant dependent PArameters
   nPlants.append( Set_plants( nlines[0], nBiomes, pl, data ) )
   #print nPlants[0]

#########################################################################
   nmethods = 3
   #bi = []
   for i in range( nmethods):
      bi.append( BiomeDepParams_KK() )
   
   Set_biomes( nBiomes[0], bi, nPlants[0], pl ) 
   
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   
   # Kmax = K_25 * f(T_leaf) [ described by fn_T_L here ]

   # eveluate f(T_leaf) per biome 
   fn_T_L = np.zeros((nBiomes[0], len( T_leaf ) ))

   ## Call function defiining Temperature dependence 
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         fn_T_L[j][i] = Tdep_KK_func( j, T_leaf[i], T_ref, K.R_gas, bi, pl )
  
#########################################################################

   # Vcmax & Jmax described by KK(2007) Eq.(1)
   # normalized by Vcmax_25 per Biome
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax_KK_Bi[j][i]= fn_T_L[j][i]
   # this will endure over following plots = leaf temperature
   x = T_leaf - T0C_degK

   plt.title('KK - per biome')
   plt.ylabel('Vcmax/Vcmax_25')
   y1= Vcmax_KK_Bi[0]
   plt.plot(x, y1, 'g-', linewidth=1 )
   
   plt.show()

#########################################################################

   # Vcmax & Jmax described by KK(2007) Eq.(1)
   # NOT normalized by Vcmax_25 per Biome
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax_KK_Bi[j][i]= bi[0].Vcmax_25[j] * fn_T_L[j][i]
   
   plt.title('KK - per biome')
   plt.ylabel('Vcmax')
   
   y1= Vcmax_KK_Bi[0]
   plt.plot(x, y1, 'r-', linewidth=1 )

   y1= Vcmax_KK_Bi[1]
   plt.plot(x, y1, 'b-', linewidth=1 )

   y1= Vcmax_KK_Bi[2]
   plt.plot(x, y1, 'g-', linewidth=1 )

   plt.show()
  
#########################################################################

   # eveluate f(T_leaf) per plant 
   gn_T_L = np.zeros((nPlants[0], len( T_leaf ) ))

   for j in range( nPlants[0] ):
      for i in range( len( T_leaf ) ):
         gn_T_L[j][i] = Tdep_KK_func_pl( j, T_leaf[i], T_ref, K.R_gas, bi,pl )
  
   # Vcmax per plant 
   for j in range( nPlants[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax_KK_pl[j][i]= pl.Vcmax_25[j] * gn_T_L[j][i]

   # plot Vcmax per plant in first Biome group 
   for j in range ( 0,14 ):
      y3= Vcmax_KK_pl[j]
      plt.plot(x, y3, 'r-', linewidth=1 )
      
   # generic desc of T-dependece
   y1= Vcmax_KK_Bi[0]
   plt.plot(x, y1, 'g-', linewidth=2 )
   
   plt.show()
 
   # plot Vcmax per plant in 2nd Biome group 
   for j in range ( 15,23 ):
      y3= Vcmax_KK_pl[j]
      plt.plot(x, y3, 'r-', linewidth=1 )
      
   # generic desc of T-dependece
   y1= Vcmax_KK_Bi[1]
   plt.plot(x, y1, 'g-', linewidth=2 )
   
   plt.show()
 
   # plot Vcmax per plant in first Biome group 
   for j in range ( 24,47 ):
      y3= Vcmax_KK_pl[j]
      plt.plot(x, y3, 'r-', linewidth=1 )
      
   # generic desc of T-dependece
   y1= Vcmax_KK_Bi[2]
   plt.plot(x, y1, 'g-', linewidth=2 )
   
   plt.show()
   
   
    
   # Vcmax & Jmax described by KK(2007) Eq.(1)
   #for j in range( nBiomes[0] ):
   #j=99
   #for i in range( len( T_leaf ) ):
   #   Vcmax[j][i]= bi[0].Vcmax_25[j] * fn_T_L[j][i]
   #   # normalized by Vcmax_25 per Biome
 
   #for i in range( len( T_leaf ) ):
   #   print "Vcmax_25 ", Vcmax[2][i] -  Vcmax[1][i]

   #for i in range( nBiomes):
   #   for j in range( len( T_leaf ) ):
   #      Vcmax = Vcmax_25[i] * fn_T_L[j]


################################################################################



























   # Vcmax & Jmax described by KK(2007) Eq.(1)
   for j in range( nBiomes[0] ):
      for i in range( len( T_leaf ) ):
         Vcmax_KK_Bi[j][i]= bi[0].Vcmax_25[j] * fn_T_L[j][i]
         # normalized by Vcmax_25 per Biome
         #Vcmax_KK_Bi[j][i]= fn_T_L[j][i]
  
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

   # Vcmax & Jmax described by KK(2007) Eq.(1)
   #for j in range( nBiomes[0] ):
   #j=99
   #for i in range( len( T_leaf ) ):
   #   Vcmax[j][i]= bi[0].Vcmax_25[j] * fn_T_L[j][i]
   #   # normalized by Vcmax_25 per Biome
 
   #for i in range( len( T_leaf ) ):
   #   print "Vcmax_25 ", Vcmax[2][i] -  Vcmax[1][i]

   #for i in range( nBiomes):
   #   for j in range( len( T_leaf ) ):
   #      Vcmax = Vcmax_25[i] * fn_T_L[j]


################################################################################



























