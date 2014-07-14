import numpy as np
import math as m

def Set_biomes( nBiomes, bi, nPlants, pl, BiomeIndex ): 

   # KK(2007) actually gives values per plant
   class BiomeDepParams_KK(object):
      def __init__(self):
         self.Vcmax_25 = 0. 
         self.Jmax_25  = 0. 
         self.H_a      = 0.      # activation energy
         self.H_d      = 0.      # de-activation energy
         self.DeltaS   = 0.      # Entropy factor

   for i in range( nBiomes ):
      bi.append( BiomeDepParams_KK() )

   # in first instance just use PFT dependent Vcmax, Jmax
   # average these per biome, ??more consistent than using values
   # derived elsewhere
   # use biome averaged parameters for others
   i = 0
   bi[i].Vcmax_25 = 78.2 
   
   bi[i].H_a = 72.0 *1000.0 #+/- 3.3 (kJ) 
   bi[i].DeltaS = 649.0 #+/- 1.43
   bi[i].H_d = 200000.
   
###############################################################
   # compute average Vcmax_25 per biome

   dummy = np.zeros(int(BiomeIndex[0])) 
   for i in range( int(BiomeIndex[0]) ):
      dummy[i] = pl[i].Vcmax_25
   bi[0].Vcmax_25 = m.fsum( dummy ) / BiomeIndex[0]
   print "", bi[0].Vcmax_25



   #for i in range( BiomeIndex[0] ):
   #sum(pl.Vcmax_25)     
   #print bi[i].Vcmax_25  
   
   #bi[i].Jmax_25 = 1.

   #bi[i].rjV = 1.97 #+/- 0.07
   
   # Jmax    
   # Jmaxbi[i].H_a = 50.0 *1000.0 #+/- 2.4 
   # Jmaxbi[i].DeltaS = 646.0 #+/- 1.66
   # Jmaxbi[i].H_d = 200000.
       
 
