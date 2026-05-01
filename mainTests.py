import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

from design import Ui_MainWindow
from secwin import Equations


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.buttn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.buttn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.buttn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.buttn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.buttn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.buttn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.buttn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.buttn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.buttn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.buttn_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.buttn_opwin.clicked.connect(self.show_secwin)

    def show_secwin(self):
        self.w2 = Equations()
        self.w2.show()

    def add_digit(self, buttn_text: str) -> None:
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(buttn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + buttn_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
