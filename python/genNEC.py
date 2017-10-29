from math import cos, sin 

#wire class
class GW:
  def __init__(self,wire_num, wire_seg, start, end, radius):

    self.wire_num = wire_num
    self.wire_seg = wire_seg
    self.radius = radius

    self.start_x = start[0]
    self.start_y = start[1]
    self.start_z = start[2]

    self.end_x = end[0]
    self.end_y = end[1]
    self.end_z = end[2]

  def construct(self):

    out = "GW " +
          self.wire_num + " " +
          self.wire_seg + " " +
          self.start_x + " " +
          self.start_y + " " +
          self.start_z + " " +
          self.end_x + " " +
          self.end_y + " " +
          self.end_z + " " +
          self.radius

    return out

class EX:
  def __init__(self,I1,I2,I3,I4,F1,F2):
    self.I1 = I1 
    self.I2 = I2 
    self.I3 = I3 
    self.I4 = I4 
    self.F1 = F1
    self.F2 = F2

  def construct(self):
    out = "EX " +
          self.I1 + " " +
          self.I2 + " " +
          self.I3 + " " +
          self.I4 + " " +
          self.F1 + " " +
          self.F2
    return out

class FR:
  def __init__(self, IFRQ, NFRQ, FMHZ, DELFRQ):
    self.IFRQ = IFRQ
    self.NFRQ = NFRQ
    self.FMHZ = FMHZ
    self.DELFRQ = DELFRQ

  def construct(self);
    out = "FR " +
          self.IFRQ + " " +
          self.NFRQ + " " +
          "0 0 " +
          self.FMHZ + " " +
          self.DELFRQ
    return out

#parameter checker

#monopole gen
def monopoleGenerator(length, freq, fileName):
  #work out segments
  seg = length/1000
  radius = 0.0001

  #get each line of output file
  gwLine = GW(1,seg,[0,0,0],[0,0,length],radius).construct
  exLine = EX(0,1,5,0,1,0).construct
  frLine = FR(0,1,0,0,freq,0).construct

  #write to file

  pass

#helix gen

if __name__ == "main":
  pass

