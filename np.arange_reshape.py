import numpy as np

x = np.arange(20).reshape(4,5)  // x = np.arange(num1).reshape(num2,num3) , whereby num1 is the range of the number
                                // num2 is the vertical axis, num3 is the horizontal axis length
print(x)

                                // num2 = 1st dimension
                                // num3 = 2nd dimension
                                // You can add another num4 for 3rd dimension at .reshape
