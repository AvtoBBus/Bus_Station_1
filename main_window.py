from cgitb import text
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
        self.iterat_bay_horse = iterator.Iterator("dataset.csv", "bay_horse")
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Please select folder of dataset')

        self.font_in_label = QFont("Times", 12, QFont.Bold)
        self.x_size_label = 600
        self.y_size_label = 40

        self.label_img_zebra = QLabel(self)
        self.label_img_bay_horse = QLabel(self)
        self.label_img_zebra.setFixedSize(500, 400)
        self.label_img_bay_horse.setFixedSize(500, 400)

        self.setWindowTitle("Лапка")
        self.setFixedSize(1280, 720)
        self.move(250, 250)

        self.button_create_annotation = QtWidgets.QPushButton(self)
        self.button_create_annotation.setFont(self.font_in_label)
        self.button_create_annotation.setText(
            "Создать аннотацию к dataset")
        self.button_create_annotation.setGeometry(
            340, 50, self.x_size_label, self.y_size_label)
        self.button_create_annotation.setIcon(
            QIcon("button_icons\csv_icon.png"))

        self.button_create_another = QtWidgets.QPushButton(self)
        self.button_create_another.setFont(self.font_in_label)
        self.button_create_another.setText(
            "Создать копию dataset с другими названиями")
        self.button_create_another.setGeometry(
            340, 90, self.x_size_label, self.y_size_label)
        self.button_create_another.setIcon(
            QIcon("button_icons\create_to_another.png"))

        self.button_create_with_new_number = QtWidgets.QPushButton(self)
        self.button_create_with_new_number.setFont(self.font_in_label)
        self.button_create_with_new_number.setText(
            "Создать копию dataset со случайными номерами")
        self.button_create_with_new_number.setGeometry(
            340, 130, self.x_size_label, self.y_size_label)
        self.new_text = QtWidgets.QLabel(self)
        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)
        self.button_create_with_new_number.setIcon(
            QIcon("button_icons\create_with_new_number.png"))

        self.button_next_bay_horse = QtWidgets.QPushButton(self)
        self.button_next_bay_horse.setFont(self.font_in_label)
        self.button_next_bay_horse.setText(
            "Следующая картинка c гнедой лошадью")
        self.button_next_bay_horse.setGeometry(
            340, 170, self.x_size_label, self.y_size_label)
        self.button_next_bay_horse.setIcon(
            QIcon("button_icons/next_bay_horse.png"))

        self.button_next_zebra = QtWidgets.QPushButton(self)
        self.button_next_zebra.setFont(self.font_in_label)
        self.button_next_zebra.setText(
            "Следующая картинка c зеброй")
        self.button_next_zebra.setGeometry(
            340, 210, self.x_size_label, self.y_size_label)
        self.button_next_zebra.setIcon(
            QIcon("button_icons/next_zebra.png"))

        self.button_next_zebra.clicked.connect(self.next_zebra)
        self.button_next_bay_horse.clicked.connect(self.next_bay_horse)
        self.button_create_annotation.clicked.connect(self.create_annotation)
        self.button_create_another.clicked.connect(self.create_another)
        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)

    def next_zebra(self) -> None:
        self.elem = next(self.iterat_zebra)
        while self.elem == None:
            self.elem = next(self.iterat_zebra)
        if os.path.isfile(str(self.elem)):
            self.label_img_zebra.clear()
            self.label_img_zebra.setPixmap(QPixmap(str(self.elem)))
            self.label_img_zebra.adjustSize()
            self.label_img_zebra.move(670, 300)
            self.label_img_zebra.show()

    def next_bay_horse(self) -> None:
        self.elem = next(self.iterat_bay_horse)
        while self.elem == None:
            self.elem = next(self.iterat_bay_horse)
        if os.path.isfile(str(self.elem)):
            self.label_img_bay_horse.clear()
            self.label_img_bay_horse.setPixmap(QPixmap(str(self.elem)))
            self.label_img_bay_horse.adjustSize()
            self.label_img_bay_horse.move(50, 300)
            self.label_img_bay_horse.show()

    def create_annotation(self):
        create_csv.main(self.folderpath)

    def create_another(self):
        copying_to_another.main()
        self.new_text.setText("Finish create another dataset!")
        self.new_text.move(0, 695)

    def create_new_number(self):
        copying_with_new_number.main()
        self.new_text.setText("Finish create dataset with random numbers!")
        self.new_text.adjustSize()


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
