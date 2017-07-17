
#function to handle file appending operations
def file_handler_append(self):
  file_type = open(self.file_name, "a")
  #TODO: finish  

#function to handle read operations
def file_handler_read(self):
  file_type = open(self.file_name, "r")
  #TODO: finish

#class for NEC structures
class 4NEC2:
  def __init__(self,file_name):

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
    4NEC2_comment.append = file_handler_append
    4NEC2_comment.check = file_handler_check

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

#function to generate helical wire antenna
#TODO: write
def helical_gen(pitch, diameter, wire_radius):


if __name__ == "__main__":
  
