import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import prettyplotlib as ppl 
import os
import sys


if not os.path.isdir("./test_clusters"):
    print "./test_clusters does not exist"
    sys.exit()
if not os.path.isdir("./figs"):
    os.mkdir("./figs")


X = np.loadtxt('./test_clusters/square_cluster.csv', delimiter = ',')


def alpha(K,n):
    if K==1 and n > 1:
        return 1.-3./(4.*n)
    else:
        return alpha(K-1,n)+(1.-alpha(K-1,n))/6.


def f(K,S,n):
    if K==0:
        return 1
    elif S[K-1] != 0:
        return S[K]/(alpha(K,n)*S[K-1])
    elif S[K-1] == 0:
        return 1
    else:
        print "Error in f(K,S,n)"
        sys.exit()


estimators = {  'k_means_01': KMeans(n_clusters=1),
        'k_means_02': KMeans(n_clusters=2),
        'k_means_03': KMeans(n_clusters=3),
        'k_means_04': KMeans(n_clusters=4),
        'k_means_05': KMeans(n_clusters=5),
        'k_means_06': KMeans(n_clusters=6),
        'k_means_07': KMeans(n_clusters=7),
        'k_means_08': KMeans(n_clusters=8),
        'k_means_09': KMeans(n_clusters=9),
        'k_means_10': KMeans(n_clusters=10),
        'k_means_11': KMeans(n_clusters=11),
        'k_means_12': KMeans(n_clusters=12),
        'k_means_13': KMeans(n_clusters=13),
        'k_means_14': KMeans(n_clusters=14),
        'k_means_15': KMeans(n_clusters=15),
        'k_means_16': KMeans(n_clusters=16),
        'k_means_17': KMeans(n_clusters=17),
        'k_means_18': KMeans(n_clusters=18),
        'k_means_19': KMeans(n_clusters=19),
        }


S=np.zeros(19)

for name, est in estimators.iteritems():
#   pl.clf()
    km = est.fit(X)
    labels = est.labels_
    S[est.n_clusters-1] = km.inertia_
#   plot.scatter(X[:, 0], X[:, 1], c=labels.astype(np.float))
#   pl.title(name)
#   pl.savefig('./figs/' + name + '.png')

output = open('eval_square_scikit.txt','w')
for i in xrange(19):
    print str(i+1) + " " + str(f(i,S,2))
    output.write(str(i+1) + " " + str(f(i,S,2)) + '\n')

    

