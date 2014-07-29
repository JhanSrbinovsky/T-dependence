#!/usr/bin/python

import numpy as np

show_plot = False


# 0 deg-C in K
T0C_degK = 277.13

nT_L = 100; n_max = 200
# class containing x & y data to plot    
class Models(object):
   def __init__(self):
      self.x = np.zeros(nT_L) 
      self.y = np.zeros( (n_max, nT_L) ) # assumes1:1 mapping b/n x&y

# class containing constants 
class Constants(object):
   def __init__(self):
      self.R_gas = 8.314462175    # Universal Gas Constant 

#########################################################################

nPlants_max = 1000 
nBiomes_max = 1000 
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
    
# instantiate classes: for plants
pl = []
bi = []
#########################################################################
 
# End global class declarations

