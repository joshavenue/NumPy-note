import numpy as np

print(np.zeros(2,3))      // prints zeros in the dimension of 2 x 3 //
print(np.ones(2,3))       // prints ones in the dimension of 2 x 3 //

print(np.empty(2,3))      // prints random value dependant on the state of the memory //

print(np.arange(10,50,5)) // prints an array that begins from 10, increasing each element by 5 to number lesser than 50 //
                          // similar to : for i=10; i < 50; i += 5; but for array
                          
print(np.linspace(0,10,5) // prints an array that begins from 0, increasing by the division of 10 and 5, which is 2.
                          // simialr to : for i = 0; i < 10; j = 10/5; i += j; but for array
                          
