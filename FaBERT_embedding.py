import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
import pickle

# Step 1: Choose a pre-trained transformer model
tokenizer = AutoTokenizer.from_pretrained("sbunlp/fabert")
model = AutoModel.from_pretrained("sbunlp/fabert")


# Step 2: Tokenization
def tokenize_textp(text):
    tokens = tokenizer(text[0], text[1], return_tensors="pt", padding=True, truncation=True, max_length=512
                       , add_special_tokens=True)
    return tokens

def tokenize_text(text):
    tokenized_batch = tokenizer((text[0], text[1]), truncation=True,
                                padding='max_length', max_length=256)
    tokenized_batch['input_ids'] = tokenized_batch['input_ids'][0] + tokenized_batch['input_ids'][1]
    tokenized_batch['attention_mask'] = tokenized_batch['attention_mask'][0] + tokenized_batch['attention_mask'][1]
    tokenized_batch['token_type_ids'] = tokenized_batch['token_type_ids'][0] + tokenized_batch['token_type_ids'][1]

    tokenized_batch['input_ids'] = torch.tensor([tokenized_batch['input_ids']])
    tokenized_batch['attention_mask'] = torch.tensor([tokenized_batch['attention_mask']])
    tokenized_batch['token_type_ids'] = torch.tensor([tokenized_batch['token_type_ids']])
    return tokenized_batch

# Step 3: Get embedding
def get_word_embeddings(tokens):
    with torch.no_grad():
        outputs = model(**tokens)
    embeddings = outputs.last_hidden_state  # Get the embeddings for all tokens
    return embeddings


# Step 4: Aggregation
def aggregate_embeddings(embeddings):
    # Calculate the average of embeddings across all tokens (words)
    avg_embedding = torch.mean(embeddings, dim=1)  # Average along the sequence dimension
    return avg_embedding


# Load your DataFrame with text data
df = pd.read_csv(r'modares_papers\articles_modares.csv', encoding='utf-8')

# Iterate through each row of the DataFrame
embeddings_list = []
for index, row in df.iterrows():
    # text = [row['title'], row['abstract']]
    text = [row['title'], row['keywords']]
    # Step 2: Tokenization
    # tokens = tokenize_text(text)
    tokens_p = tokenize_textp(text)
    # Step 3: Word embedding lookup
    embeddings = get_word_embeddings(tokens_p)
    # Step 4: Aggregation
    avg_embedding = aggregate_embeddings(embeddings)
    embeddings_list.append(avg_embedding)

# Concatenate the embeddings to form a tensor
embeddings_tensor = torch.cat(embeddings_list, dim=0)

with open(r'util\title_keywords_embedding.pkl', "wb") as f:
    pickle.dump(embeddings_tensor, f)

print(embeddings_tensor.shape)  # Output shape: (num_texts, embedding_size)


