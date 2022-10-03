import os
import shutil

def create_new_way(number):
    return f"dataset/dataset_number/{number}.jpg"

def create(name_class):
    for number in range(0, 1050):
        way = f"dataset/{name_class}/{str(number).zfill(4)}.jpg"
        if os.path.isfile(way):
            shutil.copyfile(way, create_new_way(number))

def main():
    if not os.path.isdir("dataset/dataset_number"):
        os.mkdir("dataset/dataset_number")
    create("zebra")
    create("bay_horse")

if __name__ == "__main__":
    main()