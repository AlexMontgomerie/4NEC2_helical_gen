from nec2lib import nec2
import argparse

def parseInput():
  parser = argparse.ArgumentParser()
  #number of segments
  parser.add_argument('-n','--numSeg',type=int,nargs=1)
  #radius
  parser.add_argument('-r','--radius',type=float,nargs=1)
  #length
  parser.add_argument('-l','--length',type=float,nargs=1)
  #spacing
  parser.add_argument('-s','--spacing',type=float,nargs=1)
  #freq
  parser.add_argument('-f','--frequency',type=float,nargs=1)
  #output file name
  parser.add_argument('-o','--output',nargs=1)
  
  return parser.parse_args()

if __name__ == "__main__":

  #get input args  
  args = parseInput()
  
  #assign variables
  numSeg  = args.numSeg[0]
  radius  = args.radius[0]
  length  = args.length[0]
  spacing = args.spacing[0]
  freq    = args.frequency[0]
  wireRadius = 0.0025

  #debug statements
  print('Number of segements: ',numSeg)
  print('Radius             : ',radius)
  print('Length             : ',length)
  print('spacing            : ',spacing)
  print('frequency          : ',freq)
  print('wire radius        : ',wireRadius)

  #nec2 class
  nec_out = nec2(0)

  #first helix
  nec_out.gh(1,numSeg,spacing,length,radius,radius,radius,radius,nec_out.wireRadius)

  #rotate second helix
  nec_out.gm(1,1,0,0,180.0,0,0,0,0)

  #end geometry
  nec_out.ge(0)
  
  #add frequency card
  nec_out.fr(0,1,freq,0)
  
  #add excitation card
  nec_out.ex(0,1,1,0,1.0,0,0,0,0,0)
  nec_out.ex(0,2,1,0,-1.0,0,0,0,0,0)
  
  #other shit
  
  #create output file
  nec_out.fileWrite('./input/output.nec')
