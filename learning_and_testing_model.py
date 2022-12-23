import torch
import torch.nn as nn
import torch
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import zipfile
import shutil
import transform_info as ti
import help_defenition as hd
import My_Classes as mc


def start_hacking():
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
    hd.del_n_elem(list_train, 150)
    list_validation = []

    for elem in list_test:
        shutil.move("data/train/" + str(elem), "data/test")

    list_train, list_validation = train_test_split(
        list_train, test_size=1/9)

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

    myds_train = mc.My_Dataset(list_train, ti.train_transforms)
    myds_test = mc.My_Dataset(list_test, ti.test_transforms)
    myds_valid = mc.My_Dataset(list_validation, ti.validation_transforms)

    loader_train = torch.utils.data.DataLoader(
        dataset=myds_train, batch_size=batch_size, shuffle=True)
    loader_test = torch.utils.data.DataLoader(
        dataset=myds_test, batch_size=batch_size, shuffle=True)
    loader_valid = torch.utils.data.DataLoader(
        dataset=myds_valid, batch_size=batch_size, shuffle=True)

    # print(myds_train[0][0])
    # print(loader_train.dataset[0][0])
    # print(len(myds_train), len(loader_train))

    model = mc.My_Cnn().to(device)
    model.train()

    optimizer = optim.Adam(params=model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0

        for data, label in loader_train:
            data = data.to(device)
            label = label.to(device)

            output = model(data)
            loss = criterion(output, label)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            acc = ((output.argmax(dim=1) == label).float().mean())
            epoch_accuracy += acc/len(loader_train)
            epoch_loss += loss/len(loader_train)

        print(
            f'Epoch : {epoch+1}, train accuracy : {epoch_accuracy}, train loss : {epoch_loss}')

        with torch.no_grad():
            epoch_val_accuracy = 0
            epoch_val_loss = 0
            for data, label in loader_valid:
                data = data.to(device)
                label = label.to(device)

                val_output = model(data)
                val_loss = criterion(val_output, label)

                acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc / len(loader_valid)
                epoch_val_loss += val_loss / len(loader_valid)

            print(
                f'Epoch : {epoch+1}, val_accuracy : {epoch_val_accuracy}, val_loss : {epoch_val_loss}')

    # zebra_probs = []
    # model.eval()
    # with torch.no_grad():
    #     for data, fileid in loader_test:
    #         data = data.to(device)
    #         preds = model(data)
    #         preds_list = F.softmax(preds, dim=1)[:, 1].tolist()
    #         zebra_probs += list(zip(list(fileid), preds_list))


if __name__ == "__main__":
    start_hacking()
