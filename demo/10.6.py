import numpy as np

arr1= np.ones((4, 3))
arr2= np.array([1, 2, 3])
print(arr1)
print(arr2)
print(arr1+arr2)

arr_4 = np.array([1, 2, 3, 4])
arr_col = arr_4.reshape(4, 1)
arr_4x3_2 = np.ones((4, 3)) * 5
print(arr_4)
print(arr_col)
print(arr_4x3_2)
print(arr_4x3_2+arr_col)