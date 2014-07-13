import math as m
#assume only one bi, pl etc

###############################################################################

def Tdep_KK( ins, K, bi, pl ):
 
   #print "Tdep_KK"
   Set_bi( bi)
   #Set_pl( pl )
   
   fn_T_leaf = []
   
   for i in range(len(ins.T_leaf)):
      fn_T_leaf.append( Tdep_KK_func( i, ins.T_leaf[i], K.R_gas, 
                                              bi ) )

   #V_cmax = V_cmax25 * fn_T_leaf 
   #J_cmax = J_cmax25 * fn_T_leaf 

###############################################################################

def Tdep_KK_func( i, T_leaf, R_gas, bi ):
   
   # Activation moderated by deactivation
   ####################
   
   # Activation 
   DeltaT = T_leaf - bi[1].T_ref_25
   
   Eff_activ  = bi[1].H_a * DeltaT 
   norm_activ = bi[1].T_ref_25 * T_leaf * R_gas
   Activation = Tdep_KK_funcExpFuncs( Eff_activ, norm_activ )
   
   # Deactivation: ratio b/n ref & leaf
   
   #_ref Temperature
   Entropy_ref =  ( bi[1].T_ref_25  * bi[1].DeltaS ) - bi[1].H_d
   norm_ref = R_gas * bi[1].T_ref_25
   Deactiv_ref = 1. + Tdep_KK_funcExpFuncs( Entropy_ref, norm_ref )
   
   #leaf Temperature
   Entropy_leaf = ( T_leaf    * bi[1].DeltaS ) - bi[1].H_d
   norm_leaf = R_gas * T_leaf
   Deactiv_ref = 1. + Tdep_KK_funcExpFuncs( Entropy_ref, norm_ref )
   
   #print "T-leaf T_ref ",  bi[1].T_ref_25


###############################################################################

def Tdep_KK_funcExpFuncs( numer, denom ):
   #print "Tdep_KK_funcExpFuncs"
   #print "exp ", R_gas, T_leaf 
   term = m.exp( numer/denom )
   #print term
   return term 

###############################################################################

def Set_bi( bi ):
   #print "Set_bi"
   bi[1].Vcmax_25 = 1. 
   bi[1].Jmax_25 = 1.

   bi[1].H_a = 1.
   bi[1].H_d = 1.
   bi[1].DeltaS = 1.
       
   
###############################################################################

def Set_pl( pl ):
   print "Set_pl"

###############################################################################

