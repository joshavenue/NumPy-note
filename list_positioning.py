import numpy as np

x = np.arange(0,40,2).reshape(2,2,5) .    // When there only 2 numbers in reshape, it will be (x and y-axis)
                                          // If there are 3 like this example, it will be (z,x and y-axis)

print(x)    // Will display below //
x = array([[[ 0 , 2 , 4 , 6 , 8],
            [ 10, 12, 14, 16, 18]],
            
            [[20 , 22 , 24 , 26 , 28],
             [30 , 32 , 34 , 36 , 40]]])
            

x[1:2] =    ([[[20 , 22 , 24 , 26 , 28],
               [30 , 32 , 34 , 36 , 40]]])
            

x[0:2,1] =  ([[10 , 12 , 14 , 16 , 18],
              [30 , 32 , 34 , 36 , 38]))
              
  
