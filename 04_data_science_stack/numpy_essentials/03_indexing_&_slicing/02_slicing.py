"""  
array[start:stop(excluded):step(defualt=1)]
"""
import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr[1:5])    # index 1 to 4   [2 3 4 5]
print(arr[:4])     # index 0 to 3   [1 2 3 4]
print(arr[::2])    # start se end tak poora lega aur step size 2 hoge   [1 3 5]
# HAR DOOSRE ELEMENT KO PICK KAREGA UPAR VALA.
print(arr[::-1])        # whole array is reversed.
