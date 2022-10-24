import os
import csv
from iterator import Iterator
import get_way


def write_in_file(name_class: str, number: int) -> None:
    '''
    запись в csv-файл(абсолютный путь/относительный путь/тег класса)
    '''
    with open("dataset.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [os.path.abspath(get_way.create_download_relative_way(name_class, number)),
             get_way.create_download_relative_way(name_class, number),
             name_class]
        )


def main(folderpath: str) -> None:
    '''
    создание csv-файла
    поочерёдная запись в файл-аннотацию из папки download_data
    '''
    num_files = len([f for f in os.listdir(folderpath + "/zebra")
                     if os.path.isfile(os.path.join(folderpath + "/zebra", f))])
    with open("dataset.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";", )
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    for i in range(0, num_files):
        name_class = "zebra"
        way = f"{folderpath}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)
        name_class = "bay_horse"
        way = f"{folderpath}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)


if __name__ == "__main__":
    main("dataset/download_data")
