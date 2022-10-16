import os
import shutil
import csv
import random
from class_iterator import Iterator
import get_way

'''создаёт аннотацию'''


def create_annotation(name_class, number):
    with open("dataset_number.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [get_way.create_absolute_way(name_class, number, "number"),
             get_way.create_number_relative_way(number),
             name_class]
        )


'''создаёт копии'''


def copy_with_new_number(name_class):
    iter = Iterator()
    while iter.num != 1050:
        way = f"dataset/download_data/{name_class}/{str(iter.num).zfill(4)}.jpg"
        if os.path.isfile(way) == True:
            new_number = random.randint(0, 10001)
            while os.path.isfile(get_way.create_number_relative_way(new_number)) == True:
                new_number = random.randint(0, 10001)
            shutil.copyfile(
                way, get_way.create_number_relative_way(new_number))
            create_annotation(name_class, new_number)
        next(iter)


def main():
    if not os.path.isdir("dataset/dataset_number"):
        os.mkdir("dataset/dataset_number")

    with open("dataset_number.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])

    copy_with_new_number("zebra")
    copy_with_new_number("bay_horse")


if __name__ == "__main__":
    main()
