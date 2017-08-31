import numpy as np

x = np.arange(50).reshape(5,5,2)

x.shape()             // To check the shape of the dimension //
x.ndim()              // To check the number of dimension //
x.itemsize()          // To check the size in bytes of each element of the array. //
x.size()              // To check the multiplication number of the total dimension, for this is 5 x 5 x 2 = 50  //
x.dtype()             // To check the type of element of the array, this is int64 //


