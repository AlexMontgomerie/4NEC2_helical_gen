
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
  def __init__(self, comment):
    self.comment = comment
    self.CM_out = []
	
  def construct(self):
    self.CM_out = ["CM ", self.comment, "\n"]

class SY:
  def __init__(self, name, value):
    self.name = name
    self.value = value
	
  def construct(self):
	#TODO: construct the SY type

class GW:
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
	#TODO: construct the GW type

class LD:

class EX:

class FR:


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
	self.resolution
	self.res_const = 100
	
	#list of co-ordinates
	self.co_ordinates = []
	
	#helical parameters
	self.pitch
	self.diameter
	self.length
	
	#variables (other)
	self.radius = self.diameter/2
	self.theta
	
  def radial_to_cartesian(self, r, theta, h):
	x = r * cos(theta)
	y = r * sin(theta)
	z = h
	
	return [x,y,z]  
	
  def helical_inc_theta(self, d_theta):
	self.h = #TODO: function of self.h and self.theta
		
if __name__ == "__main__":
  
