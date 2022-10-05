import os
import csv
import shutil
from class_iterator import Iterator

'''возвращает абослютный путь'''
def create_absolute_way(name_class, number):
    return os.path.abspath(create_new_way(name_class, number))
 
'''возвращает путь для копии'''
def create_new_way(name_class, number):
    return f"dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"

'''создаёт аннотацию'''
def create_annotation(name_class, number):
    with open ("dataset_another.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow( [create_absolute_way(name_class, number), create_new_way(name_class, number), name_class] )

'''создаёт копии'''
def create_copy(name_class):
    iter = Iterator()
    while iter.num != 1050:
        way = f"dataset/download_data/{name_class}/{str(iter.num).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(name_class, iter.num))
        create_annotation(name_class, iter.num)
        next(iter)
    

def main():
    if not os.path.isdir("dataset/dataset_another"):
        os.mkdir("dataset/dataset_another")
    with open ("dataset_another.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    create_copy("zebra")
    create_copy("bay_horse")

if __name__ == "__main__":
    main()