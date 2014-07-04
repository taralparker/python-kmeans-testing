import numpy as np
from matplotlib import pyplot as plt
from math import pi
import os
if not os.path.isdir("./test_clusters"):
    os.mkdir("./test_clusters")

def generate_square(size):
	x = np.random.uniform(-1,1,size)
	y = np.random.uniform(-1,1,size)
	output = open('./test_clusters/square_cluster.csv','w')
	i = 0
	while i < len(x):
		output.write(str(x[i]) + ',' + str(y[i]) + '\n')
		i += 1
#	plt.scatter(x,y)
#    	plt.show()

def generate_circle(size):
	x = np.zeros(size)
	y = np.zeros(size)
	u = np.random.rand(size)+np.random.rand(size)
	u[u>1] = 2-u[u>1]
	t = np.random.uniform(0,2*pi,size)
	x = u*np.cos(t)
	y = u*np.sin(t)
	output = open('./test_clusters/circle_cluster.csv','w')
	i = 0
	while i < len(x):
		output.write(str(x[i]) + ',' + str(y[i]) + '\n')
		i += 1
#	plt.scatter(x,y)
#	plt.show()

def generate_hypercube(size):
	x = np.random.rand(size)
       	y = np.random.rand(size)
       	z = np.random.rand(size)
       	w = np.random.rand(size)
        output = open('./test_clusters/hypercube_cluster.csv','w')
	i = 0
	while i < len(x):
		output.write(str(x[i]) + ',' + str(y[i]) + ',' + str(z[i]) + ',' + str(w[i]) + '\n')
		i += 1
#	plt.scatter(x,y)
#   	plt.show()


SAMPLE_SIZE = 100000
generate_square(SAMPLE_SIZE)
generate_circle(SAMPLE_SIZE)
generate_hypercube(SAMPLE_SIZE)    

