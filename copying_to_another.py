import os
import shutil

def create_new_way(name_class, number):
    return f"dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"

def main():
    if not os.path.isdir("dataset/dataset_another"):
        os.mkdir("dataset/dataset_another")
    for number in range(0, 1050):
        name_class = "zebra"
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(name_class, number))
        name_class = "bay_horse"
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(name_class, number))

if __name__ == "__main__":
    main()