import os
import csv
from class_iterator import Iterator
import get_way

'''записывает в файл'''


def write_in_file(name_class, number):
    with open("dataset.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [get_way.create_absolute_way(name_class, number, "download"),
             get_way.create_download_relative_way(name_class, number),
             name_class]
        )


def main():
    with open("dataset.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";", )
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    iter = Iterator()
    while iter.num != 1050:
        name_class = "zebra"
        way = f"dataset/download_data/{name_class}/{str(iter.num).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, iter.num)
        name_class = "bay_horse"
        way = f"dataset/download_data/{name_class}/{str(iter.num).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, iter.num)
        next(iter)


if __name__ == "__main__":
    main()
