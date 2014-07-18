import math as m
import numpy as np

###############################################################################

def Tdep_KK_func( i, T_L, T_ref, R_gas, bi, pl ):
   
   # Activation moderated by deactivation
   
   # Activation 
   ####################
   DeltaT = T_L - T_ref
   
   Eff_activ  = bi[i].H_a * DeltaT 
   norm_activ = T_ref * T_L * R_gas
   Activation = Tdep_KK_funcExpFuncs( Eff_activ, norm_activ )
   
   # Deactivation: ratio b/n ref & leaf
   ####################
   
   # _ref Temperature
   Entropy_ref =  ( T_ref  * bi[i].DeltaS ) - bi[i].H_d
   norm_ref = R_gas * T_ref
   Deactiv_ref = 1. + Tdep_KK_funcExpFuncs( Entropy_ref, norm_ref )
   
   # leaf Temperature
   Entropy_leaf = ( T_L * bi[i].DeltaS ) - bi[i].H_d
   norm_leaf = R_gas * T_L
   Deactiv_leaf = 1. + Tdep_KK_funcExpFuncs( Entropy_ref, norm_ref )
  
   fn_T_L =  Activation * Deactiv_ref / Deactiv_leaf
   
   return fn_T_L

###############################################################################

def Tdep_KK_funcExpFuncs( numer, denom ):
   #print "Tdep_KK_funcExpFuncs"
   term = m.exp( numer/denom )
   #print term
   return term 

###############################################################################

  
###############################################################################

def Set_pl( pl ):
   print "Set_pl"

###############################################################################

