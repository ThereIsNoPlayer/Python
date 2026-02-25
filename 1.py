import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 设置中文字体（改进版本）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者 ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建数据
x = np.array([5.1, 8.2, 11.5, 13.9, 15.1, 16.2, 19.6, 23.3]).reshape(-1, 1)
y = np.array([2.14, 4.62, 8.24, 11.24, 13.99, 16.33, 19.23, 28.74])

# 创建线性回归模型
model = LinearRegression()
model.fit(x, y)

# 获取模型参数
a = model.coef_[0]
b = model.intercept_
print(f"线性回归方程: y = {a:.4f}x + {b:.4f}")

# 预测值
y_pred = model.predict(x)

# 计算R²和MSE
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
print(f"R² 决定系数: {r2:.4f}")
print(f"MSE 均方误差: {mse:.4f}")

# 创建数据表格
data = pd.DataFrame({
    '气温温度': x.flatten(),
    '火灾影响面积': y,
    '预测面积': y_pred,
    '残差': y - y_pred
})
print("\n数据表格:")
# 设置小数位数，使表格更美观
pd.set_option('display.float_format', '{:.6f}'.format)
print(data.to_string(index=False))

# 绘制散点图和回归线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='实际数据点', s=50, zorder=5)
plt.plot(x, y_pred, color='red', label=f'回归线: y = {a:.2f}x + {b:.2f}', linewidth=2)

plt.xlabel('气温温度 (°C)', fontsize=12)
plt.ylabel('火灾影响面积 (km²)', fontsize=12)
plt.title('气温温度与火灾影响面积的线性回归分析', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# 修复标注部分的错误 - 使用更安全的方法
for i in range(len(x)):
    xi = x[i, 0]  # 获取标量值
    yi = y[i]
    plt.annotate(f'({xi:.1f}, {yi:.2f})',
                xy=(xi, yi),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.show()

# 绘制残差图
plt.figure(figsize=(10, 4))
residuals = y - y_pred
plt.scatter(x, residuals, color='green', s=50, zorder=5)
plt.axhline(y=0, color='red', linestyle='--', linewidth=1.5)
plt.xlabel('气温温度 (°C)', fontsize=12)
plt.ylabel('残差', fontsize=12)
plt.title('残差图', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 模型评估
print(f"\n模型评估:")
print(f"斜率 (a): {a:.4f}")
print(f"截距 (b): {b:.4f}")
print(f"决定系数 R²: {r2:.4f} (越接近1表示模型拟合越好)")
print(f"均方误差 MSE: {mse:.4f}")

# 预测示例
x_new = np.array([[10], [20], [25]])
y_new = model.predict(x_new)
print(f"\n预测示例:")
print(f"当气温为10°C时，预测火灾面积为: {y_new[0]:.2f} km²")
print(f"当气温为20°C时，预测火灾面积为: {y_new[1]:.2f} km²")
print(f"当气温为25°C时，预测火灾面积为: {y_new[2]:.2f} km²")