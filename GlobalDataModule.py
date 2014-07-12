
#import python modules
import numpy as np 

def SetIndependents( ins, gl ):
    
    # Temperatures in Kelvin
    #Tmin = GlobalDefs.Tmin 
    #Tmax = GlobalDefs.Tmax 
    #nx = GlobalDefs.n
   
    ins.Temperature = np.linspace(gl.Tmin, gl.Tmax, gl.nx)
    #ins(1).Temperature = np.linspace(gl.Tmin, gl.Tmax, gl.nx)
     
    #print '\n Temperature: ', ins(1).Temperature 

 
