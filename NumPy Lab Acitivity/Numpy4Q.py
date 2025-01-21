#  4. Write a NumPy program to convert a list and tuple into arrays.
# Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#  Input: my_tuple = ([8, 4, 6], [1, 2, 3])

import numpy as np

# Initialization
list_num = [1, 2, 3, 4, 5, 6, 7, 8]
tuple_num = ([8, 4, 6], [1, 2, 3])

my_arr1=np.array(list_num)

print(my_arr1)

my_arr2=np.array(tuple_num)
print(my_arr2)