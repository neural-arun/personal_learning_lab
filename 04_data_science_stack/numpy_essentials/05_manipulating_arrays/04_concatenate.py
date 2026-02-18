"""  
np.concatenate((array1,array2), axis=0/1/2)
axis = 0 vertical stacking
axis = 1 horizontal stacking
(for axis = 1 it has to be atleast 2d array.)

"""


import numpy as np

arr1 = np.array([0,1,2,3,4,5,6,7,8])

arr2 = np.array([1,2,2,2,2,6,7,8,3])

concatenated_arr = np.concatenate((arr1,arr2), axis=0)
print(concatenated_arr)