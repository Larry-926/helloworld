from numpy import *
import matplotlib.pyplot as plt
import regression


''' 8.1 '''
xArr,yArr=regression.loadDataSet('ex0.txt')  # >>>xArr[0:2]   [[1.0, 0.067732], [1.0, 0.42781]]
#print(xArr[0:2],yArr[0:2]) #[[1.0, 0.067732], [1.0, 0.42781]] [3.176513, 3.816464]

ws=regression.standRegres(xArr,yArr) #由样本数据及原始标签计算回归系数w
xMat=mat(xArr)
yMat=mat(yArr)
yHat=xMat*ws #再由原始样本特征值矩阵xMat和算出的回归系数w计算预测标签值yHat

#绘制原始数据图像
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0]) #flatten()是numpy下的一个函数，返回多维数组/矩阵的一维副本;运算.A[0]将mat转换为array后，取第0轴;运算.T表示取转置
'''
>>> A=xMat[:,1][0:2].flatten().A
>>> A
array([[0.067732, 0.42781 ]])
>>> A=xMat[:,1][0:2].flatten().A[0]
>>> A
array([0.067732, 0.42781 ])

'''

#绘制计算出的最佳拟合直线
xCopy=xMat.copy()
xCopy.sort(0) #plot绘图，数据点需为有序
yHat=xCopy*ws
ax.plot(xCopy[:,1],yHat,'y',label='regress line',)
plt.xlabel('x') #
plt.ylabel('y')
plt.legend()
plt.show()

#计算预测值和真实值的相关系数，用以评价拟合效果
#采用numpy提供的corrcoef()来计算相关性
yHat=xMat*ws
ralateRate=corrcoef(yHat.T,yMat)
print(ralateRate)
'''
[[1.         0.98647356]
 [0.98647356 1.        ]]
 '''


