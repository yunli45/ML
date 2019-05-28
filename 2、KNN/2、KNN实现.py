import csv
import random
import math
import operator

'''
    程序说明:
        自己写一个实现KNN的算法，判断一个花的种类
            数据集 ： 一个150行的数据，拥有5列（属性）和一列类别
            150个实例、
            特征属性：萼片长度，萼片宽度，花瓣长度，花瓣宽度(sepal length, sepal width, petal length and petal width）
            类别（标记）：Iris setosa, Iris versicolor, Iris virginica.
'''

# 第一步： 加载数据(数据是从网上下载下来的，和sklean中的数据集是一样的)
def loadDataset(filename, split, trainingSet = [], testSet = []):
    # 以csv格式来加载：以逗号分隔符
    with open(filename, 'rb') as f:
        lines = f.read(f)
        dataSet = list(lines)






if __name__ == '__main__':
    main()