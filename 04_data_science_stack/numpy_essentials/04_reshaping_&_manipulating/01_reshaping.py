"""  
array.reshape(rows,columns)
"""

import numpy as np

arr = np.array([1,2,3,4,5,6])
new_arr = arr.reshape(3,2)
print(new_arr)