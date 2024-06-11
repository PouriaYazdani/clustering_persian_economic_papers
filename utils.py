import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import umap
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score
from sklearn.cluster import *
import pandas as pd


def plot_similarity_mat(data: np.array, cluster_labels: np.array):
    """
    plots sorted similarity matrix of given 2D numpy array
    :param data:
    :param cluster_labels:
    :return:
    """
    sorted_indices = np.argsort(cluster_labels)
    sorted_data = data[sorted_indices]
    size = sorted_data.shape[0]
    similarity_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            similarity_matrix[i, j] = 1 / (1 + euclidean(sorted_data[i], sorted_data[j]))
    correlation_matrix = np.corrcoef(similarity_matrix)
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix, cmap='magma', xticklabels=False, yticklabels=False)
    plt.title('Sorted Similarity Matrix')
    plt.xticks(np.arange(0, size, 100), np.arange(0, size, 100))
    plt.yticks(np.arange(0, size, 100), np.arange(0, size, 100))
    plt.xlabel('Points')
    plt.ylabel('Points')
    plt.show()


def UMAP_reduce(data: np.array, rdims: int = 60) -> np.array:
    """
    performs umap reduction on given 2D numpy array and returns the reduced version
    :param data: 
    :param rdims: 
    :return: 
    """
    reducer = umap.UMAP(
        n_neighbors=25,
        min_dist=0.01,
        n_components=rdims)
    reduced = reducer.fit_transform(data)
    return reduced


def print_eval_scores(data: np.array, cluster_labels: np.array, n_clusters: int):
    """
    prints 3 evaluation scores
        silhouette_score, calinski_harabasz_score,davies_bouldin_score
    :param data:
    :param cluster_labels:
    :param n_clusters:
    :return:
    """
    silhouette_avg = silhouette_score(data, cluster_labels)
    calsinski_score = calinski_harabasz_score(data, cluster_labels)
    davies_score = davies_bouldin_score(data, cluster_labels)
    print(
        "For n_clusters =",
        n_clusters,
        "\nThe average silhouette_score is :",
        silhouette_avg,
        "\nand calinski harabasz score is :",
        calsinski_score,
        "\ndavies bouldin score is: ",
        davies_score
    )
    print("***************************************************")


def plot_score_silhouette(k: list[int], title: str, data: np.array, clustering, ax=None):
    """
    plots silouette score with respect to different number of clusters
    :param k:
    :param title:
    :param data:
    :param clustering:
    :param ax:
    :return:
    """
    silhouette_scores = []
    for i in k:
        clustering.n_clusters = i
        labels = clustering.fit_predict(data)  # Assuming you have your data stored in X
        silhouette_avg = silhouette_score(data, labels)
        silhouette_scores.append(silhouette_avg)

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(k, silhouette_scores, marker='o', color='black')
    ax.set_title(title)
    ax.set_xlabel('Number of clusters (k)')
    ax.set_ylabel('Silhouette Score')
    ax.grid(True)
    ax.axhline(min(silhouette_scores), color='red', linestyle='--', label=f'Min: {min(silhouette_scores):.2f}')
    ax.axhline(max(silhouette_scores), color='blue', linestyle='--', label=f'Max: {max(silhouette_scores):.2f}')

    # Label the minimum and maximum silhouette scores on the y-axis
    ax.text(k[0], min(silhouette_scores), f'{min(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.text(k[0], max(silhouette_scores), f'{max(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.legend()
    plt.show()


def plot_score_calinski_harabasz(k: list[int], title: str, data: np.array, clustering, ax=None):
    """
    plots calinski_harabasz score with respect to different number of clusters
    :param k:
    :param title:
    :param data:
    :param clustering:
    :param ax:
    :return:
    """
    silhouette_scores = []
    for i in k:
        clustering.n_clusters = i
        labels = clustering.fit_predict(data)  # Assuming you have your data stored in X
        silhouette_avg = calinski_harabasz_score(data, labels)
        silhouette_scores.append(silhouette_avg)

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(k, silhouette_scores, marker='o', color='black')
    ax.set_title(title)
    ax.set_xlabel('Number of clusters (k)')
    ax.set_ylabel('Calinski Harabaz index')
    ax.grid(True)
    ax.axhline(min(silhouette_scores), color='red', linestyle='--', label=f'Min: {min(silhouette_scores):.2f}')
    ax.axhline(max(silhouette_scores), color='blue', linestyle='--', label=f'Max: {max(silhouette_scores):.2f}')

    # Label the minimum and maximum silhouette scores on the y-axis
    ax.text(k[0], min(silhouette_scores), f'{min(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.text(k[0], max(silhouette_scores), f'{max(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.legend()
    plt.show()


def plot_davies_bouldin_index(k: list[int], title: str, data: np.array, clustering, ax=None):
    """
    plots davies_bouldin score with respect to different number of clusters
    :param k:
    :param title:
    :param data:
    :param clustering:
    :param ax:
    :return:
    """
    silhouette_scores = []
    for i in k:
        clustering.n_clusters = i
        labels = clustering.fit_predict(data)  # Assuming you have your data stored in X
        silhouette_avg = davies_bouldin_score(data, labels)
        silhouette_scores.append(silhouette_avg)

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(k, silhouette_scores, marker='o', color='black')
    ax.set_title(title)
    ax.set_xlabel('Number of clusters (k)')
    ax.set_ylabel('Davies Bouldin index')
    ax.grid(True)
    ax.axhline(min(silhouette_scores), color='red', linestyle='--', label=f'Min: {min(silhouette_scores):.2f}')
    ax.axhline(max(silhouette_scores), color='blue', linestyle='--', label=f'Max: {max(silhouette_scores):.2f}')

    # Label the minimum and maximum silhouette scores on the y-axis
    ax.text(k[0], min(silhouette_scores), f'{min(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.text(k[0], max(silhouette_scores), f'{max(silhouette_scores):.2f}', va='center', ha='right',
            backgroundcolor='w')
    ax.legend()
    plt.show()


def print_clustered_papers(n_clusters: int, clustering, data: np.array, path: str):
    """
    prints papers in clustered matter
    :param n_clusters:
    :param clustering:
    :param data:
    :param path:
    :return:
    """
    # kmeans = KMeans(init='k-means++', n_clusters=n_clusters)
    if not isinstance(clustering, np.ndarray):
        cluster_labels = clustering.fit_predict(data)
    else:
        cluster_labels = clustering
    # kmeans: KMeans
    cluster_dict = {}
    for i, label in enumerate(cluster_labels):
        # Add data point to the corresponding cluster in the dictionary
        if label not in cluster_dict:
            cluster_dict[label] = []
        cluster_dict[label].append(i)
    df = pd.read_csv(path, encoding='utf-8')
    titles = df['title']
    keywords = df['keywords']
    for c_i in range(n_clusters):
        print('CLUSTER ' + str(c_i))
        for i in cluster_dict.get(c_i):
            print(titles[i])
            print('\n', keywords[i])
            print('--------------------------')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print_eval_scores(data, cluster_labels, n_clusters)


def write_clustered_papers(n_clusters: int, clustering, data: np.array, path: str):
    """
    performs clustering and writes the result as a pandas dataframe
    :param n_clusters:
    :param clustering:
    :param data:
    :param path:
    :return:
    """
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
    df_clustered.to_csv(path, index=False)
