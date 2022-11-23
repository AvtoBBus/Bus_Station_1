import pandas as pd
import csv
import re
import cv2
import os


def read_csv(way_to_file: str, number_of_cell: int) -> list:
    read_list = []
    file = open(way_to_file, "r", encoding="utf-8")
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        if number_of_cell == 1:
            row_to_app = re.split(";", str(row))[number_of_cell]
        else:
            row_to_app = re.split(";", str(row))[number_of_cell][0:-2]
        read_list.append(row_to_app)
    return read_list


def start_create() -> None:
    list_abs_way = read_csv("dataset.csv", 1)
    list_name_class = read_csv("dataset.csv", 2)
    list_bin = ["Num point"]
    list_image_width = ["Image width"]
    list_image_hight = ["Image hight"]
    list_image_depth = ["Number of chanel"]
    for row in list_name_class:
        if row == "zebra":
            list_bin.append("0")
        if row == "bay_horse":
            list_bin.append("1")
    for way in list_abs_way:
        try:
            image = cv2.imread(way)
            list_image_width.append(image.shape[1])
            list_image_hight.append(image.shape[0])
            list_image_depth.append(image.shape[2])
        except:
            pass
    for i in range(1, len(list_abs_way)):
        try:
            list_abs_way[i] = os.path.abspath(list_abs_way[i])
        except:
            pass
    list_abs_way[0] = "The Absolute way"
    ser = pd.DataFrame(
        {
            list_name_class[0]: pd.array(list_name_class[1:]),
            list_abs_way[0]: pd.array(list_abs_way[1:]),
            list_bin[0]: pd.array(list_bin[1:]),
            list_image_width[0]: pd.array(list_image_width[1:]),
            list_image_hight[0]: pd.array(list_image_hight[1:]),
            list_image_depth[0]: pd.array(list_image_depth[1:])
        }
    )
    print(ser)


if __name__ == "__main__":
    start_create()
