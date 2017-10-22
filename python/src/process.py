# coding=utf-8

# This script reads stdin to interpret the data from nec2++

#std imports
import sys
import copy
import logging
import re

#lib inports
import numpy as np
import  numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D

#local imports
import aux

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

#Converting all tables to numpy objects
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

#Now we study the actual array
radiationPattern= dataout[3]

thetaCol = radiationPattern[:,0]
phiCol = radiationPattern[:,1]
gainCol = radiationPattern[:,4]
PHI, THETA, GAIN = aux.foldToMeshGrid(phiCol,thetaCol,gainCol)

del phiCol,thetaCol,gainCol
#Colormaps
cmap = plt.get_cmap('jet')
norm = colors.Normalize(vmin=GAIN.min(), vmax=GAIN.max())

NGAIN=aux.normalizer(GAIN) #ensures positivity
#Completing the final conversion to Cartesian coordinates

Xs,Ys,Zs = aux.shericalToCart(PHI,THETA,NGAIN)

#plotting
fig = plt.figure()
ax=fig.add_subplot(111, projection='3d')

ax.plot_surface(Xs,Ys,Zs,rstride=1, cstride=1,
    facecolors=cmap(norm(GAIN)),
    linewidth=0, antialiased=False, alpha=0.5)

plt.savefig('output/out.png')
plt.show()
