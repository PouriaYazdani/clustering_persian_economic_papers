import pickle as pk
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram
import utils
import matplotlib.pyplot as plt



embedding_tensor = pk.load(open(r'util\gensim_title.pkl', 'rb'))
embeddings = embedding_tensor
reduced = utils.UMAP_reduce(data=embeddings)
# reduced = embeddings
# ig, axes = plt.subplots(1, 3, figsize=(18, 6))
#
#
# k_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# utils.plot_score_calinski_harabasz(k_values, "Ward Linkage", reduced, AgglomerativeClustering(linkage='ward'), ax=axes[0])
# utils.plot_score_calinski_harabasz(k_values, "Complete Linkage", reduced, AgglomerativeClustering(linkage='complete'), ax=axes[1])
# utils.plot_score_calinski_harabasz(k_values, "Average Linkage", reduced, AgglomerativeClustering(linkage='average'), ax=axes[2])

# plt.tight_layout()
# plt.show()




average_clustering = linkage(reduced, method="average", metric="euclidean")
ward_clustering = linkage(reduced, method="ward", metric="euclidean")
complete_clustering = linkage(reduced, method="complete", metric="euclidean")

# plt.figure()
last_cls = 100 # The number of last clusters to show in the dendogram
#
plt.title(f'Hierarchical Clustering Dendrogram (truncated at {last_cls} clusters) - complete method')
plt.xlabel('Sample Index (includes count of records in cluster)')
plt.ylabel('Euclidian Distance')
fig = plt.gcf()
fig.set_size_inches(20,7)
fig.set_dpi(150)

dendrogram(
    complete_clustering,
    truncate_mode='lastp', # truncate dendrogram to the last p merged clusters
    p=last_cls,            # and set a value for last p merged clusters
    show_leaf_counts=True, # if parentheses then this is a count of observations, otherwise an id
    leaf_rotation=90.,
    leaf_font_size=8.,
    show_contracted=False, # to get a distribution impression in truncated branches
)
# plt.savefig(os.path.join('data',f'Dendogram-{c.dmeasure}-{last_cls}.png'))
plt.show()
####################################################################################################################
# num_runs = 1
# k_results = {key: None for key in [4,5,6,7,8,9,10,11,12,13,14]}
# for c_i in k_results:
#     scores = (0,0,0)
#     for _ in range(num_runs):
#         clustering = AgglomerativeClustering(n_clusters=c_i, linkage='ward')
#         cluster_labels = clustering.fit_predict(reduced)
#         clustering: AgglomerativeClustering
#         cluster_dict = {}
#         for i, label in enumerate(cluster_labels):
#             Add data point to the corresponding cluster in the dictionary
            # if label not in cluster_dict:
            #     cluster_dict[label] = []
            # cluster_dict[label].append(i)
        # utils.print_eval_scores(reduced, cluster_labels, c_i)
    # k_results[c_i] = scores
# print(reduced.shape[1])

#####################################################################################################################


# n_clusters = 5
# clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='average')
# cluster_labels = clustering.fit_predict(reduced)
# utils.plot_similarity_mat(reduced, cluster_labels)
# # # path = r'modares_papers\articles_modares.csv'
# # # utils.print_clustered_papers(n_clusters, clustering, reduced, path)
# # # utils.print_eval_scores(reduced, cluster_labels, n_clusters)
# clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='complete')
# cluster_labels = clustering.fit_predict(reduced)
# utils.plot_similarity_mat(reduced, cluster_labels)
#
# clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
# cluster_labels = clustering.fit_predict(reduced)
# utils.plot_similarity_mat(reduced, cluster_labels)
# plt.show()


