"""  
.ravel()  --> it returns a view.(jab possible) increases speed 
.flatten() --> it returns a copy. (hamesha)  when isolation is needed.
"""

import numpy as np

arr_2d = np.array([[1,2,3,4],[5,6,7,8]])

ravel = arr_2d.ravel()
print(ravel)        # ye ravel arr_2d ka view hai (mtlab memory same hai bs dikh 2d se 1d rha hai ) , agr yaha change kiya to arr_2d bhi change hoga .

fletten = arr_2d.flatten()
print(fletten)    # ye jo flatten hai ye naya data hai. isme change karne se arr_2d mein koi change nhi hoga.