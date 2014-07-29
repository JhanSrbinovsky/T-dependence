#!/usr/bin/python 

# main program governing iT-dependence Kattage & Knorr (KK) 

# usage: called from main

#import python modules
import numpy as np 
import sys
import matplotlib.pyplot as plt

from main_data import nBiomes_max,  T0C_degK

################################################################################

#def xvcmxt3(x): 
def T_dep_CABLE_C3(x, ifile, K): 
   
   #  leuning 2002 (p c & e) equation for temperature response
   #  used for vcmax for c3 plants
   xvcnum = np.zeros( nBiomes_max )
   xvcden = np.zeros( nBiomes_max )
   #z
 
   ehavc  = 73637.0  #! J/mol (Leuning 2002)
   ehdvc  = 149252.0 #! J/mol (Leuning 2002)
   entropvc = 486.0  #! J/mol/K (Leuning 2002)
   xvccoef = 1.17461 #! derived parameter
                     # xVccoef=1.0+exp((EntropJx*C%TREFK-EHdJx)/(Rconst*C%TREFK))
 
   xvcnum = xvccoef * np.exp( ( ehavc / ( K.R_gas*298.2 ) )* ( 1.-298.2/x ) )
   xvcden = 1.0 + np.exp( ( entropvc*x-ehdvc ) / ( K.R_gas*x ) )
   #z = max( 0.0,xvcnum / xvcden )
   z = (xvcnum / xvcden) * (12.e-7) 

   xp = x -  T0C_degK

   plt.title('CABLE - Temperature dependence ')
   plt.xlabel('T_leaf')
   plt.ylabel('f(T_leaf)')
   y1= z 
   plt.plot(xp, y1, 'g-', linewidth=1 )
   
   #if show_plot is True:   
   plt.show()


################################################################################

#! Explicit array dimensions as temporary work around for NEC inlining problem
#FUNCTION xvcmxt4(x) RESULT(z)
#   
#   REAL, PARAMETER      :: q10c4 = 2.0
#   REAL, INTENT(IN) :: x
#   REAL :: z
# 
#   z = q10c4 ** (0.1 * x - 2.5) /                                              &
#        ((1.0 + exp(0.3 * (13.0 - x))) * (1.0 + exp(0.3 * (x - 36.0))))
# 
#END FUNCTION xvcmxt4
#


