import numpy as np

x = np.array([[1,2,3],[2,3,4]])
y = np.array([[2,3,4],[3,4,5]])

print(np.dot(x,y))              // Prints the matrix product

// Matrix dot formulae 
        
//        [ a b c ]   [ x ]     [ ax + bx + cx ]    //
//    x = | d e f | * | y | =   | dy + ey + fy |    //
//        [ g h i ]   [ z ]     [ gz + hz + iz ]    //
        
        
