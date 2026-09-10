import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 2 * np.pi, 500)
y_cos = np.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_cos, label='cos(x)', color='blue', linewidth=2)
plt.title('余弦函数图像 (0 ~ 2π)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()


data = np.random.randn(1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('正态分布随机数直方图 (n=1000)')
plt.xlabel('数值')
plt.ylabel('频数')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

x = np.linspace(0, 2 * np.pi, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, axes = plt.subplots(2, 1, figsize=(8, 8))

axes[0].plot(x, y_sin, label='sin(x)', color='red', linewidth=2)
axes[0].set_title('正弦函数图像')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend()

axes[1].plot(x, y_cos, label='cos(x)', color='blue', linewidth=2)
axes[1].set_title('余弦函数图像')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend()

plt.tight_layout()
plt.show()