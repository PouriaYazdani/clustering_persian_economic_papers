# clustering_persian_economic_papers
In this project I used the follwing pipleline to perform clustering on Persian
economic papers.
+ crawled 592 papers from [Tarbiat Modares University](https://ecor.modares.ac.ir/)
+ extracted title, abstract and keyword for each paper.
+ performed cleaning preprocess including normalizing, lemmatizing, removing stopwords and redundant words using [hazm](https://www.roshan-ai.ir/hazm/docs/).
+ perform 2 types of word embeddings using [FaBERT](https://huggingface.co/sbunlp/fabert) and [gensim's Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html).
+ Performed various type of clusteting algorithms using [sklearn.cluster](https://scikit-learn.org/stable/modules/clustering.html) package.
+ Evaluated results using unknown ground truth evaluation metrics and by visualizing sorted similarity matrix. ([read here for more](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient)).
+ inspected identified clusters by eye and allocated appropriate names to each cluster.


Here you can view the presentation [slides](https://docs.google.com/presentation/d/1wpJCaZzaz0dXNvtjFJ1hogMPx_YURsrs/edit?usp=drive_link&ouid=117859559202921264968&rtpof=true&sd=true).

<p>
  <img src="https://github.com/user-attachments/assets/07fbb93d-8d0e-4ef9-9818-589526a1d730" alt="Figure_1" width="400" height="300">
  <img src="https://github.com/user-attachments/assets/e3a445e7-4571-4765-9251-4d2304f65f91" alt="Figure_2" width="600" height="200" style="position: relative; top: -30px;">
</p>


