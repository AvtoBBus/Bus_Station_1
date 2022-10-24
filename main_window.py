from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

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

        self.label_img_zebra = QLabel(self)
        self.label_img_bay_horse = QLabel(self)

        self.setWindowTitle("Лапка")
        self.setGeometry(250, 250, 1280, 720)

        self.button_create_annotation = QtWidgets.QPushButton(self)
        self.button_create_annotation.move(30, 50)
        self.button_create_annotation.setText(
            "Создать аннотацию к dataset")
        self.button_create_annotation.adjustSize()

        self.button_create_another = QtWidgets.QPushButton(self)
        self.button_create_another.move(30, 75)
        self.button_create_another.setText(
            "Создать копию dataset с другими названиями")
        self.button_create_another.adjustSize()

        self.button_create_with_new_number = QtWidgets.QPushButton(self)
        self.button_create_with_new_number.move(30, 100)
        self.button_create_with_new_number.setText(
            "Создать копию dataset со случайными номерами")
        self.button_create_with_new_number.adjustSize()
        self.new_text = QtWidgets.QLabel(self)
        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)

        self.button_next_bay_horse = QtWidgets.QPushButton(self)
        self.button_next_bay_horse.move(30, 125)
        self.button_next_bay_horse.setText(
            "Следующая картинка c гнедой лошадью")
        self.button_next_bay_horse.adjustSize()

        self.button_next_zebra = QtWidgets.QPushButton(self)
        self.button_next_zebra.move(30, 150)
        self.button_next_zebra.setText(
            "Следующая картинка c зеброй")
        self.button_next_zebra.adjustSize()

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
            self.label_img_zebra.move(500, 10)
            self.label_img_zebra.show()

    def next_bay_horse(self) -> None:
        self.elem = next(self.iterat_bay_horse)
        while self.elem == None:
            self.elem = next(self.iterat_bay_horse)
        if os.path.isfile(str(self.elem)):
            self.label_img_bay_horse.clear()
            self.label_img_bay_horse.setPixmap(QPixmap(str(self.elem)))
            self.label_img_bay_horse.adjustSize()
            self.label_img_bay_horse.move(10, 300)
            self.label_img_bay_horse.show()

    def create_annotation(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Please select folder of dataset')
        create_csv.main(folderpath)

    def create_another(self):
        copying_to_another.main()
        self.new_text.setText("Finish create another dataset!")
        self.new_text.adjustSize()

    def create_new_number(self):
        copying_with_new_number.main()
        self.new_text.setText("Finish create dataset with random numbers!")
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
