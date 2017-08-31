import numpy as np

x = np.array([[1,2,3], [2,3,4]])

print(x.sum(axis=0))         // axis = 0 is the row, imagine axis=0 is vertical, axis=1 is horizontal, axis=2 is depth//
print(x.sum(axis=1))
