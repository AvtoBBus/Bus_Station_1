import os
import csv
import shutil
from iterator import Iterator
import get_way


def create_annotation(name_class: str, number: int) -> None:
    '''
    создаёт csv файл-аннотацию(абсолютный путь/относительный путь/тег класса)
    '''
    with open("dataset_another.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [os.path.abspath(get_way.create_another_relative_way(name_class, number)),
             get_way.create_another_relative_way(name_class, number),
             name_class]
        )


def create_copy(name_class: str) -> None:
    '''
    создаёт копии в новой папке
    '''
    iterat = Iterator("dataset.csv", name_class)
    for elem in iterat:
        if elem != None:
            if os.path.isfile(str(elem)):
                shutil.copyfile(
                    str(elem), get_way.create_another_relative_way(name_class, iterat.counter))
            create_annotation(name_class, iterat.counter)


def main():
    if not os.path.isdir("dataset/dataset_another"):
        os.mkdir("dataset/dataset_another")
    with open("dataset_another.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    create_copy("zebra")
    create_copy("bay_horse")


if __name__ == "__main__":
    main()
