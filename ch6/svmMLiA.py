from numpy import *
from time import sleep

def loadDataSet(fileName):
	dataMat=[];labelMat=[]
	fr=open(fileName)
	for line in fr.readlines():
		lineArr=line.strip().split('\t')
		dataMat.append([float(lineArr[0]),float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat,labelMat

def selectJrand(i,m):
	j=i
	while(j==i):
		j=int(random.uniform(0,m))
	return j

def clipAlpha(aj,H,L):
	if aj>H:
		aj=H 
	if aj<L:
		aj=L 
	return aj

def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
	dataMatrix=mat(dataMatIn);labelMat=mat(classLabels).transpose()
	b=0
	m,n=shape(dataMatrix)
	alphas=mat(zeros(m,1))
	iter=0
	
