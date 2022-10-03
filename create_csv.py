import os
import csv

def create_absolute(name_class, number):
    return f"C:/Users/miste/PycharmProjects/pythonProject2/dataset/{name_class}/{str(number).zfill(4)}.jpg"
 
def create_relative(name_class, number):
    return f"dataset/{name_class}/{str(number).zfill(4)}.jpg"

def write_in_file(name_class, number):
    with open ("dataset/dataset.csv", "a") as file:
        write = csv.writer(file, delimiter=";")
        writer.writerow( [create_absolute(name_class, number), create_relative(name_class, number), name_class] )

def main():
    for i in range(0, 1050):
        name_class = "zebra"
        way = f"dataset/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)
        name_class = "bay_horse"
        way = f"dataset\{name_class}\{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)

with open("dataset\dataset.csv", "w") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow( ["The Absolute Way", "Relative Way", "Class"] )
    main()