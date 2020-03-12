import numpy
import numpy as np

def f(x):
    a = -4+(8*x)-5*(pow(x,2))+(pow(x,3))
    return a



def bisseccao(f,xi,xs,it_max,ea):
    it = 0;
    fi = f(xi)
    fs = f(xs)
    
    while ((it<=it_max) and abs(f(xi)*f(xs))>=ea):
        xn = (xi+xs)/2
        if ((f(xn)*f(xi))<0):
            xs=xn
        else:
            xi=xn
            
        it = it +1
            
    return it,xi,xs



print(bisseccao(f,(1/2),(3),(100000),(10e-999)))
