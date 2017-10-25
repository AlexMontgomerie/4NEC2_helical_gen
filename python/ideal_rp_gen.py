from math import *
import matplotlib.pyplot as plt

#setup variables
n = 10
Rs = 6371000
Re = 406000 + 6371000

#setup list
theta = [0]*n
r = [0]*n

theta_max = asin(Re/Rs)

#get values of radius according to function
for i in range (0,n):
  theta[i] = 18*i
  if theta[i] < -theta_max or theta[i] > theta_max:
    r[i] = 0
  else:
    r[i] = Rs*cos(theta[i]) + sqrt(Re^2-(Rs*sin(theta[i]))^2)

#plot r against theta
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()