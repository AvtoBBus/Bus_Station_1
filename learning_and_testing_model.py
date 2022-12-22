import torch
import torch.nn as nn
import torch
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import zipfile
import shutil
import transform_info as ti
import help_defenition as hd


class My_Dataset(torch.utils.data.Dataset):
    def __init__(self, file_list, transform=None):
        self.file_list = file_list
        self.transform = transform
        self.file_list_len = len(self.file_list)

    def __len__(self) -> int:
        return self.file_list_len

    def __getitem__(self, index: int):
        pass


def start():
    lr = 0.001
    batch_size = 100
    epochs = 10
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    torch.manual_seed(1234)

    if device == 'cuda':
        torch.cuda.manual_seed_all(1234)
    if os.path.isdir('data'):
        shutil.rmtree('data')
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/train', exist_ok=True)
    os.makedirs('data/test', exist_ok=True)
    os.makedirs('data/validation', exist_ok=True)

    base_dir = 'dataset'
    with zipfile.ZipFile(os.path.join(base_dir, 'dataset_another.zip')) as train_zip:
        train_zip.extractall('data')

    list_of_something = os.listdir('data/dataset_another')
    for el in list_of_something:
        way = 'data/dataset_another/' + str(el)
        shutil.move(way, 'data/train')
    shutil.rmtree('data/dataset_another')

    list_train = os.listdir('data/train')
    list_test = list_train[:100] + list_train[-100:]
    hd.del_n_elem(list_train, 100)
    list_validation = list_train[:100] + list_train[-100:]
    hd.del_n_elem(list_train, 150)

    for elem in list_test:
        shutil.move("data/train/" + str(elem), "data/test")
    for elem in list_validation:
        shutil.move("data/train/" + str(elem), "data/validation")

    list_rand_index = []
    hd.generate_mas(list_rand_index, 1, len(list_train) / 2, 5)
    hd.generate_mas(list_rand_index, len(
        list_train) / 2 + 1, len(list_train), 5)
    figure = plt.figure()
    num_of_img = 1
    for index in list_rand_index:
        figure.add_subplot(2, 5, num_of_img)
        way_to_file = "data/train/" + str(list_train[index])
        image = Image.open(way_to_file)
        plt.imshow(image)
        num_of_img += 1
    plt.show()

    myds_train = My_Dataset(list_train, ti.train_transforms)
    myds_test = My_Dataset(list_test, ti.test_transforms)
    myds_valid = My_Dataset(list_validation, ti.validation_transforms)


if __name__ == "__main__":
    start()
