import numpy as np
import sklearn
import pandas as pd

X=([0,0],[0,1],[1,0],[1,1])
y=[1,0,0,1]
a=0.8
it=100
W=np.random.rand(2,1)
print("w=",W)
b = 1
e=0

X=np.array(X)
#partie lineaire de la forme : z=x*w+b
def linear_func(X,W,b):
    for i in range (len(X)):
            Z = np.hstack((X[i].dot(W) ,b))
            #print(Z)
    return  Z
#model(X,W,b)
def sigmoid(Z,a):
    Y = 1 / (1 + np.exp(-a * Z))
    return Y
def dervie(X,y,b):
    d=
def training(e,X,W,b,Y,it,learning_rate=0.01):
    while it<100:
        linear_func()
        sigmoid()

y=np.array(y)
y=y.T
y=y.reshape(4,1)
print("y.shape=",y.shape)
X=np.array(X)
print("X.shape",X.shape)
print("W.shape=",W.shape)

print("b=",b)
Z=X.dot(W)+b
print("z.shape=",Z.shape)
print("z=", Z)







