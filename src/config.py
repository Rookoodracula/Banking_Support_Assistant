import os
import torch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Notebooks",
    "models",
    "saved_model"
)

TRAIN_PATH = os.path.join(
    BASE_DIR,
    "Data",
    "train.csv"
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")