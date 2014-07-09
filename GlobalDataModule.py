
#import python modules
import numpy as np 

def SetIndependents( Independents ):
    
    # Temperatures in Kelvin
    Independents.T_ref= 25.0 
    Independents.Temperature = np.linspace(0,360,100)
     
    print '\n Temperature: ', Independents.Temperature 

 
