import numpy as np

arr_2d = np.array([[1,2],[3,4]])

print(arr_2d)

new_arr_2d = np.insert(arr_2d, 1,[5,6], axis=0)  # this will inser values row wise.
new_arr_2d1 = np.insert(arr_2d, 1,[5,6], axis=1)  # this will insert value coulumn wise
new_arr_2d2 = np.insert(arr_2d, 1,[5,6], axis=None)     # this will make array flattened and then insert.
print(new_arr_2d)
print(new_arr_2d1)
print(new_arr_2d2)
