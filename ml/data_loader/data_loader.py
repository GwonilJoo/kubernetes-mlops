# import torch
# import torchvision.datasets as dsets
# import torchvision.transforms as transforms
# import torch.nn.init


# def get_data_loader(mnist_train, batch_size):
#     data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
#                                           batch_size=batch_size,
#                                           shuffle=True,
#                                           drop_last=True)
#     return data_loader


from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms

def get_data_loader(dataset_dir, batch_size) -> DataLoader:
    imgs = ImageFolder(
        root=dataset_dir,
        transform=transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )
    )
    data_loader = DataLoader(imgs, batch_size=batch_size, shuffle=True)

    return data_loader