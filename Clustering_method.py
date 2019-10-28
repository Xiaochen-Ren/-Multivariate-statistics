# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:54:28 2019

@author: RenXiaochen
"""

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
dataset = datasets.load_iris()
x = dataset.data
target = dataset.target

#主成分分析
from sklearn.decomposition import PCA
model = PCA(n_components=2)
data_pca_dim = model.fit_transform(x)




#kmeans
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(data_pca_dim)
y_pre = kmeans.predict(data_pca_dim)
#kmeans.score(x)
index_1 = np.where(y_pre==1)
index_2 = np.where(y_pre==2)
for i in range(len(index_1)):
    y_pre[index_1[i]] = 2
    
for i in range(len(index_2)):
    y_pre[index_2[i]] = 1
    
fig = plt.figure()
axes = fig.add_subplot(221)

for i in range(len(y_pre)):
    if y_pre[i] ==0:
        #  第i行数据，及returnMat[i:,0]及矩阵的切片意思是:i：i+1代表第i行数据,0代表第1列数据
        axes.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1 ,1], color = 'red')
    if y_pre[i] == 1:
        axes.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1, 1], color='green')
    if y_pre[i] == 2:
        axes.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1, 1], color='black')

axes_ori = fig.add_subplot(222)
for i in range(len(target)):
    if target[i] ==0:
        #  第i行数据，及returnMat[i:,0]及矩阵的切片意思是:i：i+1代表第i行数据,0代表第1列数据
        axes_ori.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1 ,1],color = 'red')
    if target[i] == 1:
        axes_ori.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1, 1], color='green')
    if target[i] == 2:
        axes_ori.scatter(data_pca_dim[i:i+1, 0], data_pca_dim[i:i+1, 1], color='black')



plt.show()

accuracy_rate = np.size(np.where((target - y_pre)==0))/len(x)
print("The accuracy is :" + str(accuracy_rate))
