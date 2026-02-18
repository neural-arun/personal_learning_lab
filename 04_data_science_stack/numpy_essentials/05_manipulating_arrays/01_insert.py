"""  
np.array(array, index, value, axis=None)
axis= 0  # row wise change.
axis = 1 # column wise change.
axis = 2  # entity wise change.
"""

import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8])
print(arr)

new_arr = np.insert(arr, 3,10,axis=None)
print(new_arr)