# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    \n"
"    background-color: rgb(184, 215, 255);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 241, 51))
        self.label.setStyleSheet("font: 23pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(170, 510, 141, 61))
        self.upload.setStyleSheet("background-color: rgb(255, 243, 235);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.upload.setObjectName("upload")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 240, 471, 221))
        self.result.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.result.setText("")
        self.result.setWordWrap(True)
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.upload.clicked.connect(self.uploaded)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def uploaded(self):
        fname = QFileDialog.getOpenFileName()
        path = fname[0]
        import cv2
        d = cv2.QRCodeDetector()
        val, points, straight_qrcode = d.detectAndDecode(cv2.imread(path))
        is_link = False
        is_text = False
        val_list = list(val)
        for x in val_list:
            if ':' in val_list:
                is_text = False
                is_link = True
            else:
                is_text = True
                is_link = False

        if is_text:
            self.result.setText(val)
        elif is_link:
            import pyautogui
            pyautogui.hotkey('win', 'r')
            pyautogui.write(val)
            pyautogui.press('enter')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Scan QRCode"))
        self.upload.setText(_translate("MainWindow", "Upload"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
