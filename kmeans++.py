import pickle as pk
from yellowbrick.cluster import kelbow_visualizer
import utils
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

embedding_tensor = pk.load(open(r'util\gensim_abstract.pkl', 'rb'))

embeddings = embedding_tensor
reduced = utils.UMAP_reduce(data=embeddings)
elbow_M = kelbow_visualizer(KMeans(init='k-means++'), X=reduced, k=(2, 15))

n_clusters = 5
# num_runs = 1
# k_results = {key: None for key in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}
#
# for c_i in k_results:
#     scores = (0, 0, 0)
#     for _ in range(num_runs):
#         kmeans = KMeans(init='k-means++', n_clusters=c_i)
#         cluster_labels = kmeans.fit_predict(reduced)
#         kmeans: KMeans
#         cluster_dict = {}
#         for i, label in enumerate(cluster_labels):
#             Add data point to the corresponding cluster in the dictionary
#             if label not in cluster_dict:
#                 cluster_dict[label] = []
#             cluster_dict[label].append(i)
#         utils.print_eval_scores(reduced, cluster_labels, c_i)
#
#     k_results[c_i] = scores
# print(reduced.shape[1])
# path = r'modares_papers\articles_modares.csv'
# utils.print_clustered_papers(n_clusters, KMeans(init='k-means++', n_clusters=n_clusters), reduced, path)
# num_runs = 100
# for _ in range(num_runs):
# clustering = KMeans(init='k-means++', n_clusters=n_clusters)
# cluster_labels = clustering.fit_predict(reduced)
# if davies_bouldin_score(reduced, cluster_labels) < 0.55:
#     break

# utils.print_eval_scores(data=reduced, cluster_labels=cluster_labels, n_clusters=n_clusters)
# utils.plot_similarity_mat(data=reduced, cluster_labels=cluster_labels)


clustering = KMeans(n_clusters=n_clusters, init='k-means++')
cluster_labels = clustering.fit_predict(reduced)
