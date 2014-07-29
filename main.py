#!/usr/bin/python #-i
# use -i here to drop into innteractive mode t end of script
# and preserve namespce. have to comment out below as well

__author__ = 'Jhan Srbinovsky'

# main program governing project to do .... 

# usage:

#import python modules
import sys
import numpy as np 
import matplotlib.pyplot as plt

#import local, application specific modules
from Tdep_KK_main import Tdep_KK_main
from DataSet import Read_dataset

# End python header
#########################################################################

# GLOBAL model parmeters

HowManyModels  =3 

# Set domain model[0].x: Leaf Temperature (Kelvin) 
# with nT_L grads from Tmin:Tmax
from main_data import nT_L, n_max 

# model uses Kelvin but plots in degress-C
from main_data import T0C_degK 
Tmin0_degC = 0.; Tmax0_degC = 50.
Tmin0 = Tmin0_degC + T0C_degK 
Tmax0 = Tmax0_degC + T0C_degK 

# End Model Header
#########################################################################

# commented to run interactively
#def main(argv):

# GLOBAL decs so cn bring back various model data to here and manipulate
from main_data import Models, Constants 
from main_data import pl, bi 

#########################################################################

# instantiate classes

K = Constants()    

model= []
for i in range(HowManyModels):
   model.append( Models() )

# Set domain of Leaf Temperature (Kelvin) with nx grads from Tmin:Tmax
model[0].x = np.linspace(Tmin0, Tmax0, nT_L)

#########################################################################

# insert a break from the CLI for reading output
print "\n"

# Model 1 - KK T-dependence

# Dataset to read 
ifile = "KK_dataset.txt"

# call model(s)

# KK Temperature dependence model
#Tdep_KK_main( model[0].x, model[0].y, model[1].y, K, nBiomes, nPlants, ifile, \
#model[2].y)
Tdep_KK_main( model[0].x, ifile, K )

#########################################################################

from Tdep_CABLE import T_dep_CABLE_C3 
T_dep_CABLE_C3( model[0].x, ifile, K ) 

















#
## plot model(s)
#
## plot generically x against y
##plot_generic( model[0].x, model[0].y )
#
## plot KK instance for T-dependence - averaged params other than PFT dep. Vcmax 
#x= model[0].x - T0C_degK
#
#y1= model[1].y[0]      
##y1= np.log(model[1].y[0] )     
#plt.subplot(3, 1, 1)
#plt.plot(x, y1, 'g-', linewidth=1 )
#plt.title('KK - per biome')
#plt.ylabel('Vcmax/Vcmax_25')
#
## broadleaf
#y2= model[0].y[0]     
#plt.subplot(3, 1, 2)
#plt.plot(x, y2, 'g-', linewidth=1 )
#
##coniferous
#y2= model[0].y[1]     
#plt.subplot(3, 1, 2)
#plt.plot(x, y2, 'r-', linewidth=1 )
#
##herbaceous
#y2= model[0].y[2]     
#plt.subplot(3, 1, 2)
#plt.plot(x, y2, 'b-', linewidth=1 )
#
#y3= model[2].y[0]     
#plt.subplot(3, 1, 3)
#plt.plot(x, y3, 'b-', linewidth=1 )
#
#y3= model[2].y[1]     
#plt.subplot(3, 1, 3)
#plt.plot(x, y3, 'b-', linewidth=1 )
#
#y3= model[2].y[2]     
#plt.subplot(3, 1, 3)
#plt.plot(x, y3, 'b-', linewidth=1 )
#
##for i in range ( nPlants[0] ):
#for i in range ( 17 ):
#   y3= model[2].y[i]     
#   plt.subplot(3, 1, 3)
#   plt.plot(x, y3, 'b-', linewidth=1 )
#
#y2= model[1].y[0]  * bi[0].Vcmax_25[0]    
#plt.subplot(3, 1, 3)
#plt.plot(x, y2, 'r-', linewidth=1 )
#
###for i in range ( nPlants[0] ):
##j =99
##y3= model[2].y[j]     
##plt.subplot(3, 1, 3)
##plt.plot(x, y3, 'y-', linewidth=1 )
##
#plt.xlabel('Leaf Temperature (deg C)')
#plt.ylabel('Vcmax')
#
#plt.show()
#
#########################################################################


#plt.plot( x, y, 'bd' )
#
#
##this is first dim(biome)=0
#y= model[0].y[0]     
#plt.plot( x, y, '-', linewidth=1 )
#
##sys.exit()
## plot Second Biome, T-dependence KK 
#y= model[0].y[1]     #this is first dim(biome)=1
#plt.plot( x, y, 'r-', linewidth=1 )
#
###plt.plot( x, y, 'rs' )
#
## plot Third Biome, T-dependence KK 
#y= model[0].y[2]     #this is first dim(biome)=2
#plt.plot( x, y, 'g-', linewidth=1 )
###plt.plot( x, y, 'go' )
#
#
#plt.show()
#######################

#if running purely as a script from the command line
################################################################################
#if __name__ == "__main__":
#   main(sys.argv[1:])

################################################################################


