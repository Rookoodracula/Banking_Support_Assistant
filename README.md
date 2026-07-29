[README.md](https://github.com/user-attachments/files/30415431/README.md)
# 🏦 Banking Intent Detection Chatbot using DistilBERT

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📌 Project Overview

The **Banking Intent Detection Chatbot** is an NLP-based intelligent customer support system that classifies banking-related customer queries into predefined intent categories using **DistilBERT**, a lightweight transformer model from Hugging Face.

The project demonstrates the complete NLP pipeline, including:

- Data preprocessing
- Text tokenization
- Transformer-based model training
- Model evaluation
- Inference pipeline
- Semantic retrieval
- Streamlit web application deployment

The chatbot predicts the user's banking intent and provides an appropriate response in real time.

---

# 🎯 Problem Statement

Customer support teams receive thousands of banking-related queries every day.

Instead of manually classifying these queries, this project automates the process using Natural Language Processing (NLP).

Example:

**User Query**

> My debit card hasn't arrived yet.

↓

Predicted Intent

> card_arrival

↓

Chatbot Response

> Your card is currently being processed and will be delivered soon.

---

# 🚀 Features

✅ Banking Intent Classification

✅ DistilBERT Fine-Tuning

✅ Top-3 Intent Prediction

✅ Confidence Score

✅ Semantic Similarity Search

✅ Banking Response Generation

✅ Interactive Chatbot

✅ Streamlit Web Application

---

# 🧠 Model Used

- DistilBERT Base Uncased
- Hugging Face Transformers
- PyTorch Backend

Why DistilBERT?

- Faster than BERT
- Smaller model size
- High accuracy
- Suitable for real-time inference

---

# 📂 Dataset

Dataset Used:

**Banking77 Dataset**

Contains:

- Banking customer queries
- 77 intent categories
- Short text classification dataset

Example:

| Query | Intent |
|--------|--------|
| My card is blocked | card_not_working |
| Cash withdrawal failed | cash_withdrawal |
| I forgot my PIN | cash_withdrawal_pin |

---

# 📁 Project Structure

```
CAPSTONE PROJECT/
│
├── Data/
│   ├── train.csv
│   └── test.csv
│
├── Notebooks/
│   ├── Data_Preprocessing.ipynb
│   ├── Model_Training.ipynb
│   ├── Model_Evaluation.ipynb
│   ├── Inference_Demo.ipynb
│   └── models/
│       └── saved_model/
│
├── outputs/
│
├── src/
│   ├── config.py
│   ├── predictor.py
│   ├── responses.py
│   └── retrieve.py
│
├── app.py
├── README.md
├── requirements.txt
```

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- PyTorch
- Hugging Face Transformers
- Sentence Transformers
- Streamlit

---

# 🔄 Project Workflow

```
Raw Dataset

        │

        ▼

Data Preprocessing

        │

        ▼

Label Encoding

        │

        ▼

Train-Test Split

        │

        ▼

Tokenization

        │

        ▼

DistilBERT Fine-Tuning

        │

        ▼

Model Evaluation

        │

        ▼

Save Model

        │

        ▼

Inference

        │

        ▼

Streamlit Deployment
```

---

# 📚 Notebook Description

## Notebook 1

### Data_Preprocessing.ipynb

Performed:

- Data Loading
- Exploratory Data Analysis
- Missing Value Check
- Duplicate Removal
- Label Encoding
- Train-Test Split
- Tokenization
- Saving Processed Dataset

---

## Notebook 2

### Model_Training.ipynb

Performed:

- Load Processed Dataset
- Load DistilBERT
- Create Trainer
- Fine-tune Model
- Training
- Validation
- Save Model
- Save Tokenizer

---

## Notebook 3

### Model_Evaluation.ipynb

Performed:

- Load Saved Model
- Predict Test Data
- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report
- Top-3 Prediction
- Save Evaluation Metrics

---

## Notebook 4

### Inference_Demo.ipynb

Performed:

- Load Saved Model
- Predict User Query
- Confidence Score
- Top-3 Predictions
- Banking Response
- Interactive Chatbot

---

# 🤖 Model Pipeline

```
User Query

      │

      ▼

Tokenizer

      │

      ▼

Input IDs

      │

      ▼

DistilBERT

      │

      ▼

Logits

      │

      ▼

Softmax

      │

      ▼

Predicted Intent

      │

      ▼

Banking Response
```

---

# 🖥️ Streamlit Application

The web application provides:

- User-friendly interface
- Banking chatbot
- Intent prediction
- Confidence score
- Top-3 predictions
- Similar question retrieval
- Banking response

Run:

```bash
streamlit run app.py
```

---

# 📊 Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report

---

# 📈 Outputs Generated

The project generates:

- Trained Model
- Tokenizer
- Classification Report
- Evaluation Metrics
- Prediction CSV
- Top-3 Predictions

---

# 💡 Future Improvements

- Voice Assistant Integration
- Multi-language Support
- Speech-to-Text
- Text-to-Speech
- RAG Integration
- LLM Integration
- Chat History Database
- Cloud Deployment
- REST API using FastAPI

---

# ▶️ Installation

Clone the repository

```bash
git clone <https://github.com/Rookoodracula/Banking_Support_Assistant.git>
```

Go inside the project

```bash
cd CAPSTONE_PROJECT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Screenshots

### Home Page
![Home Page](Screenshot%202026-07-27%20125616.png)

### Prediction Page
![Prediction Page](Screenshot%202026-07-27%20125645.png)

### Chatbot Output
![Chatbot Output](Screenshot%202026-07-27%20125705.png)

**PLS CHECK THE SCREENSHOT FOLDER UPLOADED TO GET A GLANCE OF THE PROJECT**

## 🤖 Trained Model Weights

Due to GitHub file size limitations, the trained DistilBERT / transformer model weights for this project are hosted on the **Hugging Face Model Hub**:

[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model%20Hub-yellow)](https://huggingface.co/Abhiroopbasu/Banking_77_chatbot)

🔗 **MODEL LINK:** [https://huggingface.co/Abhiroopbasu/Banking_77_chatbot](https://huggingface.co/Abhiroopbasu/Banking_77_chatbot)


# 👨‍💻 Skills Demonstrated

- Natural Language Processing
- Text Classification
- Transformer Models
- Transfer Learning
- DistilBERT
- Hugging Face
- PyTorch
- Streamlit
- Model Deployment
- Machine Learning Pipeline

---

# 🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

- NLP preprocessing
- Tokenization
- Transformer fine-tuning
- Model evaluation
- Text classification
- Semantic search
- Streamlit deployment
- End-to-end AI project development

---

# 🙏 Acknowledgements

- Hugging Face Transformers
- PyTorch
- Streamlit
- Banking77 Dataset
- Scikit-Learn

---

# 📄 License

This project is developed for educational and learning purposes.

---

# 👤 Author

**Abhirup Basu**

B.Tech (Computer Science & Engineering)

AI/ML Enthusiast

Capstone Project"# Banking_Support_Assistant" 
