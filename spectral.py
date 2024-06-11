import pickle as pk
from matplotlib import pyplot as plt
from sklearn.cluster import SpectralClustering
import utils
import pandas as pd

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score

num_runs = 1
n_clusters = 5
embedding_tensor = pk.load(open(r'util\gensim_title_abs.pkl', 'rb'))
embeddings = embedding_tensor
reduced = utils.UMAP_reduce(data=embeddings, rdims=20)
# ig, axes = plt.subplots(1, 3, figsize=(18, 6))


# k_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# utils.plot_score_silhouette(k_values, "Spectral Clustering", reduced, SpectralClustering(affinity='rbf'), ax=axes[0])
# utils.plot_score_calinski_harabasz(k_values, "Spectral Clustering", reduced, SpectralClustering(affinity='rbf'), ax=axes[1])
# utils.plot_davies_bouldin_index(k_values, "Spectral Clustering", reduced, SpectralClustering(affinity='rbf'), ax=axes[2])

# plt.tight_layout()
# plt.show()
#
# num_runs = 1
# k_results = {key: None for key in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}

# for c_i in k_results:
#     for _ in range(num_runs):
#         clustering = SpectralClustering(n_clusters=c_i, affinity='rbf')
#         cluster_labels = clustering.fit_predict(reduced)
#         clustering: SpectralClustering
#         cluster_dict = {}
#         for i, label in enumerate(cluster_labels):
#             Add data point to the corresponding cluster in the dictionary
            # if label not in cluster_dict:
            #     cluster_dict[label] = []
            # cluster_dict[label].append(i)
        # utils.print_eval_scores(reduced, cluster_labels, c_i)

def print_clustered_papers(n_clusters: int, clustering, data: np.array, path: str):
    if not isinstance(clustering, np.ndarray):
        cluster_labels = clustering.fit_predict(data)
    else:
        cluster_labels = clustering

    cluster_dict = {}
    for i, label in enumerate(cluster_labels):
        if label not in cluster_dict:
            cluster_dict[label] = []
        cluster_dict[label].append(i)

    df = pd.read_csv(path, encoding='utf-8')
    titles = df['title']
    keywords = df['keywords']

    clustered_texts = [[] for _ in range(n_clusters)]
    for c_i in range(n_clusters):
        for i in cluster_dict.get(c_i, []):
            text = titles[i] + '\n' + keywords[i]
            clustered_texts[c_i].append(text)

    max_length = max(len(texts) for texts in clustered_texts)
    for texts in clustered_texts:
        texts.extend([''] * (max_length - len(texts)))
    # Create DataFrame
    df_clustered = pd.DataFrame({f'Cluster {c_i}': clustered_texts[c_i] for c_i in range(n_clusters)})

    # Write DataFrame to CSV
    df_clustered.to_csv('results\spectral5_abs_title.csv', index=False)


for _ in range(num_runs):
    clustering = SpectralClustering(n_clusters=n_clusters, affinity='rbf')
    cluster_labels = clustering.fit_predict(reduced)
    utils.print_eval_scores(reduced, cluster_labels, n_clusters)
utils.plot_similarity_mat(reduced, cluster_labels)
print_clustered_papers(n_clusters,cluster_labels,reduced,r'modares_papers\articles_modares.csv')


# range_n_clusters = [5, 6]
#
# for n_clusters in range_n_clusters:
#     Create a subplot with 1 row and 2 columns
    # fig, (ax1) = plt.subplots(1, 1)
    # fig.set_size_inches(18, 7)
    #
    # The 1st subplot is the silhouette plot
    # The silhouette coefficient can range from -1, 1 but in this example all
    # lie within [-0.1, 1]
    # ax1.set_xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    # ax1.set_ylim([0, len(reduced) + (n_clusters + 1) * 10])
    #
    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    # clusterer = clustering = SpectralClustering(n_clusters=n_clusters, affinity='rbf')
    # cluster_labels = clusterer.fit_predict(reduced)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    # silhouette_avg = silhouette_score(reduced, cluster_labels)
    # print(
    #     "For n_clusters =",
    #     n_clusters,
    #     "The average silhouette_score is :",
    #     silhouette_avg,
    # )
    #
    # Compute the silhouette scores for each sample
    # sample_silhouette_values = silhouette_samples(reduced, cluster_labels)
    #
    # y_lower = 10
    # for i in range(n_clusters):
    #     Aggregate the silhouette scores for samples belonging to
    #     cluster i, and sort them
        # ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        #
        # ith_cluster_silhouette_values.sort()
        #
        # size_cluster_i = ith_cluster_silhouette_values.shape[0]
        # y_upper = y_lower + size_cluster_i
        #
        # color = cm.nipy_spectral(float(i) / n_clusters)
        # ax1.fill_betweenx(
        #     np.arange(y_lower, y_upper),
        #     0,
        #     ith_cluster_silhouette_values,
        #     facecolor=color,
        #     edgecolor=color,
        #     alpha=0.7,
        # )
        #
        # Label the silhouette plots with their cluster numbers at the middle
        # ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        #
        # Compute the new y_lower for next plot
        # y_lower = y_upper + 10  # 10 for the 0 samples
    #
    # ax1.set_title("The silhouette plot for the various clusters.")
    # ax1.set_xlabel("The silhouette coefficient values")
    # ax1.set_ylabel("Cluster label")
    #
    # The vertical line for average silhouette score of all the values
    # ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    #
    # ax1.set_yticks([])  # Clear the yaxis labels / ticks
    # ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    #
    # 2nd Plot showing the actual clusters formed
    # colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
#
# plt.show()
#
#
