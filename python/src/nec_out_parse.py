# coding=utf-8

# This script reads stdin to interpret the data from nec2++

#std imports
import copy
import logging
import re

#lib inports
import numpy as np

#local imports
import aux

DEBUG = True

#A short function to clean out the 'LINEAR' tags
def cleanStrings(l,replacement='NaN'):
    r = []
    for i in l:
        try:
            r.append(float(i))
        except ValueError:
            r.append(np.nan)
    return r

def removeLINEAR(line):
  return re.sub(r'LINEAR','',line)

def removeEndLine():
  pass

def rowColTransform(table):
  return zip(*table)

def parseNECOutTables(outArray):

  out = [[]] 
  tableIndex = 0 
  
  match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[+\-]?\ *[0-9]+)?') 

  for i in range(len(outArray)):
    outArray[i] = removeLINEAR(outArray[i])
  
  state = 1
  state_prev = 1  
 
  for i in range(len(outArray)):
    
    state_prev = state
    val = re.findall(match_number,outArray[i])

    if len(val)>2:
      state = 0
      out[tableIndex].append([float(x) for x in val])

    else:
      state = 1

    if state and not state_prev:
      out.append([])
      tableIndex = tableIndex + 1

  if DEBUG==True:
    for i in range(len(out)):
      print 'Table: ',i
      print out[i]

  return out

'''
function to parse for values in relation to power budget
IN = list of lines
OUT = dictionary of power budget values
'''
def parseNECOutPowerBudget(outArray):
  
  #TODO: turn into a dictionary
  out = {
    'inputPower'    : 0,
    'radiatedPower' : 0, 
    'structureLoss' : 0,
    'networkLoss'   : 0,
    'efficiency'    : 0 
  }
 
  #print outArray 
  print len(outArray)
  
  match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?') 
  
  for i in range(len(outArray)):

    #INPUT POWER search
    searchObj = re.search( r'INPUT POWER', outArray[i], re.M|re.I)
    if searchObj:
      val = re.findall(match_number,outArray[i])
      out['inputPower'] = float(val[0])

    #RADIATED POWER search
    searchObj = re.search( r'RADIATED POWER', outArray[i], re.M|re.I)
    if searchObj:
      val = re.findall(match_number,outArray[i])
      out['radiatedPower'] = float(val[0])

    #STRUCTURE LOSS search
    searchObj = re.search( r'STRUCTURE LOSS', outArray[i], re.M|re.I)
    if searchObj:
      val = re.findall(match_number,outArray[i])
      out['structureLoss'] = float(val[0])

    #NETWORK LOSS search
    searchObj = re.search( r'NETWORK LOSS', outArray[i], re.M|re.I)
    if searchObj:
      val = re.findall(match_number,outArray[i])
      out['networkLoss'] = float(val[0])

    #EFFICIENCY search
    searchObj = re.search( r'EFFICIENCY', outArray[i], re.M|re.I)
    if searchObj:
      val = re.findall(match_number,outArray[i])
      out['efficiency'] = float(val[0])

  if DEBUG==True:
    print 'input power: ', out['inputPower']
    print 'radiated power: ', out['radiatedPower']
    print 'structure loss: ', out['structureLoss']
    print 'network loss: ', out['networkLoss']
    print 'efficiency: ', out['efficiency']
      
  return out

if __name__ == "__main__":
  #dataout = parseNECOutFile('../output/output.out')
  
  #open the file and read it
  fh = open('../output/output.out','r')
  datain = fh.readlines() 
 
  parseNECOutPowerBudget(datain)
  dataout = parseNECOutTables(datain) 
  rowColTransform(dataout[8])
