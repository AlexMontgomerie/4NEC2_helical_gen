from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import aux

def getIdealMatrix():
  #setup variables
  n = 100
  Re = 6.371
  Rs = 0.406 + Re
  scale =1
  theta_max = asin(Re/Rs)

  #setup list
  theta = np.arange(-pi,pi,2*pi/n)
  phi = np.arange(-pi,pi,2*pi/n)
  r = np.zeros(n)
  
  theta = [0.0]*n*n
  phi   

  #variable to track maximum radius value
  r_max = 0

  for i in range(len(theta)):
    if abs(theta[i]) > theta_max:
      r[i]=0
    else:
      r[i] = Rs*np.cos(theta[i]) - np.sqrt(Re**2 - (Rs*np.sin(theta[i]))**2)
    
    #for normalisation
    if r[i] > r_max:
      r_max = r[i]


  #TODO: add normalisation function
  for i in range(len(theta)):
    r[i] = r[i]/r_max

  #TODO: add loop for phi
  s=(n,n)
  r_3d = np.zeros(n*n)
  theta_3d = np.zeros(n*n)
  phi_3d = np.zeros(n*n)
  #set r_3d to same pattern as r for all phi
  for i in range(len(theta)):
    for j in range(len(phi)):
      r_3d[n*i+j] = r[j]
      phi_3d[n*i+j] = phi[i]
      theta_3d[n*i+j] = theta[j]

  print "R: ", r_3d
  print "THETA: ",theta_3d
  print "PHI: ",phi_3d

  PHI, THETA, GAIN = aux.foldToMeshGrid(phi_3d,theta_3d,r_3d)
  Xs,Ys,Zs = aux.shericalToCartRad(PHI,THETA,GAIN)

#TODO: change to 3D plot
if fig_3d==False:
  #plot r against theta
  ax = plt.subplot(111, projection='polar')
  ax.plot(theta, r*scale, xunits=radians)
  ax.set_rmax(1)
  #ax.set_rticks([0.5, 1])  # less radial ticks
  #ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
  #ax.grid(True)

  ax.set_title("A line plot on a polar axis, scaled by {}".format(scale), va='bottom')
  plt.savefig('ideal.png')
  plt.show()
else:
  ax = plt.subplot(111, projection='3d')
  ax.plot_surface(Xs,Ys,Zs)
  plt.savefig('ideal.png')
  plt.show()
