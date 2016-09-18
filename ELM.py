import numpy as np
def elm_train(TrainingData, ELM_Type, NumberofHideen):
	T = TrainingData[:,0]
	P = TrainingData[:,1:TrainingData.shape[1]]
	labels = np.array(list(set(T)))
	newT = T[:]
	j = 0
	while j<len(T):
		i = 0
		while i<len(labels):
			if T[j]==labels[i]:
				newT[j]=i
				break
			else:
				i = i+1
		j = j+1
	target = np.zeros([len(T),len(labels)])
	target = target-1
	for i in range(0,len(labels)):
		target[i,i]=1
	print target

m = np.array([[2,2,3],[3,3,4],[2,3,3]])
elm_train(m,0,0)