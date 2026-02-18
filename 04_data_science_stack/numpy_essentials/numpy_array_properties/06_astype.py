import numpy as np

arr = np.array([12,1.7,3.4,45])
int_arr = arr.astype(int)
print(int_arr.dtype)            # int64
print(arr.dtype)                # float64

print(int_arr)