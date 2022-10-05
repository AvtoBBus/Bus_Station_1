import os
import shutil
import csv
import random
from class_iterator import Iterator

'''воззвращает путь для копии'''
def create_new_way(number):
    return f"dataset/dataset_number/{number}.jpg"

'''возвращает абослютный путь'''
def create_absolute_way(number):
    return os.path.abspath(create_new_way(number))

'''создаёт аннотацию'''
def create_annotation(name_class, number):
    with open ("dataset_number.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow( [create_absolute_way(number), create_new_way(number), name_class] )

'''создаёт копии'''
def create(name_class):
    iter = Iterator()
    while iter.num != 1050:
        way = f"dataset/download_data/{name_class}/{str(iter.num).zfill(4)}.jpg"
        if os.path.isfile(way) == True:
            new_number = random.randint(0, 10001)
            while os.path.isfile(create_new_way(new_number)) == True:
                new_number = random.randint(0, 10001)
            shutil.copyfile(way, create_new_way(new_number))
            create_annotation(name_class, iter.num)
        next(iter)

def main():
    if not os.path.isdir("dataset/dataset_number"):
        os.mkdir("dataset/dataset_number")
    
    with open ("dataset_number.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    
    create("zebra")
    create("bay_horse")

if __name__ == "__main__":
    main()