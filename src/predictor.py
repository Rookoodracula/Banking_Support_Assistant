import torch
import numpy as np
import pandas as pd
import streamlit as st

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)
from sklearn.preprocessing import LabelEncoder
from src.config import MODEL_PATH, TRAIN_PATH, DEVICE

# -----------------------------
# Caching Model & Artifacts
# -----------------------------

@st.cache_resource
def load_assets():
    train_df = pd.read_csv(TRAIN_PATH)
    encoder = LabelEncoder()
    encoder.fit(train_df["category"])

    tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)

    model = DistilBertForSequenceClassification.from_pretrained(
        MODEL_PATH,
        num_labels=len(encoder.classes_)
    )
    model.to(DEVICE)
    model.eval()

    return tokenizer, model, encoder

# -----------------------------
# Prediction Function
# -----------------------------

def predict(query):
    # Retrieve cached assets
    tokenizer, model, encoder = load_assets()

    inputs = tokenizer(
        query,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = torch.softmax(outputs.logits, dim=1)

    probs = probabilities.cpu().numpy()[0]
    top3_idx = np.argsort(probs)[-3:][::-1]

    top3 = []
    for idx in top3_idx:
        top3.append({
            "intent": encoder.inverse_transform([idx])[0],
            "confidence": round(float(probs[idx]) * 100, 2)
        })

    return top3[0], top3