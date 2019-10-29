x1=matrix(rnorm(100,mean=0,sd=0.3),ncol=2)#生成正态数据
x2=matrix(rnorm(100,mean=1,sd=0.3),ncol=2)#生成正态数据
x=rbind(x1,x2)#拼接数据
cl<-kmeans(x,2)#k均值聚类
#绘图
pch1=rep("1",10000)
pch2=rep("2",10000)
plot(x,col=cl$ cluster,pch=c(pch1,pch2))
points(cl$ centers,col=c(2,3),pch="* ",cex=3)
