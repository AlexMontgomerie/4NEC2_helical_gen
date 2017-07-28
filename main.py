from math import cos, sin #for the geometry.radial_to_cartesian(*args) function

#
def file_handler_append(path, text):
  """Handles file appending operations"""
  with open(path,'a') as file_type:
    file_type.write(text)
    file_type.write("\n")
  #TODO: finish

def writeLine(Class, I1, I2, F1, F2, F3, F4, F5, F6, F7):
  """Writes a generic line for a .nec file"""
  #Check types and convert for better reliability
  assert(type(Class) == str)
  assert(Class.isupper())

  I1 = int(I1)
  I2 = int(I2)

  F1 = float(F1)
  F2 = float(F2)
  F3 = float(F3)
  F4 = float(F4)
  F5 = float(F5)
  F6 = float(F6)
  F7 = float(F7)

  s = '' #output string
  #Line type first (+space)
  s += Class + ' '

  #I1 I2 (+spaces)
  assert(I1<10**5)
  assert(I2<10**5) 
  s += '{:>5} {:>5}'.format(I1,I2)

  #F1-F7 (+spaces)
 


#function to handle read operations
def file_handler_read(self):
  file_type = open(self.file_name, "r")
  file_type.close()
  #TODO: finish


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
  
