import pickle as pk
from sklearn.cluster import Birch,KMeans
import numpy as np
import utils
import pandas as pd


num_runs = 1
n_clusters = 6
embedding_tensor = pk.load(open(r'util\gensim_title.pkl', 'rb'))
embeddings = embedding_tensor
reduced = utils.UMAP_reduce(data=embeddings)
for _ in range(num_runs):
    # clustering = Birch(n_clusters=KMeans(init='k-means++', n_clusters=n_clusters))
    # clustering = Birch(n_clusters=n_clusters)
    clustering = Birch(n_clusters=None)
    cluster_labels = clustering.fit_predict(reduced)
    utils.print_eval_scores(reduced, cluster_labels, n_clusters)

    cluster_sizes = np.bincount(cluster_labels)
    for cluster_id, size in enumerate(cluster_sizes):
        print(f"Cluster {cluster_id}: {size} samples")

utils.plot_similarity_mat(reduced, cluster_labels)

