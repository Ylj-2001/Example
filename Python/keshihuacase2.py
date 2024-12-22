import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# AR数据
data2 = pd.read_csv('data102A_points.csv',header=None)

data2 = np.array(data2)

# SR数据
data3 = pd.read_csv('data102S_points.csv',header=None)

data3 = np.array(data3)

# IRT数据
data1 = pd.read_csv('data102I_points.csv',header=None)

data1 = np.array(data1)

# 创建一个点网格
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)

# 椭球的参数方程
x = (1/2)*np.cos(u) * np.sin(v) 
y = (1/3)*np.sin(u) * np.sin(v) 
z = np.cos(v) 

# 创建一个掩码来筛选出只在第一象限内的点
mask = (x > 0) & (x < 1) & (y > 0) & (y < 1) & (z > 0) & (z < 1)

# 应用掩码
x = x[mask]
y = y[mask]
z = z[mask]

# 将点变形为适合绘制表面的格式
x = x.reshape((len(x), 1))
y = y.reshape((len(y), 1))
z = z.reshape((len(z), 1))

# 绘制椭球
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面
ax.plot_trisurf(x.flatten(), y.flatten(), z.flatten(), color='gray', alpha=0.4, linewidth=0.3)

# 设置轴限制
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)


# 绘制散点图IRT,AR,SR
ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2],  marker='+',c= 'red',label='IRT')

ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2],  marker='.',c= 'blue',label='AR')

ax.scatter(data3[:, 0], data3[:, 1], data3[:, 2],  marker='*',c= 'black',label='SR')

ax.legend(title="Point Types", loc="upper left")

# 标签和显示图形
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
plt.show()
