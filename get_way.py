import os


def create_download_relative_way(name_class, number):
    return f"dataset/download_data/{name_class}/{str(number).zfill(4)}.jpg"


def create_another_relative_way(name_class, number):
    return f"dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"


def create_number_relative_way(number):
    return f"dataset/dataset_number/{str(number).zfill(4)}.jpg"
