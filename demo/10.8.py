import numpy as np
np.random.seed(42)
arr1 = np.random.randint(1, 101, size=10)
print(arr1)
print(np.sum(arr1))
print(np.mean(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.std(arr1))

arr2 = np.random.randint(1, 101, size=(4, 3))
print(arr2)

print(np.mean(arr2,axis=0))
print(np.mean(arr2,axis=0))

