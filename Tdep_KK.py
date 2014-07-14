import math as m
#assume only one bi, pl etc

###############################################################################

def Tdep_KK_func( i, T_L, T_ref, R_gas, bi ):
   
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
   Deactiv_ref = 1. + Tdep_KK_funcExpFuncs( Entropy_ref, norm_ref )
  
   fn_T_L =  Activation * Entropy_ref / Deactiv_ref 
   
   return fn_T_L

###############################################################################

def Tdep_KK_funcExpFuncs( numer, denom ):
   #print "Tdep_KK_funcExpFuncs"
   term = m.exp( numer/denom )
   #print term
   return term 

###############################################################################

def Set_bi( i,bi ):
   #print "Set_bi"
   #bi[1].Vcmax_25 = 1. 
   #bi[1].Jmax_25 = 1.

   bi[i].H_a = 84917.
   bi[i].H_d = 200000.
   bi[i].DeltaS = 648.2
       
   
###############################################################################

def Set_pl( pl ):
   print "Set_pl"

###############################################################################

