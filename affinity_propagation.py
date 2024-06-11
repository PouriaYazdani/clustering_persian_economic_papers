import pickle as pk
from sklearn.cluster import AffinityPropagation
import numpy as np
import utils


embedding_tensor = pk.load(open(r'util\gensim_title.pkl', 'rb'))
embeddings = embedding_tensor
reduced = utils.UMAP_reduce(data=embeddings, rdims=80)


prefrences = [-30, -20, -15, -10]
for pref in prefrences:
    clustering = AffinityPropagation(preference=pref).fit(reduced)
    cluster_labels = clustering.labels_
    n_clusters = len(np.unique(cluster_labels))
    utils.print_eval_scores(reduced, cluster_labels, n_clusters)
    print(
        "preference was ",pref,
        '\n####################################'
    )
utils.plot_similarity_mat(reduced, cluster_labels)
