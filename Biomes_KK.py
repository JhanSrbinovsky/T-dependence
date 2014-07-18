import numpy as np
import math as m

def Set_biomes( nBiomes, bi, nPlants, pl, BiomeIndex ): 

   # in first instance just use PFT dependent Vcmax, Jmax
   # average these per biome, ??more consistent than using values
   # derived elsewhere
   # use biome averaged parameters for others
   
   for i in range( nBiomes ):
      bi[i].Vcmax_25 = 78.2 
      bi[i].H_a = 72.0 *1000.0 #+/- 3.3 (kJ) 
      bi[i].DeltaS = 649.0 #+/- 1.43
      bi[i].H_d = 200000.
   
###############################################################
   # compute average Vcmax_25 per biome
   #for i in range( nPlants ):
   sum_bi = np.zeros( nBiomes )
   sum_bi[0:] =0.
   for i in range( nPlants ):
      if(i >= 0 and i <=17 ):
         sum_bi[0] =  sum_bi[0] + pl.Vcmax_25[i]
      if(i >= 18 and i <=26 ):
         sum_bi[1] =  sum_bi[1] + pl.Vcmax_25[i]
      if(i >= 27 and i <=53 ):
         sum_bi[2] =  sum_bi[2] + pl.Vcmax_25[i]
       
   for i in range( nBiomes ):
      bi[i].Vcmax_25 = sum_bi[i] / BiomeIndex[i]
      print "Vcmax_25 ", bi[i].Vcmax_25
   
   print sum_bi[0]
   print sum_bi[1]
   print sum_bi[2]
   #av_bi1=  sum_bi1 / 17 - 0
   #av_bi2=  sum_bi2 / 26 -18
   #av_bi3=  sum_bi3 / 53 -27

   #dummy = np.zeros(int(BiomeIndex[0])) 
   #for i in range( int(BiomeIndex[0]) ):
   #   dummy[i] =    #bi[0].Vcmax_25 = m.fsum( dummy ) / BiomeIndex[0]
   ##print "", bi[0].Vcmax_25
   #dummy = np.zeros(int(BiomeIndex[1])) 
   #for i in range( int(BiomeIndex[0]:int(BiomeIndex[1]) ):
   #   dummy[i] = pl[i].Vcmax_25
   #bi[1].Vcmax_25 = m.fsum( dummy ) / BiomeIndex[1]
   ##print "", bi[0].Vcmax_25
   #dummy = np.zeros(int(BiomeIndex[2])) 
   #for i in range( int(BiomeIndex[2]) ):
   #   dummy[i] = pl[i].Vcmax_25
   #bi[2].Vcmax_25 = m.fsum( dummy ) / BiomeIndex[2]
   #print "", bi[0].Vcmax_25



   #for i in range( BiomeIndex[0] ):
   #sum(pl.Vcmax_25)     
   #print bi[i].Vcmax_25  
   
   #bi[i].Jmax_25 = 1.

   #bi[i].rjV = 1.97 #+/- 0.07
   
   # Jmax    
   # Jmaxbi[i].H_a = 50.0 *1000.0 #+/- 2.4 
   # Jmaxbi[i].DeltaS = 646.0 #+/- 1.66
   # Jmaxbi[i].H_d = 200000.
       
 
