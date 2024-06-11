import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import pickle as pk
import umap
import numpy as np
from yellowbrick.cluster import kelbow_visualizer
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
import umap
from sklearn.metrics import davies_bouldin_score

import utils

embedding_tensor = pk.load(open(r'util\both_embedding_concat.pkl', 'rb'))
embeddings = embedding_tensor.numpy()
reduced = utils.UMAP_reduce(data=embeddings)
eps = 5
minPts = 8
clusterer = DBSCAN(eps=eps, min_samples=minPts)
clusterer:DBSCAN
cluster_labels = clusterer.fit_predict(reduced)
n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
print("Number of clusters:", n_clusters)

silhouette_avg = silhouette_score(reduced, cluster_labels)
calsinski_score = calinski_harabasz_score(reduced, cluster_labels)
davies_score = davies_bouldin_score(reduced, cluster_labels)
print(
    "For n_clusters =",
    n_clusters,
    "The average silhouette_score is :",
    silhouette_avg,
    "\nand calinski harabasz score is :",
    calsinski_score,
    "\nand davies score is :",
    davies_score,
    "\nreduced to ", reduced.shape[1], " dims"
)
