
#import python modules
import numpy as np 

def SetIndependents( indies, GD ):
    
    # Temperatures in Kelvin
    #Tmin = GlobalDefs.Tmin 
    #Tmax = GlobalDefs.Tmax 
    #nx = GlobalDefs.n
   
    indies.Temperature = np.linspace(GD.Tmin, GD.Tmax, GD.nx)
     
    #print '\n Temperature: ', indies.Temperature 

 
