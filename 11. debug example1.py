#파이참 디버그 배우기 1

import matplotlib.pyplot as plt
import numpy as np

#Initialize empty arrays
array_len = 10000  #Desired length of arrays
var1 = np.zeros(array_len)
var2 = np.zeros(array_len)
var3 = np.zeros(array_len)
var4 = np.zeros(array_len)

#Define two functions:

def function_1(input):
    # Function 1
    for i in range(array_len):
        var1[i] = 2 + i*input
        var2[i] = 2*var1[i]
    return var1, var2

def function_2(input):
    #Function 2
    for j in range(array_len):
        var3[j] = 3+j*input
        var4[j] = 2*var3[j]
    return var3, var4

#Add var1 and var3, and plot result:
Output = function_1(1)[0] + function_2(2)[0]
plt.plot(Output)
print(Output)
