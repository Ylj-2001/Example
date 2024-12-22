import numpy as np
from scipy.integrate import nquad
from shapely.geometry import Point, Polygon
import pandas as pd


#######模拟数据
# AR数据
data2 = pd.read_csv('data10A_points.csv',header=None)
data2 = np.array(data2)
# SR数据
data3 = pd.read_csv('data10S_points.csv',header=None)
data3 = np.array(data3)
# IRT数据
data1 = pd.read_csv('n=100.csv',header=None)
data1 = np.array(data1)

n = 100

#######试验区域与子区域定义
# D
vertices = np.array([
    [0.25, 1, 0],
    [0.5, 0, 0],
    [1, 0, 1],
    [0.75,1,1],
])
#D1
vertices1 = np.array([
    [0.5, 1, 0.5],
    [0.625, 0.5, 0.5],
    [0.875, 0.5, 1],
    [0.75,1,1],
])
#D2
vertices2 = np.array([
    [0.625, 0.5, 0.5],
    [0.75,0,0.5],
    [1, 0, 1],
    [0.875, 0.5, 1],
])
#D3
vertices3 = np.array([
    [0.25, 1, 0],
    [0.375,0.5,0],
    [0.625, 0.5, 0.5],
    [0.5, 1, 0.5],
])
#D4
vertices4 = np.array([
    [0.375,0.5,0],
    [0.5, 0, 0],
    [0.75, 0, 0.5],
    [0.625, 0.5, 0.5],
])

#########计算各个区域的面积
# 计算三角形面积的函数
def triangle_area(vertices):
    # 使用叉积法计算三角形面积
    a = vertices[0]
    b = vertices[1]
    c = vertices[2]
    ab = b - a
    ac = c - a
    area = 0.5 * np.linalg.norm(np.cross(ab, ac))
    return area
# 计算超立方体中四个顶点构成的平面的面积
def calculate_plane_area(vertices):
    # vertices 是一个 4x3 的矩阵，其中每一行代表一个顶点
    if vertices.shape != (4, 3):
        raise ValueError("vertices should be a 4x3 matrix")
    # 将四边形分割成两个三角形
    tri1 = vertices[:3, :]
    tri2 = vertices[[0, 2, 3], :]
    area1 = triangle_area(tri1)
    area2 = triangle_area(tri2)
    return area1 + area2
# 定义区域面积
def volume_of_D(vertices):
    ar = calculate_plane_area(vertices)
    return ar  
# 计算子域体积
def volume_of_Dk(vertices):
    ar = calculate_plane_area(vertices)
    return (ar/4)   # 均匀划分

datal = [data1,data2,data3]
for data in datal :
########计算N(Dk)/N(D)
# 统计落在D1内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 polygon = Polygon([(v[0], v[1]) for v in vertices1])
 count_inside1 = 0
 for point in data:
    p = Point(point)
    if polygon.contains(p) or polygon.exterior.contains(p):
        count_inside1 += 1
 print(f"Number of points inside the polygon: {count_inside1}")
 p1 = count_inside1 / n

# 统计落在D2内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 polygon = Polygon([(v[0], v[1]) for v in vertices2])
 count_inside2 = 0
 for point in data:
    p = Point(point)
    if polygon.contains(p) or polygon.exterior.contains(p):
        count_inside2 += 1
 print(f"Number of points inside the polygon: {count_inside2}")
 p2 = count_inside2 / n

# 统计落在D3内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 polygon = Polygon([(v[0], v[1]) for v in vertices3])
 count_inside3 = 0
 for point in data:
    p = Point(point)
    if polygon.contains(p) or polygon.exterior.contains(p):
        count_inside3 += 1
 print(f"Number of points inside the polygon: {count_inside3}")
 p3 = count_inside3 / n

# 统计落在D4内的点的数量
# 创建四边形多边形对象（仅考虑x和y坐标）
 polygon = Polygon([(v[0], v[1]) for v in vertices4])
 count_inside4 = 0
 for point in data:
    p = Point(point)
    if polygon.contains(p) or polygon.exterior.contains(p):
        count_inside4 += 1
 print(f"Number of points inside the polygon: {count_inside4}")
 p4 = count_inside4 / n

 sum1 = (abs(p1-0.25)** (2)+abs(p2-0.25)** (2)+abs(p3-0.25)** (2)+abs(p4-0.25)** (2)) / 4

########### 计算 CCD_2
 CCD_p = (sum1 ** (1/2))

 print("中心复合差异 CCD_p(P):", CCD_p)