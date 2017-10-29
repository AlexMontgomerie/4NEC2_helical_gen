# coding=utf-8
import numpy as np

def shericalToCart(PHI,THETA,R):
    X=np.sin(THETA*np.pi/180.)*np.cos(PHI*np.pi/180.)*R
    Y=np.sin(THETA*np.pi/180.)*np.sin(PHI*np.pi/180.)*R
    Z=np.cos(THETA*np.pi/180.)*R
    return X,Y,Z

def shericalToCartRad(PHI,THETA,R):
    X=np.sin(THETA)*np.cos(PHI)*R
    Y=np.sin(THETA)*np.sin(PHI)*R
    Z=np.cos(THETA)*R
    return X,Y,Z

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
    Zmesh = np.zeros(np.shape(Xmesh))

    for i, item in enumerate(Z):
        Zmesh[ymappings[Y[i]],xmappings[X[i]]] = item

    return Xmesh, Ymesh, Zmesh

def normalizer(ARRAY):
    return ARRAY - ARRAY.min()
