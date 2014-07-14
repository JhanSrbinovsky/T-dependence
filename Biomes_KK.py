
def Set_biomes( nBiomes, bi, nPlants, pl ): 

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

   bi[i].Vcmax_25 = 78.2 
   #bi[i].Jmax_25 = 1.

   #bi[i].rjV = 1.97 #+/- 0.07
   
   bi[i].H_a = 72.0 *1000.0 #+/- 3.3 (kJ) 
   bi[i].DeltaS = 649.0 #+/- 1.43
   bi[i].H_d = 200000.

   # Jmax    
   # Jmaxbi[i].H_a = 50.0 *1000.0 #+/- 2.4 
   # Jmaxbi[i].DeltaS = 646.0 #+/- 1.66
   # Jmaxbi[i].H_d = 200000.
       
 
