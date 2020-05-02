from pyclustering.samples.definitions import FAMOUS_SAMPLES
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.fcm import fcm
from pyclustering.utils import read_sample



# load list of points for cluster analysis

sample = read_sample(FAMOUS_SAMPLES.SAMPLE_OLD_FAITHFUL)

# initialize
initial_centers = kmeans_plusplus_initializer(sample, 2, kmeans_plusplus_initializer.FARTHEST_CENTER_CANDIDATE).initialize()


# create instance of Fuzzy C-Means algorithm
fcm_instance = fcm(sample, initial_centers)


# run cluster analysis and obtain results
fcm_instance.process()
clusters = fcm_instance.get_clusters()
centers = fcm_instance.get_centers()


# visualize clustering results
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, sample)
visualizer.append_cluster(centers, marker='*', markersize=10)
visualizer.show()