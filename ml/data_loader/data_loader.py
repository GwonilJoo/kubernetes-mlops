import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init


def get_data_loader(mnist_train, batch_size):
    data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                          batch_size=batch_size,
                                          shuffle=True,
                                          drop_last=True)
    return data_loader