import numpy as np

def Set_plants( nPlants, nBiomes, pl, lines ): 
   print "Set Plants "   
   
   # Loop over all of these read lines
   for ll in range( nPlants ):

      # Create a string from each line
      lstr = str(lines[ll])
      # nullify case sensitivity in that string
      lstr = lstr.lower()

      # if it is meant to be interpreted - interpret based on what
      # it starts with. See configfile example format
      # check if the string is a comment
      if not lstr.startswith('#'):
         cfield = lines[ll].strip().split()
         pl.PlNumber[ll] = (cfield[0])
         pl.BiNumber[ll] = (cfield[1])
         pl.Vcmax_25[ll] = (cfield[2])
         pl.H_a[ll] = (cfield[3])
         pl.H_d[ll] = (200000.)
         pl.DeltaS[ll] = (cfield[4])
         #pl.Jmax_25.append(cfield[0])

         print pl.PlNumber[ll]
         print pl.BiNumber[ll]
         print pl.Vcmax_25[ll]
         print pl.H_a[ll]
         print pl.H_d[ll]
         print pl.DeltaS[ll]
         #pl.Jmax_25.append(cfield[0])
         ## Mode
         #if lstr.startswith( "mode" ):
         #   cfield = lines[ll].strip().split()
         #   cfg.mode.append(cfield[1])

         ## Name
         #if lstr.startswith( "name" ):
         #   cfield = lines[ll].strip().split()
         #   cstr = ""
         #   for istr in range( 1,len(cfield) ):
         #      cstr = cstr + cfield[istr]
         #   cfg.name.append(cstr)

         ## Path
         #if lstr.startswith( "path" ):
         #   cfield = lines[ll].strip().split()
         #   cfg.path.append(cfield[1])

      # End IF not comment line

   # End Loop over read lines[]





