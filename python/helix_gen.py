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
  return parser.parse_args()
  

if __name__ == "__main__":
  
  args = parseInput()
  
  numSeg  = args.numSeg[0]
  print(numSeg)
  radius  = args.radius[0]
  print(radius)
  length  = args.length[0]
  print(length)
  spacing = args.spacing[0]
  print(spacing)
  wireRadius = 0.0025

  nec_out = nec2(0)

  #first helix
  nec_out.gh(1,numSeg,spacing,length,radius,radius,radius,radius,nec_out.wireRadius)

  #rotate second helix
  nec_out.gm(1,1,0,0,180.0,0,0,0,0)

  #end geometry
  nec_out.ge(0)
  
  #add frequency card
  
  #add excitation card
  nec_out.ex(0,1,1,0,1.0,0,0,0,0,0)
  nec_out.ex(0,2,1,0,-1.0,0,0,0,0,0)
  
  #other shit
  
  #create output file
  nec_out.fileWrite('output.nec')