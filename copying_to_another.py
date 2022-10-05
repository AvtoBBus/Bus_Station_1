import os
import csv
import shutil

'''возвращает абослютный путь'''
def create_absolute_way(name_class, number):
    return f"C:/Users/miste/PycharmProjects/pythonProject2/dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"
 
'''возвращает относительный путь'''
def create_relative_way(name_class, number):
    return f"dataset/{name_class}_{str(number).zfill(4)}.jpg"

'''создаёт аннотацию'''
def create_annotation(name_class, number):
    with open ("dataset_another.csv", "a", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow( [create_absolute_way(name_class, number), create_relative_way(name_class, number), name_class] )

'''воззвращает путь для копии'''
def create_new_way(name_class, number):
    return f"dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"

'''создаёт копии'''
def create_copy(name_class):
    for number in range(0, 1050):
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(name_class, number))
        create_annotation(name_class, number)

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