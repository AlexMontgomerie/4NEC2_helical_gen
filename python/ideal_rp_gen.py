from math import *
import matplotlib.pyplot as plt
import numpy as np

#setup variables
n = 1000
Rs = 6371000
Re = 406000 + 6371000
scale =1e-7

#setup list
theta = np.arange(-pi,pi,2*pi/n)
r = Rs*np.cos(theta) + np.sqrt(Re**2 - (Rs*np.sin(theta))**2)

theta_max = asin(Re/Rs)

#get values of radius according to function
for i in range(len(theta)):
    if abs(theta[i]) > theta_max:
        r[i]=0

#plot r against theta
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r*scale)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis, scaled by {}".format(scale), va='bottom')
plt.show() 
