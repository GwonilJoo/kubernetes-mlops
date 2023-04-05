import torch
import os
from dataclasses import dataclass

@dataclass
class config:
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    learning_rate = float(os.getenv("LEARNGIN_RATE", "0.001"))
    epochs = int(os.getenv("EPOCHS", "1"))
    batch_size = int(os.getenv("BATCH_SIZE", "100"))
    #dataset_dir = os.getenv("MNIST_DIR", '../saved/MNIST_data/')
    dataset_dir = os.getenv("DATASET_DIR", '../saved/MNIST_data/')
    experiment_id = os.getenv("EXPERIMENT_ID", "none")
    save_dir = os.getenv("SAVE_DIR", "../saved/")
    mongo = {
        "HOST": os.getenv("DB_HOST", "mongo"),
        "PORT": int(os.getenv("DB_PORT", "27017")),
        "USERNAME": os.getenv("DB_USERNAME", "admin"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password"),
        "DB_NAME": os.getenv("DB_NAME", "ml"),
        "COLLECTION": os.getenv("COLLECTION", "train"),
    }