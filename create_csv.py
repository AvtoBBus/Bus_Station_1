from lib2to3.pgen2.token import NEWLINE
import os
import csv

'''возвращает абослютный путь'''
def create_absolute_way(name_class, number):
    return f"C:/Users/miste/PycharmProjects/pythonProject2/dataset/{name_class}/{str(number).zfill(4)}.jpg"
 
'''возвращает относительный путь'''
def create_relative_way(name_class, number):
    return f"dataset/{name_class}/{str(number).zfill(4)}.jpg"

'''записывает в файл'''
def write_in_file(name_class, number):
    with open ("dataset.csv", "a", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow( [create_absolute_way(name_class, number), create_relative_way(name_class, number), name_class] )

def main():
    with open("dataset.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";", )
        printer.writerow( ["The Absolute Way", "Relative Way", "Class"] )
    for number in range(0, 1050):
        name_class = "zebra"
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, number)
        name_class = "bay_horse"
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, number)


if __name__ == "__main__":
    main()