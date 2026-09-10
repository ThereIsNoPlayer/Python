import numpy as np

arr1 = np.random.randint(1,11,(3,3))
print(arr1)
arr1[1,1]=99
print(arr1)

arr1[0,:]=0
arr1[:,0]=0
print(arr1)

result=np.where(arr1<5,-1,1)
print(result)