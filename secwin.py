from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QFontDatabase

from designsqr import Ui_SecWindow
import math


class Equations(QMainWindow):
    def __init__(self):
        super(Equations, self).__init__()
        self.ui = Ui_SecWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")
        self.ui.buttn_sqrans.clicked.connect(self.count)

    def StyleSheet(self):
        self.ui.label_sqra.setStyleSheet("color: white;\n"
                                         "font-family: Rubik;\n"
                                         "font-size: 28pt;\n"
                                         "font-weight: 700;")

    def count(self):

        c = self.ui.lineEdit_sqrx.text()
        b = self.ui.lineEdit_sqrx2.text()
        a = self.ui.lineEdit_sqrx3.text()
        if c == '':
            c = 0
        if b == '':
            b = 1
        if a == '':
            a = 1

        c = int(c)
        b = int(b)
        a = int(a)
        if a != 0:
            if b**2 - (4*a*c) == 0:
               ans = str("x1 =") + str(-b / 2*a)
               self.StyleSheet()
               self.ui.label_sqra.setText(ans)

            elif b**2 - (4*a*c) > 0:
               if ((-b + math.sqrt(b**2-(4*a*c)))/2*a) % 1 != 0:
                   preans = round(((-b + math.sqrt((b**2)+(-4*a*c)))/(2*a)), 3)
                   preans2 = round(((-b - math.sqrt((b**2)+(-4*a*c)))/(2*a)), 3)
                   ans = str("x1 ≈") + str(preans)
                   ans2 = str("x2 ≈") + str(preans2)
                   self.StyleSheet()
                   self.ui.label_sqra.setText(ans)
                   self.ui.label_sqra2.setText(ans2)
               else:
                   ans = str("x1 = ") + str((-b + math.sqrt((b**2) + (-4 * a * c))) / (2 * a))
                   ans2 = str("x2 = ") + str((-b - math.sqrt((b**2) + (-4 * a * c))) / (2 * a))
                   self.StyleSheet()
                   self.ui.label_sqra.setText(ans)
                   self.ui.label_sqra2.setText(ans2)

            elif b ** 2 - (4 * a * c) < 0:
               self.StyleSheet()
               self.ui.label_sqra.setText("Корней нет")
               self.ui.label_sqra2.setText("")
        if a == 0:
            ans = str("x1 = ") + str((-c) / b)
            self.StyleSheet()
            self.ui.label_sqra.setText(ans)
            self.ui.label_sqra2.setText("")






