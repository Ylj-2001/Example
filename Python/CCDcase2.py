import numpy as np
from scipy.integrate import nquad
from shapely.geometry import Point, Polygon
import pandas as pd


#######模拟数据
# AR数据
data2 = pd.read_csv('data102A_points.csv',header=None)
data2 = np.array(data2)
# SR数据
data3 = pd.read_csv('data102S_points.csv',header=None)
data3 = np.array(data3)
# IRT数据
data1 = pd.read_csv('data102I_points.csv',header=None)
data1 = np.array(data1)

n = 100

datal =[data1,data2,data3]
for data in datal :
########计算N(Dk)/N(D)
# 统计落在D1内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 count_inside1 = 0
 for i in range(n):
    if (0.75 < data[i,2] < 1) :
        count_inside1 += 1
 print(f"Number of points inside the polygon: {count_inside1}")
 p1 = count_inside1 / n

# 统计落在D2内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 count_inside2 = 0
 for i in range(n):
    if (0.5 < data[i,2] < 0.75) :
        count_inside2 += 1
 print(f"Number of points inside the polygon: {count_inside2}")
 p2 = count_inside2 / n

# 统计落在D3内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 count_inside3 = 0
 for i in range(n):
    if (0.25 < data[i,2] < 0.5) :
        count_inside3 += 1
 print(f"Number of points inside the polygon: {count_inside3}")
 p3 = count_inside3 / n

# 统计落在D4内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 count_inside4 = 0
 for i in range(n):
    if (0 < data[i,2] < 0.25) :
        count_inside4 += 1
 print(f"Number of points inside the polygon: {count_inside4}")
 p4 = count_inside4 / n

 sum1 = (abs(p1-(1/16))** (2)+abs(p2-(3/16))** (2)+abs(p3-(5/16))** (2)+abs(p4-(7/16))** (2)) / 4

########### 计算 CCD_2
 CCD_p = (sum1 ** (1/2))

 print("中心复合差异 CCD_p(P):", CCD_p)