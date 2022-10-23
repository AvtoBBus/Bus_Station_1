from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Пук")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.button_create_another = QtWidgets.QPushButton(self)
        self.button_create_another.move(40, 100)
        self.button_create_another.setText(
            "Создать копию dataset с другими названиями")
        self.button_create_another.adjustSize()

        self.button_create_with_new_number = QtWidgets.QPushButton(self)
        self.button_create_with_new_number.move(30, 80)
        self.button_create_with_new_number.setText(
            "Создать копию dataset со случайными номерами")
        self.button_create_with_new_number.adjustSize()

        self.button_create_with_new_number.clicked.connect(
            self.create_new_number)
        self.button_create_another.clicked.connect(self.create_another)

    def create_another(self):
        self.new_text.setText("another")
        self.new_text.adjustSize()

    def create_new_number(self):
        self.new_text.setText("number")
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
