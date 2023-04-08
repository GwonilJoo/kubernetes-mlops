import torch
import torch.nn as nn

class Resnet18(nn.Module):
    def __init__(self, num_classes):
        super(Resnet18, self).__init__()
        self.model = torch.hub.load(
            'pytorch/vision:v0.10.0', 
            'resnet18', 
            pretrained=True
        )
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, num_classes)

    def forward(self, x):
        out = self.model(x)
        return out