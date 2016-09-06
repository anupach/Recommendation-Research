import numpy as np
filename ="collaborative_rms.csv"
adata = np.genfromtxt(filename,delimiter=',')
#print adata.shape
#rint adata.size
#print adata[0,0]
#print adata[0,:]
#print np.max(adata[:,0])
#print np.max(adata[:,1])
#actual_mean = np.mean(adata[:,0])
#print actual_mean
#predicted_mean = np.mean(adata[:,1])
#print predicted_mean
actual = adata[:,0]
predicted = adata[:,1]
n=len(actual)
rmse = np.linalg.norm(predicted-actual)/np.sqrt(n)
print "rmse"
print rmse

