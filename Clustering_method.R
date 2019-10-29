x=iris
target=x[,5:5]
iris_train_pca <- princomp(x[,1:4])#主成分分析降维
new_data <- predict(iris_train_pca, x[,-5])[,1:2]
set.seed(20)#设置随机种子
cl<-kmeans(new_data,3)#kmeans聚类
#绘图
split.screen(c(2,1))
screen(1)
p1<-plot(new_data,col=cl$ cluster,sub="k-means聚类")
screen(2)
p2<-plot(new_data,col=target,sub="标签")
#计算准确率
num_true<-0
for(i in 1:length(target))
{
  if(cl$ cluster[i]==1 && target[i]=='setosa')
    {
    num_true=num_true+1
    }
  if(cl$ cluster[i]==2 && target[i]=='versicolor')
    {
    num_true=num_true+1
    }
  if(cl$ cluster[i]==3 && target[i]=='virginica')
    {
    num_true=num_true+1
    }
}
print(paste("The accuracy is :",as.character(num_true/length(target))))
