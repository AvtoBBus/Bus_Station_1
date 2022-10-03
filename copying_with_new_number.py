import os
import shutil
import csv

def create_absolute_way(name_class, number):
    return f"E:/BRUH/учёба/проектики/пп лаба 2/Bus_Station_1/dataset/dataset_number/{name_class}/{str(number).zfill(4)}.jpg"
 
def create_relative_way(name_class, number):
    return f"dataset/{name_class}/{str(number).zfill(4)}.jpg"

def create_annotation(name_class, number):
    with open ("dataset_number.csv", "a") as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow( [create_absolute_way(name_class, number), create_relative_way(name_class, number), name_class] )

def create_new_way(number):
    return f"dataset/dataset_number/{number}.jpg"

def create(name_class):
    for number in range(0, 1050):
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(number))
        create_annotation(name_class, number)

def main():
    if not os.path.isdir("dataset/dataset_number"):
        os.mkdir("dataset/dataset_number")
    
    with open ("dataset_number.csv", "w") as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    
    create("zebra")
    create("bay_horse")

if __name__ == "__main__":
    main()