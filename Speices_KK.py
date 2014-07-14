
def Set_plants( nPlants, pl ): 
   #print "Set Plants "   
   
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
    
   # Biome 1 - broadleaf trees and shrubs
   pl[0].Vcmax_25 = 78.2
   pl[1].Vcmax_25 = 37.8  
   pl[2].Vcmax_25 = 68.3  
   pl[3].Vcmax_25 = 101.9 
   pl[4].Vcmax_25 = 33.6  
   pl[5].Vcmax_25 = 90.4  
   pl[6].Vcmax_25 = 17.3  
   pl[7].Vcmax_25 = 24.7  
   pl[8].Vcmax_25 = 25.7 
   pl[9].Vcmax_25 = 62.8  
   pl[10].Vcmax_25 = 27.5  
   pl[11].Vcmax_25 = 76.3  
   pl[12].Vcmax_25 = 77.1  
   pl[13].Vcmax_25 = 62.3  
   pl[14].Vcmax_25 = 66.2  
   pl[15].Vcmax_25 = 86.9  
   pl[16].Vcmax_25 = 95.1  
   pl[17].Vcmax_25 = 42.3  
   # Biome 2 - Coniferous trees 
   pl[18].Vcmax_25 = 43.5  
   pl[19].Vcmax_25 = 64.8  
   pl[20].Vcmax_25 = 51.8  
   pl[21].Vcmax_25 = 61.5  
   pl[22].Vcmax_25 = 92.4  
   pl[23].Vcmax_25 = 85.9  
   pl[24].Vcmax_25 = 99.2  
   pl[25].Vcmax_25 = 67.3  
   pl[26].Vcmax_25 = 57.7  
   # Biome 3 - Herbaceous plants 
   pl[27].Vcmax_25 = 157.5  
   pl[28].Vcmax_25 = 170.8  
   pl[29].Vcmax_25 = 187.1  
   pl[30].Vcmax_25 = 127.1  
   pl[31].Vcmax_25 = 196.6  
   pl[32].Vcmax_25 = 162.1  
   pl[33].Vcmax_25 = 50.2  
   pl[34].Vcmax_25 = 77.0  
   pl[35].Vcmax_25 = 67.8  
   pl[36].Vcmax_25 = 130.2  
   pl[37].Vcmax_25 = 152.8  
   pl[38].Vcmax_25 = 93.9  
   pl[39].Vcmax_25 = 90.2  
   pl[40].Vcmax_25 = 49.2  
   pl[41].Vcmax_25 = 53.8  
   pl[42].Vcmax_25 = 57.2  
   pl[43].Vcmax_25 = 186.0  
   pl[44].Vcmax_25 = 192.6  
   pl[45].Vcmax_25 = 200.7  
   pl[46].Vcmax_25 = 165.0  
   pl[47].Vcmax_25 = 123.1  
   pl[48].Vcmax_25 = 128.2  
   pl[49].Vcmax_25 = 45.7  
   pl[50].Vcmax_25 = 38.3  
   pl[51].Vcmax_25 = 50.9  
   pl[52].Vcmax_25 = 205.2  
   pl[53].Vcmax_25 = 174.4  
   
   
   #pl[0].Jmax_25  = 0. 
   #pl[0].H_a      = 0.      # activation energy
   #pl[0].H_d      = 0.      # de-activation energy
   #pl[0].DeltaS   = 0.      # Entropy factor
