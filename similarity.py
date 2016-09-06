import numpy as np
filename ="similarity.csv"
adata = np.genfromtxt(filename,delimiter=',')
actual = adata[:,0]
predicted = adata[:,1]
n=len(actual)
rmse = np.linalg.norm(predicted-actual)/np.sqrt(n)
print "rmse"
print rmse

