import numpy as np

def Read_dataset( nPlants, nBiomes, ifile ):

   # Declare mutable object => lines read from config file
   lines = []

   # Reads all the lines in the config file specified at CLI
   lines = tuple( open(ifile, 'r' ))

   nplants =  int( len(lines) ) 
   #nplants[0] =  len(lines) 
   # Loop over all of these read lines
#   for ll in range( nplants[0] ):
#
#      # Create a string from each line
#      lstr = str(lines[ll])
#      # nullify case sensitivity in that string
#      lstr = lstr.lower()

      # if it is meant to be interpreted - interpret based on what
      # it starts with. See configfile example format
      # check if the string is a comment
      #if not lstr.startswith('#'):
      #   pl.PlNumber[ll] = 
      #   pl.BiNumber[ll] =
      #   pl.Vcmax_25[ll] =
      #   pl.Jmax_25[ll] =
      #   pl.H_a[ll] =
      #   pl.H_d[ll] =
      #   pl.DeltaS[ll] =

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

###############################################################################

