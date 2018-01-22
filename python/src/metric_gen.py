import math
import nec_out_parse 
import numpy as np

'''
This source file will take all the tables as input.
Need to get metrics for
  - peak/average gain
  - size of antenna (length, radius)
  - front-to-back ratio
  - fit to ideal radiation pattern
  - efficiency
  - power of output
  - directivity
'''

'''
def getIdealFitness(datain):
    
  dataout = nec_out_parse.parseNECOutTables(datain) 
  dataout = nec_out_parse.rowColTransform(dataout[8])

  idealout = 
 
  for i in range(len(dataout[7])):

  return diff
'''

def getPeak2AvgGain(datain):
  peak = 0
  totalSum = 0
  avg = 0

  dataout = nec_out_parse.parseNECOutTables(datain) 
  dataout = nec_out_parse.rowColTransform(dataout[8])

  for i in range(len(dataout[7])):
    #theta column
    '''
    if dataout[7][i] > peak:
      peak = dataout[7][i]
    totalSum = totalSum + dataout[7][i]
    #phi column
    if dataout[9][i] > peak:
      peak = dataout[9][i]
    '''

    mag = math.sqrt(dataout[7][i]**2 + dataout[9][i]**2)

    if mag > peak:
      peak = mag

    totalSum = totalSum + mag
  
  #TODO: need to actually see if this is the average
  avg = totalSum/(2*len(dataout[7]))

  return peak/avg


def getF2BRatio(datain,theta=True):
  #PHI: 1->9, THETA: 0->7
   
  front = 0
  back = 0

  dataout = nec_out_parse.parseNECOutTables(datain) 
  dataout = nec_out_parse.rowColTransform(dataout[8])

  #looking at f2b for theta
  if theta:
    for i in range(len(dataout[0])):
      if dataout[0][i] < 180:
        front = front + dataout[7][i]
      else:
        back = back + dataout[7][i]
  
  #looking at f2b for phi
  else:
    for i in range(len(dataout[1])):
      if dataout[1][i] < 180:
        front = front + dataout[9][i]
      else:
        back = back + dataout[9][i]

  #TODO: probably should check that not doing 0/0
  try:
    return front/back
  
  except ZeroDivisionError:
    return front  


def getEfficiency(datain):
  powerData = nec_out_parse.parseNECOutPowerBudget(datain)
  return powerData['efficiency']

def getOutPower(datain):
  powerData = nec_out_parse.parseNECOutPowerBudget(datain)
  return powerData['radiatedPower']

if __name__=="__main__":
   
  #open the file and read it
  fh = open('../output/output.out','r')
  datain = fh.readlines() 
 
  print getOutPower(datain)
  print getEfficiency(datain)
  print getF2BRatio(datain)
  print getPeak2AvgGain(datain)
