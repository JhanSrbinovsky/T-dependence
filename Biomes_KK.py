import numpy as np
import math as m

def Set_biomes( nBiomes, bi, nPlants, pl ): 
   
   # first average over plants
   Vcmax_25_tot = 0.
   H_a_tot = 0.
   DeltaS_tot = 0.
 
   Vcmax_25_bi = np.zeros(nBiomes) 
   H_a_bi      = np.zeros(nBiomes)
   DeltaS_bi   = np.zeros(nBiomes)

   for ll in range( nPlants ):
      Vcmax_25_tot = pl.Vcmax_25[ll] + Vcmax_25_tot
      H_a_tot = pl.H_a[ll] + H_a_tot
      DeltaS_tot = pl.DeltaS[ll] + DeltaS_tot
      
      if( pl.BiNumber[ll] == 1 ):
         Vcmax_25_bi[0] = pl.Vcmax_25[ll] + Vcmax_25_bi[0]
         H_a_bi[0]      = pl.H_a[ll] + H_a_bi[0]
         DeltaS_bi[0]   = pl.DeltaS[ll] + DeltaS_bi[0]
   
      if( pl.BiNumber[ll] == 2 ):
         Vcmax_25_bi[1] = pl.Vcmax_25[ll] + Vcmax_25_bi[1]
         H_a_bi[1]      = pl.H_a[ll] + H_a_bi[1]
         DeltaS_bi[1]   = pl.DeltaS[ll] + DeltaS_bi[1]
      
      if( pl.BiNumber[ll] == 3 ):
         Vcmax_25_bi[2] = pl.Vcmax_25[ll] + Vcmax_25_bi[2]
         H_a_bi[2]      = pl.H_a[ll] + H_a_bi[2]
         DeltaS_bi[2]   = pl.DeltaS[ll] + DeltaS_bi[2]
      
   # Average over all plants
   Vcmax_25_av_pl = Vcmax_25_tot / nPlants
   H_a_av_pl = H_a_tot / nPlants
   DeltaS_av_pl = DeltaS_tot / nPlants

   # Average over biomes 
   for lb in range( nBiomes ):
      Vcmax_25_bi[lb] = Vcmax_25_bi[lb] / nPlants
      H_a_bi[lb]      = H_a_bi[lb] / nPlants
      DeltaS_bi[lb]   = DeltaS_bi[lb] / nPlants
   
   # KK use PFT dependent Vcmax, Jmax and these fit values for others
   for i in range( nBiomes ):
      bi[0].Vcmax_25[i] = Vcmax_25_bi[i]
      bi[0].H_a[i] = 72.0 *1000.0 #+/- 3.3 (kJ) 
      bi[0].DeltaS[i] = 649.0 #+/- 1.43
      bi[0].H_d[i] = 200000.
   
#jhan: pass this back for plotting
#1: plot raw data sets
#2: plot av over plants
#3: plot av over biomes 
#4: plot what KK have

#my contention is that mixing plant averaged parameters,biome averaged parameters 

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
       
 
