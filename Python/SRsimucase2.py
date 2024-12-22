import numpy as np
import csv

def generate_samples(num_samples):
    samples = []
    while len(samples) < num_samples:
        # 随机生成x1和x2的值
        x1 = np.random.uniform(0, 1)
        x2 = np.random.uniform(0, 1)
        
        # 使用约束条件计算x3的值
        x32 = (1 - 4*x1**2 - 9*x2**2) 
        
        # 检查x32是否在有效范围内
        if 0 < x32 < 1:
            samples.append((x1, x2, x32**(0.5)))
    
    return samples

# 生成数据点
data92S_points = generate_samples(90)
print(data92S_points)

# 写入CSV文件
with open('data92S_points.csv', 'w', newline='') as csvfile:
    fieldnames = ['x1', 'x2', 'x3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for point in data92S_points:
        writer.writerow({'x1': point[0], 'x2': point[1], 'x3': point[2]})