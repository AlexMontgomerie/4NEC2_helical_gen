# coding=utf-8

#std imports
import sys

#lib inports
import  numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        raise ValueError('Data file path missing')



#get data
data =  np.genfromtxt(path,delimiter=',',dtype=np.float64)[1:,:]

#Extract info and clear memory
theta, phi, gain = data[:,0],data[:,1],data[:,4]
del data

#Convert to radiants
degToRad=np.pi/180

#figure out number of thetas
nTheta=0
for i, item in enumerate(theta[1:]):
    if item==theta[0]:
        nTheta=i+1
        break

thetaVals=theta[0:nTheta]*degToRad
#figure out number of phis
nPhi=len(phi)/nTheta
phiVals=np.array([phi[i*nPhi] for i in xrange(nPhi)])*degToRad


#create meshgrid
THETA, PHI = np.meshgrid(thetaVals,phiVals)
GAIN=THETA*0

#Asign Gain Values
for j, jtems in enumerate(phiVals):
    for i, item in enumerate(thetaVals):
        GAIN[i,j]=gain[j+i*nTheta]
#set the colormap
GAIN=np.abs(GAIN)
cmap = plt.get_cmap('jet')
norm = colors.Normalize(vmin=GAIN.min(), vmax=GAIN.max())

#Normalize gain

NGAIN=GAIN - GAIN.min()

NGAIN=NGAIN/NGAIN.max()

#clean memory
del phi, theta, gain

Xs,Ys,Zs = NGAIN*np.cos(PHI)*np.cos(THETA),NGAIN*np.cos(PHI)*np.sin(THETA),NGAIN*np.sin(PHI)
del PHI, THETA
#setup plots
fig = plt.figure()
ax=fig.add_subplot(111, projection='3d')

ax.plot_surface(Xs,Ys,Zs,rstride=1, cstride=1,
    facecolors=cmap(norm(GAIN)),
    linewidth=0, antialiased=False, alpha=0.9)

plt.savefig('../pics/out.png')
plt.show()
