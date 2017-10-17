from nec2lib import *

'''
TODO:
 - fix up nec2lib
'''

def single_wire_gen():
  m = nec2(plot=0)  #create new nec model
  #create cards for the nec file
  m.gw(1,8,0,0,0,0,0,17,0.001)
  m.ge(1)
  m.fr(0,1,0,0,18.1,0,0,0,0,0)
  m.ex(0,1,1,0,1,0,0,0,0,0)
  m.rp(0,37,72,1000,0,0,5,500,0,0)
  m.en
  #write to file
  m.fileWrite("./test_nec.nec")

if __name__ == "__main__":
  single_wire_gen()  
 
