from genericpath import isfile
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont, QIcon

import sys
import copying_to_another
import copying_with_new_number
import create_csv
import iterator
import os


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.iterat_zebra = iterator.Iterator("dataset.csv", "zebra")
        self.iterat_bay_horse = iterator.Iterator(
            "dataset.csv", "bay_horse")
        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Please select folder of dataset')

        self.font_in_label = QFont("Times", 12, QFont.Bold)
        self.x_size_label = 600
        self.y_size_label = 40

        self.label_img_zebra = QLabel(self)
        self.label_img_bay_horse = QLabel(self)
        self.label_img_zebra.setFixedSize(500, 400)
        self.label_img_bay_horse.setFixedSize(500, 400)

        self.label_folderpath_text = QLabel(self)
        self.label_folderpath_text.setFont(QFont("Times", 10))
        self.label_folderpath_text.setText(
            "Выбранный путь до dataset: " + self.folderpath_dataset)
        self.label_folderpath_text.setStyleSheet("color: rgb(200, 200, 200);")
        self.label_folderpath_text.adjustSize()

        self.info_text_label = QLabel(self)
        self.info_text_label.setFont(self.font_in_label)

        self.setWindowTitle("Лапка 3")
        self.setFixedSize(1280, 720)
        self.move(320, 180)

        self.button_create_annotation = QtWidgets.QPushButton(self)
        self.button_create_annotation.setFont(self.font_in_label)
        self.button_create_annotation.setText(
            "Создать аннотацию к dataset")
        self.button_create_annotation.setGeometry(
            340, 60, self.x_size_label, self.y_size_label)
        self.button_create_annotation.setIcon(
            QIcon("button_icons\csv_icon.png"))
        self.button_create_annotation.setStyleSheet(
            "background: rgb(255, 24, 24);")

        self.button_create_another = QtWidgets.QPushButton(self)
        self.button_create_another.setFont(self.font_in_label)
        self.button_create_another.setText(
            "Создать копию dataset с другими названиями")
        self.button_create_another.setGeometry(
            340, 100, self.x_size_label, self.y_size_label)
        self.button_create_another.setIcon(
            QIcon("button_icons\create_to_another.png"))
        self.button_create_another.setStyleSheet(
            "background: rgb(255, 179, 24);")

        self.button_create_with_new_number = QtWidgets.QPushButton(self)
        self.button_create_with_new_number.setFont(self.font_in_label)
        self.button_create_with_new_number.setText(
            "Создать копию dataset со случайными номерами")
        self.button_create_with_new_number.setGeometry(
            340, 140, self.x_size_label, self.y_size_label)
        self.new_text = QtWidgets.QLabel(self)
        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)
        self.button_create_with_new_number.setIcon(
            QIcon("button_icons\create_with_new_number.png"))
        self.button_create_with_new_number.setStyleSheet(
            "background: rgb(148, 255, 24);")

        self.button_next_bay_horse = QtWidgets.QPushButton(self)
        self.button_next_bay_horse.setFont(self.font_in_label)
        self.button_next_bay_horse.setText(
            "Следующая картинка c гнедой лошадью")
        self.button_next_bay_horse.setGeometry(
            340, 180, self.x_size_label, self.y_size_label)
        self.button_next_bay_horse.setIcon(
            QIcon("button_icons/next_bay_horse.png"))
        self.button_next_bay_horse.setStyleSheet(
            "background: rgb(24, 101, 255);")

        self.button_next_zebra = QtWidgets.QPushButton(self)
        self.button_next_zebra.setFont(self.font_in_label)
        self.button_next_zebra.setText(
            "Следующая картинка c зеброй")
        self.button_next_zebra.setGeometry(
            340, 220, self.x_size_label, self.y_size_label)
        self.button_next_zebra.setIcon(
            QIcon("button_icons/next_zebra.png"))
        self.button_next_zebra.setStyleSheet(
            "background: rgb(225, 24, 255);")

        self.button_next_zebra.clicked.connect(self.next_zebra)
        self.button_next_bay_horse.clicked.connect(self.next_bay_horse)
        self.button_create_annotation.clicked.connect(self.create_annotation)
        self.button_create_another.clicked.connect(self.create_another)
        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)

    def next_zebra(self) -> None:
        self.info_text_label.clear()
        if os.path.isfile("dataset.csv"):
            self.elem = next(self.iterat_zebra)
            while self.elem == None:
                self.elem = next(self.iterat_zebra)
            if os.path.isfile(str(self.elem)):
                self.label_img_zebra.clear()
                self.label_img_zebra.setPixmap(QPixmap(str(self.elem)))
                self.label_img_zebra.adjustSize()
                self.label_img_zebra.move(670, 300)
                self.label_img_zebra.show()
        else:
            self.info_text_label.setText(
                "ERROR: DON'T FIND FILE 'dataset.csv'!")
            self.info_text_label.move(0, 695)
            self.info_text_label.adjustSize()

    def next_bay_horse(self) -> None:
        self.info_text_label.clear()
        if os.path.isfile("dataset.csv"):
            self.elem = next(self.iterat_zebra)
            self.elem = next(self.iterat_bay_horse)
            while self.elem == None:
                self.elem = next(self.iterat_bay_horse)
            if os.path.isfile(str(self.elem)):
                self.label_img_bay_horse.clear()
                self.label_img_bay_horse.setPixmap(QPixmap(str(self.elem)))
                self.label_img_bay_horse.adjustSize()
                self.label_img_bay_horse.move(50, 300)
                self.label_img_bay_horse.show()
        else:
            self.info_text_label.setText(
                "ERROR: DON'T FIND FILE 'dataset.csv'!")
            self.info_text_label.move(0, 695)
            self.info_text_label.adjustSize()

    def create_annotation(self):
        create_csv.main(self.folderpath_dataset)

    def create_another(self):
        copying_to_another.main()
        self.info_text_label.setText("Finish create another dataset!")
        self.info_text_label.move(0, 695)
        self.info_text_label.adjustSize()

    def create_new_number(self):
        copying_with_new_number.main()
        self.info_text_label.setText(
            "Finish create dataset with random numbers!")
        self.info_text_label.move(0, 695)
        self.info_text_label.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        "#MainWindow{border-image:url(The_beautifulest_background.jpg)}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
