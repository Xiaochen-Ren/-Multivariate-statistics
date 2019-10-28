# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 09:41:51 2019

@author: RenXiaochen
"""

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
dataset = datasets.load_iris()
x = dataset.data
target = dataset.target

plot_data = x[:,0:2]
#散点图
plt.scatter(plot_data[:,0],plot_data[:,1])
plt.xlabel('x')#x轴标签
plt.ylabel('y')#y轴标签
plt.title('dot')#设置标题
plt.show()

#折线图
plt.plot(range(0,50),plot_data[0:50,0])
plt.xticks(rotation=45)#旋转x轴刻度
plt.xlabel('x')#x轴标签
plt.ylabel('y')#y轴标签
plt.title('line')#设置标题
plt.show()

#柱状图
pie_data = {}
pie_list = []
target=list(target)
set_temp =  set(target)
for item in set_temp:
    pie_data.update({item:target.count(item)})
    pie_list.append([item,target.count(item)])
pie_list = np.array(pie_list)
plt.bar(range(len(pie_list[:,1])), pie_list[:,1])
plt.show()

#箱型图
plt.boxplot(plot_data[:,0])
plt.show()

#饼状图
pie_data = {}
pie_list = []
target=list(target)
set_temp =  set(target)
for item in set_temp:
    pie_data.update({item:target.count(item)})
    pie_list.append([item,target.count(item)])
pie_list = np.array(pie_list)
plt.pie(pie_list[:,1],labels=pie_list[:,0])
