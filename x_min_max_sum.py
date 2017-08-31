import numpy as np
import random

x = np.random.random((3,3))       // create a 3 by 3 matrix with randoms number within //

print(x.sum())                    // Find the summation of all the numbers within the array //
print(x.min())                    // Find the minumum value //
print(x.max())                    // What else do you think this does? //

print(x.cumsum())                 // prints the cumulative of each row , try it and you will know //

print(x.sum(axis=0))              // prints the sums of the first row, axis is the row number //
