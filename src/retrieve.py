#Importing necessary libraries

import os
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Paths

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_PATH = os.path.join(
    BASE_DIR,
    "Data",
    "train.csv"
)


# Load Training Data

train_df = pd.read_csv(TRAIN_PATH)


# Load Embedding Model

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Create Embeddings

train_embeddings = embedding_model.encode(
    train_df["text"].tolist(),
    convert_to_numpy=True,
    show_progress_bar=False
)

# Retrieval Function

def retrieve_similar(query):

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        query_embedding,
        train_embeddings
    )[0]

    best_index = np.argmax(similarities)

    return {
        "matched_question": train_df.iloc[best_index]["text"],
        "category": train_df.iloc[best_index]["category"],
        "similarity": round(float(similarities[best_index]) * 100, 2)
    }