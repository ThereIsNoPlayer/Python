import numpy as np
arr1=np.arange(16).reshape(4,4)
arr2=arr1.T
print(arr1)
print(arr2)
a1=np.random.randint(1,10,(2,2))
a2=np.random.randint(1,10,(2,2))
print(a1)
print(a2)
h_st=np.hstack((a1,a2))
v_st=np.vstack((a1,a2))
print(h_st)
print(v_st)

