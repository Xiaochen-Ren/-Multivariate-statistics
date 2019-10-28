# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:24:13 2019

@author: RenXiaochen
"""

import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.normal(loc=0,scale=0.3,size=(1000,2))
x2 = np.random.normal(loc=1,scale=0.3,size=(1000,2))
x = np.vstack((x1, x2))

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=1)
kmeans.fit(x)
y_pre = kmeans.predict(x)
col=[]
for i in range(len(y_pre)):
    if y_pre[i] ==0:
        #  第i行数据，及returnMat[i:,0]及矩阵的切片意思是:i：i+1代表第i行数据,0代表第1列数据
        col.append('red')
    if y_pre[i] == 1:
        col.append('green')



plt.scatter(x[:,0],x[:,1],color=col,s=4)

plt.scatter(np.delete(kmeans.cluster_centers_, [1], axis = 1),np.delete(kmeans.cluster_centers_, [0], axis = 1),s=50,marker='*',color='black')
#for i in range(len(y_pre)):
#    if y_pre[i] ==0:
#        #  第i行数据，及returnMat[i:,0]及矩阵的切片意思是:i：i+1代表第i行数据,0代表第1列数据
#        plt.scatter(x[i:i+1, 0], x[i:i+1 ,1], color = 'red',s=4)
#    if y_pre[i] == 1:
#        plt.scatter(x[i:i+1, 0], x[i:i+1, 1], color='green',s=4)
plt.show()
