# coding=utf-8

# This script reads stdin to interpret the data from nec2++

import sys
import copy
import logging
import re

import numpy as np

Logger = logging.getLogger()

datain = sys.stdin.readlines() #Reading the stdin

emptyLine = '\n'
currentTable = []
Tables = []
inTable = False

for line in datain:
    if line == emptyLine and not inTable:
        continue
    elif line == emptyLine and inTable:
        Tables.append(copy.copy(currentTable))
        currentTable = []
        inTable = False
        continue
    else:
        if inTable == False:
            inTable = True
        currentTable.append(line)
        continue


if inTable: #if the last line is in a table append the table to the main stack
    Tables.append(copy.copy(currentTable))


#Converting tables to matrices
dataout = []
headersOut = [] #list of strings containig headers
dataTemp = []
headers = ''
numeric = re.compile('[\d]')

#A shorth function to clean out the 'LINEAR' tags
def cleanStrings(l,replacement='NaN'):
    r = []
    for i in l:
        try:
            r.append(float(i))
        except ValueError:
            r.append(np.nan)
    return r

for table in Tables:
    for line in table:
        if not numeric.search(line):
            headers.join(line)
        else:
            dataTemp.append(np.array(cleanStrings(line.split(','),
                                    replacement=np.nan),dtype=float))
    try:
        dataout.append(copy.copy(np.vstack(dataTemp)))
    except ValueError:
        dataout.append([])

    headersOut.append(headers)
    headers = ''
    dataTemp=[]

del headers, dataTemp
