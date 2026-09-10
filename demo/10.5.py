# 1.	创建一个 3×3 的全 1 数组，每个元素乘以 5，打印结果。
# 2.	创建两个相同形状的随机数组，完成加减乘除四种运算。
# 3.	定义 2×3 和 3×2 的两个矩阵，计算矩阵乘法并打印结果。
# 4.	对一个随机数组，计算所有元素的平方根并输出。
import numpy as np

arr=np.ones((3,3))
arr1=arr*5
print(arr1)

a2=np.random.randint(1,10,(3,3))
a3=np.random.randint(1,10,(3,3))
print(a2)
print(a3)
print(a2+a3)
print(a2-a3)
print(a2*a3)
print(a2/a3)


a4=np.random.randint(1,10,(2,3))
a5=np.random.randint(1,10,(3,2))
print(a4)
print(a5)
print(np.dot(a4,a5))

arr4 = np.random.randint(1, 50, size=(3, 3))
sqrt_arr = np.sqrt(arr4)
print(sqrt_arr)