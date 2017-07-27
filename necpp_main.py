# -*- coding: utf-8 -*-
try:
    from necpp import *
except ImportError:
    print('Install necpp using \"(sudo) pip install necpp\"')

#define: unitsL, meters
#define: unitsA, degrees

#prepare
context = nec_context()

#Begin to build geometry

g = context.get_geometry()

antennaHeight = 0.1 #m
antennaPitch = 0.01 #m.cycles^-1

antennaXRadius1 = 0.05 #m
antennaXRadius2 = 0.05 #m
antennaYRadius1 = 0.05 #m
antennaYRadius2 = 0.05 #m

wireRadius = 0.001 #m

nSeg = 1000

nHelix = 2
#Helixes:
ang = 360./nHelix #deg
for n in range(nHelix):
    g.helix(0, nSeg, antennaPitch, antennaHeight, antennaRadius1, \
        antennaYRadius1,antennaXRadius2, antennaYRadius2, wireRadius)
    g.move(0,0,ang)

#Second helix
