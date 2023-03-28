import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init

from data_loader import get_data_loader
from model import CNN
from train import train
from test import test


class config:
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    learning_rate = 0.001
    training_epochs = 15
    batch_size = 100
    dataset_dir = '../saved/MNIST_data/'

print(f"dataset_dir: {config.dataset_dir}")

mnist_train = dsets.MNIST(root=config.dataset_dir,
                        train=True,
                        transform=transforms.ToTensor(),
                        download=True)

mnist_test = dsets.MNIST(root=config.dataset_dir,
                        train=False,
                        transform=transforms.ToTensor(),
                        download=True)


def train_model():
    data_loader = get_data_loader(mnist_train, config.batch_size)
    
    model = CNN().to(config.device)
    
    criterion = torch.nn.CrossEntropyLoss().to(config.device)    # Softmax is internally computed.
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)

    train(model, data_loader, criterion, optimizer, config.training_epochs, config.device)
    test(model, mnist_test, config.device)



if __name__ == "__main__":
   train_model()