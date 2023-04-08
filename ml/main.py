import os
import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init
from typing import Dict
from bson import ObjectId
from uuid import UUID

from data_loader import get_data_loader
from model import CNN
from train import train
from test import test
from repo import MongoRepo
from config import config


repo = MongoRepo(config)

def train_model():
    experiment_id = ObjectId()

    train_data_loader = get_data_loader(
        dataset_dir=os.path.join(config.dataset_dir, "train"),
        batch_size=config.batch_size
    )
    test_data_loader = get_data_loader(
        dataset_dir=os.path.join(config.dataset_dir, "test"),
        batch_size=config.batch_size
    )

    model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
    
    criterion = torch.nn.CrossEntropyLoss().to(config.device)    # Softmax is internally computed.
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)

    train_result: Dict[str, Dict[str, any]] = train(
        model, 
        train_data_loader, 
        criterion, 
        optimizer, 
        config,
        experiment_id
    )

    for key, value in train_result.items():
        test_acc = test(model, value["path"], test_data_loader, config.device)
        train_result[key]["test_acc"] = test_acc

    experiment = {
        "_id": experiment_id,
        "model": "resnet18",
        "epochs": config.epochs,
        "learning_rate": config.learning_rate,
        "batch_size": config.batch_size,
        "result": train_result,
        "project_id": UUID(config.project_id)
    }
    try:
        repo.create(experiment)
        print("Success to create documents", flush=True)
    except Exception as e:
        print(f"Fail to create documents: {e}", flush=True)

    print(train_result, flush=True)


if __name__ == "__main__":
   train_model()