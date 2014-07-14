
def Set_plants( nPlants, pl ): 
   # KK(2007) actually gives values per plant
   class PlantDepParams_KK(object):
      def __init__(self):
         self.Vcmax_25 = 0. 
         self.Jmax_25  = 0. 
         self.H_a      = 0.      # activation energy
         self.H_d      = 0.      # de-activation energy
         self.DeltaS   = 0.      # Entropy factor
 
   for i in range( nPlants):
      pl.append( PlantDepParams_KK() )

   print "Set Plants "   
