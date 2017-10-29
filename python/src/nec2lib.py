import math
import os

def sci(f):
  ''' Return formatted string containing scientific notation float in a 13 char wide field (xyz coordiates, radius)
  '''
  return '{: > 13.5E}'.format(f)


def dec(i):
  ''' Return formatted string containing a decimal integer in a 6 char wide field (tags, segments)
  '''
  return '{: >6d}'.format(math.trunc(i))

class nec2:
  def __init__(self,plot):
    ''' Prepare the model with the given wire radius
    '''
    self.comments   =""
    self.geometry   =""
    self.tag      =0
    self.wireRadius = 2.5e-3
    self.controls   =""
    if plot :
      self.graph=Plot()


  # ---------------------------------------------------------------------------------------------------
  # Comments cards
  # ---------------------------------------------------------------------------------------------------

  def cm(self, comment):
    ''' Add the line for a CM comment card.
    '''
    self.comments += "CM " + comment + "\n"
    return self

  def ce(self):
    ''' Card to "terminate reading of geometry data cards"
    '''
    self.comments += "CE\n"
    return self


  # ---------------------------------------------------------------------------------------------------
  # Geometry cards
  # ---------------------------------------------------------------------------------------------------


  def gw(self, tag, segments, x1, y1, z1, x2, y2, z2, radius):
    ''' Add the line for a GW card, a wire.
    '''
    self.geometry += "GW" + dec(tag) + dec(segments)+ sci(x1) + sci(y1) + sci(z1) + sci(x2) + sci(y2) + sci(z2) + sci(radius) + "\n"

  def gh(self, tag, segments, s, l, rx0, ry0, rxl, ryl, rad):
    ''' Add the line for a GH card, a helix.
    '''
    self.geometry += "GH" + dec(tag) + dec(segments)+ sci(s) + sci(l) + sci(rx0) + sci(ry0) + sci(rxl) + sci(ryl) + sci(rad) + "\n"

  def gm(self, ITSI, NRPT, ROX, ROY, ROZ, XS, YS, ZS, ITS):
    ''' Add the line for a GH card, a helix.
    '''
    self.geometry += "GM" + dec(ITSI) + dec(NRPT)+ sci(ROX) + sci(ROY) + sci(ROZ) + sci(XS) + sci(YS) + sci(ZS) + sci(ITS) + "\n"
	
  def addWire(self, segments, pt1, pt2):
    ''' Append a wire, increment the tag number, and return this object to facilitate a chained attachToEX() call
    '''
    self.tag += 1
    self.gw(self.tag, segments, pt1.x, pt1.y, pt1.z, pt2.x, pt2.y, pt2.z, self.wireRadius)
    self.middle = math.trunc(segments/2) + 1
    return self


  def ge(self,gpflag):
    ''' Card to "terminate reading of geometry data cards"
    '''
    self.geometry += "GE" + dec(gpflag) + "\n"
    return self



  # ---------------------------------------------------------------------------------------------------
  # Controls
  # ---------------------------------------------------------------------------------------------------

  def gn(self):
    ''' Card to determine the Ground Parameters
    '''
    self.controls +="GN     0     0     0     0           6.0    1.000E-03\n"
    return


  def fr(self, IFRQ, NFRQ, FMHZ, DELFRQ):
    ''' Define the frequency range to be modeled
    '''
    self.controls += "FR" + dec(IFRQ) + dec(NFRQ) + dec(0) + dec(0) + sci(FMHZ) + sci(DELFRQ) + "\n"
    return self


  def ex(self,I1,I2,I3,I4,F1,F2,F3,F4,F5,F6):
    ''' Define excitation parameters.
    '''
    if I1==0:
      self.controls += "EX" + dec(I1) + dec(I2) + dec(I3) + dec(I4) + sci(F1) + sci(F2) + "\n"
    
    else:
      self.controls += "EX" + dec(I1) + dec(I2) + dec(I3) + dec(I4) + sci(F1) + sci(F2) + sci(F3) + sci(F4)  + sci(F5) + sci(F6) + "\n"

    return self

  def feedAtMiddle(self):
    ''' Attach the EX card feedpoint to the middle segment of the element that was most recently created
    '''
    self.ex(self.tag,self.middle)
    return self

  def feedAtEnd(self):
    ''' Attach the EX card feedpoint to the begin or end segment of the element that was most recently created
    '''
    self.ex(self.tag,1)
    return self


  def ld(self,ldtyp,ldtag,ldtagf,ldtagt,zlr,zli,zlc):
    ''' Define excitation parameters.
    '''
    I1 = ldtyp    # Determines the type of loading which is used.
    I2 = ldtag    # Tag number; identifies the wire section(s) to be loaded by its (their) tag numbers.
    I3 = ldtagf   # Equal to m specifies the mth segment of the set of segments whose tag numbers equal the tag number specified in the previous parameter.
    I4 = ldtagt   # Equal to n specifies the nth segment of the set of segments whose tag numbers equal the tag number specified in the parameter LDTAG.
    F1 = zlr      # Resistance in ohms, if none, leave blank.
    F2 = zli      # Inductance in henries, if none, leave blank.
    F3 = zlc      # Capacitance in farads, if none, leave blank.
    self.controls += "LD" + dec(I1) + dec(I2) + dec(I3) + dec(I4)+ sci(F1) + sci(F2) + sci(F3)+ "\n"
    return self

  def loadAtMiddle(self,ldtyp,zlr,zli,zlc):
    '''Loading at Middle LD
    '''
    self.ld(ldtyp,self.tag, self.middle, self.middle, zlr, zli, zlc)
    return self

  def loadAtEnd(self,ldtyp,zlr,zli,zlc):
    '''Loadin at end LD
    '''
    self.ld(ldtyp,self.tag, 1, 1, zlr, zli, zlc)
    return self


  def rp(self,I1,NTH,NPH,I4,THETS,PHIS,DTH,DPH):
    ''' Card to initiate calculation and output of radiation pattern.
    '''
    '''
    I1  = 0      # 0 is normal mode: defaults to free-space unless a previous GN card specified a ground plane
    NTH = 10     # Number of values of theta (angle away from positive Z axis)
    NPH = 21     # Number of values of phi (angle away from X axis in the XY plane)
    I4  = 0      # Use defaults for some misc output printing options
    THETS = 0.0  # Theta start value in degrees
    PHIS  = 0.0  # Phi start value in degrees
    DTH   = 10.0 # Delta-theta in degrees
    DPH   = 18.0 # Delta-phi in degrees
    '''
    self.controls += "RP" + dec(I1) + dec(NTH) + dec(NPH) + dec(I4) + sci(THETS) + sci(PHIS) + sci(DTH) + sci(DPH) + "\n"
    return self

  def xq(self):
    ''' Cart to execution calculation not nedded if rp
    '''
    self.controls += "XQ\n"
    return self


  def en(self):
    ''' Card to mark end of input
    '''
    self.controls += "EN\n"
    return self


  # ---------------------------------------------------------------------------------------------------
  # Creatin nec2 File
  # ---------------------------------------------------------------------------------------------------


  def fileWrite(self,fileName):
    ''' Write a NEC2 formatted card stack to the output file
    '''
    nec2File = open(fileName,'w')
    nec2File.write(self.comments)
    nec2File.write(self.geometry)
    nec2File.write(self.controls)
    nec2File.close()



  def show(self):
    ''' Dump the card stack back to the console for a quick sanity check
    '''
    print self.comments
    print self.geometry
    print self.controls
