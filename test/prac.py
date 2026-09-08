import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
b=a.reshape(3,5)
print(b)

plt.plot([1,2,3],[4,5,6])
plt.scatter([1,2,3],[4,5,6])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
plt.show()