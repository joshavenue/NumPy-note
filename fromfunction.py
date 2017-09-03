import numpy as np

def f(x,y,z):
    return z*x+y
    
a = np.fromfunction(f,(2,3,5),dtype=int)

print(a)
