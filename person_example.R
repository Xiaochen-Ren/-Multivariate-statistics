orin_data <- read.csv('data.csv')
person_data <- read.csv('person_data.csv')
data <- orin_data[,2:5]
for(i in 1:length(data))
{
  person_num <- person_data[i,2]
  for(j in 1:4)
  {
    data[i,j] <- data[i,j]/person_num
  }
}

set.seed(0)
ari <- array( data = NA, dim = 10, dimnames = NULL)
for(i in 1:10)
{
  cl <- kmeans(data,i)
  #print(cl$betweenss/cl$totss)
  ari[i] <- cl$betweenss/cl$totss
}
plot(1:10,ari,pch="+",type='b',col='red',xlab='类数',ylab='R^2')
#发现分三类时效果最好

#先聚类后降维
cl <- kmeans(data,3)
clu <- cl$cluster
#data$cluster <- clu
iris_train_pca <- princomp(data)
new_data <- predict(iris_train_pca, data)[,1:2]
plot(new_data,col=cl$ cluster,sub="k-means聚类",xlab='X',ylab='Y')


#先降维后聚类
iris_train_pca <- princomp(data)
new_data <- predict(iris_train_pca, data)[,1:2]
cl <- kmeans(new_data,3)
clu <- cl$cluster
#data$cluster <- clu
plot(new_data,col=cl$ cluster,sub="k-means聚类",xlab='X',ylab='Y')

