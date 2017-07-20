from math import cos, sin #for the geometry.radial_to_cartesian(*args) function

#function to handle file appending operations
def file_handler_append(self, text):
  file_type = open(self.file_name, "a")
  file_type.write(text)
  file_type.write("\n")
  file_type.close()
  #TODO: finish  

#function to handle read operations
def file_handler_read(self):
  file_type = open(self.file_name, "r")
  file_type.close()
  #TODO: finish

class CM:
  """
  The CM class is used to comment the calculations, it has one attribute: the comment text.
  A CM class is required for each input file.
  """
  def __init__(self, comment):
    self.comment = comment
    self.CM_out = []
    
  def construct(self):
    self.CM_out = "CM " + self.comment + "\n"
    #Should we just return that string instead of creating a new prop?

class SY:
  def __init__(self, name, value):
    self.name = name
    self.value = value
    
  def construct(self):
    pass
    #TODO: construct the SY type

class GW:
  """
  The GW class defines a wire segment. A (GW) segment has the folowing properties:
      -start_x, start_y, start_z The coordinates of the start point (float)
    -end_x, end_y, end_z The coordinates of the end point of the segment (float)
    -wire_num an ID for the wire (int)
    -wire_seg ??
    -radius physical radius of the wire (float)
  Refer to http://www.nec2.org/part_3/cards/gw.html for more information
  """

  def __init__(self, wire_num, wire_seg, start, end, radius):
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
    pass
    #TODO: construct the GW type

class LD:
    pass

class EX:
    pass

class FR:
  """
  The FR class describes the frequencies used for the analysis, it has the folowing properties:
      - frequency, the first frequency considered in MHz (float)
    - increment, size of steps in MHz or noUnits when sweeping a frequency domain (float)
    - nsteps, number of steps considered (default 1) (int)
    - incType, type of incrementation: (int)
        + 0 : linear, frequency incremented by self.increment at each step
        + 1 : logarithmic frequency multiplied by self.increment at each step
  More information at: http://www.nec2.org/part_3/cards/fr.html
  """

  def __init__(self, frequency = 298.8):
    #define single frequency analysis as default case
    self.frequency = frequency
    self.increment = 0. #MHz
    self.nsteps = 1
    self.incType = 0

  def withLinSpace(self, increment = 0., nsteps = 1):
    """ To define a linear incrementation. Give increment in MHz"""
    self.increment = increment
    self.nsteps = nsteps
    self.incType = 0

  def withLogSpace(self, increment = 1.,nsteps = 1):
    """ To define a logarithmic incrementation. Give increment without units """
    self.increment = increment
    self.nsteps = nsteps    
    self.incType = 1

  def explain(self):
    """Provides some details on the current FR definition, for debug"""
    strFreq1 = str(self.frequency)
    if self.nsteps == 1:
        print('Describing single frequency analysis at ', strFreq1, ' MHz')
    elif self.incType == 0:
        strFreq2 = str(self.frequency + self.increment*(self.nsteps - 1))
        print('Sweeping linear domain from ', strFreq1, ' to ', strFreq2,' MHz using ', str(self.nsteps), ' steps')
    elif self.incType == 1:
        strFreq2 = str(self.frequency*(self.increment**(self.nsteps - 1)))  
        print('Sweeping log domain from ', strFreq1, ' to ', strFreq2,' MHz using ', str(self.nsteps), ' steps')


#class for NEC structures
class class_4NEC2:
  def __init__(self, file_name, CM_in, SY_in, GW_in):
    
    self.CM_data = CM_in
    self.SY_data = SY_in
    self.GW_data = GW_in
    
    #file info
    self.file_name = file_name

    #section bases
    self.CM_base = 0
    self.SY_base = 0
    self.GW_base = 0
    self.LD_base = 0
    self.EX_base = 0
    self.FR_base = 0

    #section sizes
    self.CM_size = 1
    self.SY_size = 0
    self.GW_size = 1
    self.LD_size = 0
    self.EX_size = 0
    self.FR_size = 0    
    
    #TODO: add external functions to class
    self.append = file_handler_append 
    self.check = file_handler_check

  def set_bases(self):
    self.CM_base = 0
    self.SY_base = self.CM_base + self.CM_size
    self.GW_base = self.SY_base + self.SY_size
    self.LD_base = self.GW_base + self.GW_size
    self.EX_base = self.LD_base + self.LD_size
    self.FR_base = self.EX_base + self.EX_size

#class to handle geometry
class geometry:
  def __init__(self):
    
    #variable for resolution (size of each segment)
    self.resolution = None
    self.res_const = 100
    
    #list of co-ordinates
    self.co_ordinates = []
    
    #helical parameters
    self.pitch = None
    self.diameter = None
    self.length = None
    
    #variables (other)
    self.radius = self.diameter/2
    self.theta = 0
    self.height = 0
 
  def radial_to_cartesian(self, r, theta, h):
    x = r * cos(theta)
    y = r * sin(theta)
    z = h    
    return [x,y,z]  
    
  def helical_inc_theta(self, d_theta):
    d_height = 2*self.radius*sin(d_theta/2)*tan(self.pitch)
    self.height = self.height + d_height
        
if __name__ == "__main__":
    pass
  
