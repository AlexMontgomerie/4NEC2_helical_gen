
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
  #TODO: finish

class CM:
  def __init__(self, comment):
    self.comment = comment

class SY:
  def __init__(self, name, value):
    self.name = name
    self.value = value

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

#class for NEC structures
class class_4NEC2:
  def __init__(self, file_name, CM, SY, GW):
    
    self.CM_data = CM
    self.SY_data = SY
    self.GW_data = GW
    
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
    4NEC2.append = file_handler_append
    4NEC2.check = file_handler_check

  def write_comment(self):
    self.append("CM")
    self.append(self.comment)
    
  def set_bases(self):
    self.CM_base = 0
    self.SY_base = self.CM_base + self.CM_size
    self.GW_base = self.SY_base + self.SY_size
    self.LD_base = self.GW_base + self.GW_size
    self.EX_base = self.LD_base + self.LD_size
    self.FR_base = self.EX_base + self.EX_size

#class to handle geometry
#TODO:create class
class geometry:
  def __init__(self):
    self.resolution
    self.shape_gen #=helical_gen

  def get_co_ordinates:
    

#function to generate helical wire antenna
#TODO: write
def helical_gen(pitch, diameter, wire_radius):
  #function will define 
  return

if __name__ == "__main__":
  
