# coding = utf-8
"""
    1、导入模块
"""
import csv
##sklearn对输入数据的格式有一定要求，只支持整型的数据，不支持类型数据，故需要对输入数据进行转换；
from sklearn.feature_extraction import DictVectorizer   #用于将csv数据中字符数据转化为整形数据
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

"""
    程序说明：
        参照 ：https://blog.csdn.net/akadiao/article/details/77800909
        在pycharm中使用Anaconda，解决了各种包的安装
        本次使用的是Python机器学习的库：scikit-learn 来实现
            关于决策树scikit-learn已经实现好了，我们只需要去调用相应的方法就好了
        决策树对于输入的值（属性、标记）必须是数值型的值
            比如年龄分为 youth mid senor，对于一条数据有属性age（ youth mid senor）：youth 、income
            (high、medium、low)：high；使用数值型来表示为：
            youth   mid senor   high    medium  low
            1       0    0      1        0    0
        数值型: 对于一个属性分为yes（1）、no（0）来显示

"""

"""
    2、从csv文件中读取数据
"""
allElectronicsData = open(r'D:\Python\pythonProjectHome\机器学习\决策树\AllElectronics.csv', 'r')
reader = csv.reader(allElectronicsData)  ##csv自带的reader可以按行读取allElectronicsData中的数据
headers = next(reader)                   # reader.next() 注意这是 python2 中的写法，3 中 reader 已经没了 next 属性，需要单独调用 next 方法
print(headers)    # ['RID', 'age', 'income', 'student', 'credit_rating', 'class_buys_computer']

"""
    3、数据预处理： 
        sklearn要求数据输入的特征值（属性）features以及输出的类，必须是数值型的值，而不能是类别值（如income属性中的high、medium、low）。
"""

featureList = []  # 特征集合
labelList = []    # 标记集合

for row in reader:  # 循环的时候 row 代表每一行的数据，是一个集合 ['1', 'youth', 'high', 'no', 'fair', 'no']
    labelList.append(row[len(row)-1])   # 添加标记，每一行的最后一个值
    rowDict = {}
    for i in range(1, len(row)-1): # 对每一行数据转化为 特性：特征值 的字典集合
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict) # 将每一行的字典数据（特性：特征值） 集合添加到特征集合中

###  list中的每一个字典对应原始数据中的一行数据 <featureList[0]对应第1行原始数据>
print(featureList)

"""
    将数据进行编码处理，将字符型的数据进行one-hot编码转化为0、1： 
    即age中的youth对应001、middle_aged对应100、senior对应010；
"""
# Vetorize features  使用 sklearn 的 feature_extraction （特征提取） 提供的 DictVectorizer() 将 特征值集合原来字符型数据转换为数值型
# 注意：DictVectorizer 中是将数据的属性以及其属性值按照字母的顺序来排列的， 比如 	income、age， 那么 排列的时候 age 在前面
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX: " + str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

# Vetorize class lables
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))


# Using decision tree for classification  使用决策树作为分类器
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf: " + str(clf))

# Visualize model 可视化模型 : 将获得的决策树写入dot文件：
with open("allElectronicInformationGainOri.dot", 'w') as f :
    f = tree.export_graphviz()
