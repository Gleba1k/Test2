import sys
import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 450)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:1, y2:0, stop:1 rgba(0, 169, 189, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb 199, 170, 127);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 272, 131, 21))
        self.pushButton.setStyleSheet("border-color: rgb(0, 255, 127);")
        self.pushButton.setObjectName("pushButton")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(230, 200, 141, 18))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(230, 230, 161, 18))
        self.checkBox_2.setObjectName("checkBox_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # кнопка для функції генерації пароля
        self.pushButton.clicked.connect(self.generate_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролів"))
        self.label.setText(_translate("MainWindow", "           Пороль створювач"))
        self.label_2.setText(_translate("MainWindow", "Результат"))
        self.pushButton.setText(_translate("MainWindow", "Натискнути!"))
        self.checkBox.setText(_translate("MainWindow", "числа"))
        self.checkBox_2.setText(_translate("MainWindow", "алфавіт"))
    
    def generate_password(self):
        length = 10  # Довжина пароля
        characters = ""
        if self.checkBox.isChecked():
            characters += string.digits
        if self.checkBox_2.isChecked():
            characters += string.ascii_letters
        
        if not characters:
            self.label_2.setText("Оберіть параметри!")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.label_2.setText(password)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
