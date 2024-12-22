import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# AR数据
data2 = pd.read_csv('data5A_points.csv',header=None)

data2 = np.array(data2)

# SR数据
data3 = pd.read_csv('data5S_points.csv',header=None)

data3 = np.array(data3)

# IRT数据
data1 = pd.read_csv('n=50.csv',header=None)

data1 = np.array(data1)

# 定义单纯形顶点
vertices = np.array([
    [0.25, 1, 0],
    [0.5, 0, 0],
    [1, 0, 1],
    [0.75,1,1],
])

# 创建三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制单纯形
faces = [[vertices[j] for j in [0, 1, 2, 3]]]
poly3d = Poly3DCollection(faces, alpha=0.1, facecolor='gray')
ax.add_collection3d(poly3d)


# 绘制散点图IRT,AR,SR
ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2],  marker='+',c= 'red',label='IRT')

ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2],  marker='.',c= 'blue',label='AR')

ax.scatter(data3[:, 0], data3[:, 1], data3[:, 2],  marker='*',c= 'black',label='SR')

ax.legend(title="Point Types", loc="upper left")

# 设置坐标轴标签
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')

# 显示图形
plt.show()
