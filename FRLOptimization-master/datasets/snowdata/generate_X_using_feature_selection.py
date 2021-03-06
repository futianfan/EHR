
# python generate_X_using_feature_selection.py $n tmp snow.X_new

import sys
n_dim = int(sys.argv[1])
reduce_dim = 20
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

Y_file = open('snow.Y', 'r')
lines = Y_file.readlines()
n_sample = len(lines)
Y = np.zeros((n_sample,))
for i, line in enumerate(lines):
	Y[i] = int(line)

X = np.zeros((n_sample, n_dim),dtype = np.float32)

with open(sys.argv[2], 'r') as fin:
	lines = fin.readlines()
	for indx, line in enumerate(lines):
		line = line.split()
		line = [int(i) for i in line]
		for i in range(n_dim):
			if i in line:
				X[indx,i] = 1


X_new = SelectKBest(chi2, k=reduce_dim).fit_transform(X, Y)
print(X_new.shape)

index = []
for i in range(reduce_dim):
	col = X_new[:,i]
	try:
		begin_num = index[-1]
	except:
		begin_num = 0
	for j in range(begin_num, n_dim):
		if (col == X[:,j]).all():
			index.append(j)
			break 

with open(sys.argv[3], 'w') as fout:
	for i in range(n_sample):
		str_all = ['F_' + str(index[j])+ '=yes'  if X_new[i,j] == 1 else 'F_' + str(index[j]) + '=no' for j in range(reduce_dim)]
		str_all = ' '.join(str_all)
		fout.write(str_all + '\n')
		#  'F_' + str(i) + '=yes'





