from scipy.optimise import #...
import os
from ./helix_gen import get_helix_card
import metric_gen 
#import metric_gen 


#create function to optimise
def func(x)
  #create the antenna
  get_helix_card(x)
  #run nec
  os.system("nec2++ -i input/test_nec.nec -o output/output.out -s -c")

  #get the output data
  fh = open('../output/output.out','r')
  datain = fh.readlines()  

  #define weights for each output
  w = [1.0,1.0,1.0,1.0,1.0]

  #get output array
  #y[0] = w[0] * metric_gen.getIdealFitness(datain)
  y[1] = w[1] * metric_gen.getPeak2AvgGain(datain)
  y[2] = w[2] * metric_gen.getF2BRatio(datain)
  y[3] = w[3] * metric_gen.getEfficiency(datain)
  y[4] = w[4] * metric_gen.getOutPower(datain)

  return y
#optimise

#verify results

