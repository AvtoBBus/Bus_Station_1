import torch
import torch.nn as nn
from PIL import Image


class My_Dataset(torch.utils.data.Dataset):
    def __init__(self, file_list: list, transform=None):
        self.file_list = file_list
        self.transform = transform
        self.file_list_len = len(self.file_list)

    def __len__(self) -> int:
        return self.file_list_len

    def __getitem__(self, index: int):
        way_to_file = "data/train/" + str(self.file_list[index])
        img = Image.open(way_to_file)
        img_transformed = self.transform

        name_class = way_to_file.split('/')[-1].split('.')[0]
        name_class = name_class[:-5]
        label = 1
        if name_class == 'zebra':
            label = 0

        return img_transformed, label


class My_Cnn(nn.Module):
    def __init__(self):
        super(My_Cnn, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc1 = nn.Linear(3*3*64, 10)
        self.fc2 = nn.Linear(10, 2)
        self.dropout = nn.Dropout(0.5)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.view(out.size(0), -1)
        out = self.relu(self.fc1(out))
        out = self.fc2(out)
        return out
