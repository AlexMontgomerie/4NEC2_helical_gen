# coding=utf-8
import numpy as np

def shericalToCart(PHI,THETA,R):
    X=np.sin(THETA)*np.cos(PHI)*R
    Y=np.sin(THETA)*np.sin(PHI)*R
    Z=np.cos(THETA)*R
    return XYZ

def reduceToDict(X):
    #storing the mapping of the array in a dict to reduce search complexity
    #to O(1) (instead of O(n))

    xs = []
    xPhone = {}
    for i in X:
        if not i in xs:
            xs.append(i)
    xs.sort()
    for i, item in enumerate(xs):
        xPhone[item] = i
    return xs, xPhone

def foldToMeshGrid(X,Y,Z):
    #this function takes three column vectors and returns the meshgrid
    #representation of the data

    #Step 1: Create array mapping dicts to build the Z mesh and extract unique
    #values
    xs ,xmappings = reduceToDict(X)
    ys ,ymappings = reduceToDict(Y)

    Xmesh, Ymesh = np.meshgrid(xs,ys)#build X,Y mesh

    #initialize Z mesh
    Zmesh = Xmesh

    for i, item in enumerate(Z):
        Zmesh[ymappings[Y[i]],xmappings[X[i]]] = item

    return Xmesh, Ymesh, Zmesh
