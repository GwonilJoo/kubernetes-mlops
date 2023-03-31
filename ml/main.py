import os
import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init
from typing import Dict

from data_loader import get_data_loader
from model import CNN
from train import train
from test import test
from repo import MongoRepo


class config:
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    learning_rate = float(os.getenv("LEARNGIN_RATE", "0.001"))
    epochs = int(os.getenv("EPOCHS", "1"))
    batch_size = int(os.getenv("BATCH_SIZE", "100"))
    dataset_dir = os.getenv("MNIST_DIR", '../saved/MNIST_data/')
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

mnist_train = dsets.MNIST(root=config.dataset_dir,
                        train=True,
                        transform=transforms.ToTensor(),
                        download=True)

mnist_test = dsets.MNIST(root=config.dataset_dir,
                        train=False,
                        transform=transforms.ToTensor(),
                        download=True)

repo = MongoRepo(config)

def train_model():
    data_loader = get_data_loader(mnist_train, config.batch_size)
    
    model = CNN().to(config.device)
    
    criterion = torch.nn.CrossEntropyLoss().to(config.device)    # Softmax is internally computed.
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)

    train_result: Dict[str, Dict[str, any]] = train(
        model, 
        data_loader, 
        criterion, 
        optimizer, 
        config,
    )

    for key, value in train_result.items():
        test_acc = test(model, value["path"], mnist_test, config.device)
        train_result[key]["test_acc"] = test_acc

    repo.create(
        {
            "experiment_id": config.experiment_id,
            **train_result,
        }
    )
    print(train_result)


if __name__ == "__main__":
   train_model()