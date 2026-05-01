from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecWindow(object):
    def setupUi(self, SecWindow):
        SecWindow.setObjectName("SecWindow")
        SecWindow.resize(650, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecWindow.sizePolicy().hasHeightForWidth())
        SecWindow.setSizePolicy(sizePolicy)
        SecWindow.setMinimumSize(QtCore.QSize(650, 350))
        SecWindow.setMaximumSize(QtCore.QSize(650, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SecWindow.setWindowIcon(icon)
        SecWindow.setStyleSheet("QWidget {\n"
"   color: white;\n"
"    background-color: #aad4e1;\n"
"    font-family: Rubik;\n"
"    font-size: 15pt;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #B0C4DE;\n"
"    color: #4682B4;\n"
"}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(SecWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 621, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_sqrx3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_sqrx3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_sqrx3.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 30pt;\n"
"font-weight: 600;")
        self.lineEdit_sqrx3.setText("")
        self.lineEdit_sqrx3.setMaxLength(4)
        self.lineEdit_sqrx3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sqrx3.setObjectName("lineEdit_sqrx3")
        self.horizontalLayout.addWidget(self.lineEdit_sqrx3)
        self.label_sqrx = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sqrx.sizePolicy().hasHeightForWidth())
        self.label_sqrx.setSizePolicy(sizePolicy)
        self.label_sqrx.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 32pt;\n"
"font-weight: 700;")
        self.label_sqrx.setObjectName("label_sqrx")
        self.horizontalLayout.addWidget(self.label_sqrx)
        self.lineEdit_sqrx2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_sqrx2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_sqrx2.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 30pt;\n"
"font-weight: 600;")
        self.lineEdit_sqrx2.setText("")
        self.lineEdit_sqrx2.setMaxLength(4)
        self.lineEdit_sqrx2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sqrx2.setObjectName("lineEdit_sqrx2")
        self.horizontalLayout.addWidget(self.lineEdit_sqrx2)
        self.label_sqrx2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sqrx2.sizePolicy().hasHeightForWidth())
        self.label_sqrx2.setSizePolicy(sizePolicy)
        self.label_sqrx2.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 32pt;\n"
"font-weight: 700;")
        self.label_sqrx2.setObjectName("label_sqrx2")
        self.horizontalLayout.addWidget(self.label_sqrx2)
        self.lineEdit_sqrx = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_sqrx.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_sqrx.setAutoFillBackground(False)
        self.lineEdit_sqrx.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 30pt;\n"
"font-weight: 600;")
        self.lineEdit_sqrx.setText("")
        self.lineEdit_sqrx.setMaxLength(4)
        self.lineEdit_sqrx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sqrx.setObjectName("lineEdit_sqrx")
        self.horizontalLayout.addWidget(self.lineEdit_sqrx)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 32pt;\n"
"font-weight: 700;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.buttn_sqrans = QtWidgets.QPushButton(SecWindow)
        self.buttn_sqrans.setGeometry(QtCore.QRect(540, 170, 91, 41))
        self.buttn_sqrans.setObjectName("buttn_sqrans")
        self.label_sqra = QtWidgets.QLabel(SecWindow)
        self.label_sqra.setGeometry(QtCore.QRect(80, 230, 211, 51))
        self.label_sqra.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 28pt;\n"
"font-weight: 700;")
        self.label_sqra.setObjectName("label_sqra")
        self.label_sqra2 = QtWidgets.QLabel(SecWindow)
        self.label_sqra2.setGeometry(QtCore.QRect(330, 230, 231, 51))
        self.label_sqra2.setStyleSheet("color: white;\n"
"font-family: Rubik;\n"
"font-size: 28pt;\n"
"font-weight: 700;")
        self.label_sqra2.setObjectName("label_sqra2")

        self.retranslateUi(SecWindow)
        QtCore.QMetaObject.connectSlotsByName(SecWindow)

    def retranslateUi(self, SecWindow):
        _translate = QtCore.QCoreApplication.translate
        SecWindow.setWindowTitle(_translate("SecWindow", "Калькулятор"))
        self.label_sqrx.setText(_translate("SecWindow", "x² +"))
        self.label_sqrx2.setText(_translate("SecWindow", "x +"))
        self.label_3.setText(_translate("SecWindow", " =  0"))
        self.buttn_sqrans.setText(_translate("SecWindow", "Ent"))
        self.label_sqra.setText(_translate("SecWindow", "x1 "))
        self.label_sqra2.setText(_translate("SecWindow", "x2 "))

import files_rc
