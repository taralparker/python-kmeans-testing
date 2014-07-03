import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import prettyplotlib as plot 


X = np.loadtxt('./test_clusters/square_cluster.csv', delimiter = ',')


estimators = {	'k_means_square_01': KMeans(n_clusters=1),
		'k_means_square_02': KMeans(n_clusters=2),
		'k_means_square_03': KMeans(n_clusters=3),
		'k_means_square_04': KMeans(n_clusters=4),
		'k_means_square_05': KMeans(n_clusters=5),
		'k_means_square_06': KMeans(n_clusters=6),
		'k_means_square_07': KMeans(n_clusters=7),
		'k_means_square_08': KMeans(n_clusters=8),
		'k_means_square_09': KMeans(n_clusters=9),
		'k_means_square_10': KMeans(n_clusters=10),
		'k_means_square_11': KMeans(n_clusters=11),
		'k_means_square_12': KMeans(n_clusters=12),
		'k_means_square_13': KMeans(n_clusters=13),
		'k_means_square_14': KMeans(n_clusters=14),
		'k_means_square_15': KMeans(n_clusters=15),
		'k_means_square_16': KMeans(n_clusters=16),
		'k_means_square_17': KMeans(n_clusters=17),
		'k_means_square_18': KMeans(n_clusters=18),
		'k_means_square_19': KMeans(n_clusters=19),
		}


for name, est in estimators.iteritems():
	pl.clf()
	est.fit(X)
	labels = est.labels_
	plot.scatter(X[:, 0], X[:, 1], c=labels.astype(np.float))
        pl.title(name)
	pl.savefig('./figs/' + name + '.png')

