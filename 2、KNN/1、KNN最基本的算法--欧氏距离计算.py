# coding = utf-8
import math
"""
    程序说明：
        这个程序实现了KNN计算两个特征值之间的距离，使用了 python 提供的 math模块俩实现，计算的公式是欧氏距离（n维空间下）
        二维： dis = sqrt( (x1-x2)^2 + (y1-y2)^2 )
        三维：dis=sqrt( (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 )
"""

def ComputerEuclideanDistance(x1, y1, x2, y2):
    d = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
    return d


d_ag = ComputerEuclideanDistance(3, 104, 18, 90)
print(d_ag)