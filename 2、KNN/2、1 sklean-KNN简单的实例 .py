from sklearn import neighbors
from sklearn import datasets
'''
    程序说明:
        采用sklean中自带的判断花的种类例子来判断一个花的种类
            数据集 ： 一个150行的数据，拥有5列（属性）和一列类别
            150个实例、
            特征属性：萼片长度，萼片宽度，花瓣长度，花瓣宽度(sepal length, sepal width, petal length and petal width）
            类别（标记）：Iris setosa, Iris versicolor, Iris virginica.
    更多的文档说明 请查看sklearn的knn 算法文档（百度 knn sklean）
        https://scikit-learn.org/stable/modules/neighbors.html

'''
# 加载sklearn自带的K临近分类器
knn = neighbors.KNeighborsClassifier()

# 加载sklearn自带的数据集
iris = datasets.load_iris()
print(iris)

# 建模，在python算法中基本都有一个fit（） 用于建立模型。KNN模型中有两个参数：自带的数据字典中的数据集、字典中的类别
knn.fit(iris.data, iris.target)

# 预测 'target_names': array(['setosa', 'versicolor', 'virginica']
predictLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(predictLabel)  # setosa


