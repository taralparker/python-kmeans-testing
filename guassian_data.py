from numpy.random import multivariate_normal
from numpy import vstack
import numpy as np
from matplotlib import pyplot as plt
import prettyplotlib as ppl

center1 = np.array([1,1])
center2 = np.array([-1,-1])
center3 = np.array([-1,1])

var_scale = 0.01

sample_size = 1000

x1 = multivariate_normal(center1,var_scale*np.eye(2),sample_size)
x2 = multivariate_normal(center2,var_scale*np.eye(2),sample_size)
x3 = multivariate_normal(center3,var_scale*np.eye(2),sample_size)

X = vstack((x1,x2,x3))

#np.savetxt("./test_clusters/guassian3.csv",X,delimiter=",")
ppl.scatter(X[:,0],X[:,1])
plt.show()
