import pandas as pd
from gensim.models import Word2Vec
import pickle
import numpy as np

data = pd.read_csv(r'cleaned\cleaned_title.csv', encoding='utf-8')
data2 = pd.read_csv(r'cleaned\cleaned_abstract.csv', encoding='utf-8')

separator_token = ["SEP"]
tokenized_titles = [eval(row) if isinstance(row, str) else row for row in data['title']]
tokenized_abstracts = [eval(row) if isinstance(row, str) else row for row in data2['abstract']]
combined = [tokenized_titles[i] + separator_token + tokenized_abstracts[i] for i in range(len(tokenized_abstracts))]

# Train Word2Vec model
word2vec_model = Word2Vec(sentences=combined, vector_size=150, window=5, min_count=1, workers=4)
# word2vec_model.save(r'util\gensim_train_title.model')

embeddings_list = []
for tokenized_text in combined:
    # Extract word embeddings for words present in the vocabulary
    document_embedding = np.array([word2vec_model.wv[word] for word in tokenized_text if word in word2vec_model.wv])
    # Calculate the mean along the first axis (axis=0)
    avg_embedding = np.mean(document_embedding, axis=0)
    embeddings_list.append(avg_embedding)
# Convert embeddings_list to a NumPy array
embeddings_array = np.array(embeddings_list)

# Save embeddings tensor to file
with open(r'util\gensim_title_abs.pkl', "wb") as f:
    pickle.dump(embeddings_array, f)

print(embeddings_array.shape)
