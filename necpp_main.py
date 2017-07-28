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
#TODO is this the new c_geometry() equivalent?
g = context.get_geometry()

def getPitch(spacing, radius):
  #return arctan(radius*spacing)
  pass

antennaHeight = 0.1 #m
antennaSpacing = 0.01 #m.cycles^-1

antennaXRadius1 = 0.05 #m
antennaXRadius2 = 0.05 #m
antennaYRadius1 = 0.05 #m
antennaYRadius2 = 0.05 #m

wireRadius = 0.001 #m

nSeg = 1000

'''
/* subroutine helix generates segment geometry
  data for a helix of segment_count segments 
 
           S   (F1) - Spacing between turns.
           HL  (F2) - Total length of the helix.
           A1  (F3) - Radius in x at z = 0.
           B1  (F4) - Radius in y at z = 0.
           A2  (F5) - Radius in x at z = HL.
           B2  (F6) - Radius in y at z = HL.
           RAD (F7) - Radius of wire.
*/
void c_geometry::helix(int tag_id, int segment_count, nec_float s, nec_float hl, nec_float a1, nec_float b1,
    nec_float a2, nec_float b2, nec_float rad)
'''

nHelix = 2
#Helixes:
ang = 360./nHelix #deg
g.helix(1, nSeg, antennaSpacing, antennaHeight, antennaRadius1, \
    antennaYRadius1,antennaXRadius2, antennaYRadius2, wireRadius)
g.move(0,0,ang,0,0,0,1,1,1)

#Second helix



g.geometry_complete()
