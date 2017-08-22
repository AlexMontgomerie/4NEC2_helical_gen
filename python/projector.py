# coding=utf-8
import numpy as np
from math import tan, pi


def planar(THETA,PHI,VALS,h):
    """This function will project a meshgrid spherical field on a plane h units
    above the origin
    Only feed angles in the -pi:pi range for theta"""
    assert(h != 0)

    radius = []
    colls = []
    for i, theta in enumerate(THETA[0,:]):
        if h>0 and theta>-pi/2. and theta<pi/2:
            radius.append(abs(tan(theta)*h))
            colls.append(i)
        elif h<0 and (theta<-pi/2. or theta>pi/2.):
            radius.append(abs(tan(theta)*h))
            colls.append(i)
        else:
            continue
    nVals=len(colls)
    Rs,PHI = np.meshgrid(np.array(radius),PHI[:,0])
    X,Y,Z = np.cos(PHI)*Rs,np.sin(PHI)*Rs,VALS[:,colls]
    return X,Y,Z
def tests():
    THETA = np.array([[0,pi/3.,pi/2.+0.1],[0,pi/3.,pi/2.+0.1],[0,pi/3.,pi/2.+0.1]])
    PHI = np.array([[0,0,0],[pi/3.,pi/3.,pi/3.],[pi/2.,pi/2.,pi/2.]])
    GAIN = np.array([[1,2,3],[4,5,6],[7,8,9]])
    return planar(THETA,PHI,GAIN,1)


print tests()
