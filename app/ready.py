from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from dbconnect import DbConnection
from style import widgets_style
import re


class Ui_MainWindow:

    def __init__(self):
        self.db_worker = DbConnection()

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 445)
        icon = QIcon('style/redone.png')
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_destroy_button()
        self.create_count_button()
        self.create_find_button()
        self.create_edit_text()
        self.create_label()
        self.create_label_result()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_destroy_button(self):
        self.destroy_button = QtWidgets.QPushButton(self.centralwidget)
        self.destroy_button.setGeometry(QtCore.QRect(280, 80, 205, 205))
        self.destroy_button.setStyleSheet(widgets_style.push_butthon_sytle)
        self.destroy_button.setObjectName("destroyButton")
        self.destroy_button.clicked.connect(self.destroy_human)

    def create_count_button(self):
        self.count_button = QtWidgets.QPushButton(self.centralwidget)
        self.count_button.setGeometry(QtCore.QRect(280, 300, 90, 60))
        self.count_button.setObjectName("countButton")
        self.count_button.clicked.connect(self.count_clients)

    def create_find_button(self):
        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_button.setGeometry(QtCore.QRect(400, 300, 90, 60))
        self.find_button.setObjectName("findButton")
        self.find_button.clicked.connect(self.find_client)

    def create_edit_text(self):
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(10, 160, 231, 41))
        self.text_edit.setObjectName("textEdit")
        self.text_edit.setStyleSheet(widgets_style.edit_text_style)
        self.text_edit.setText('89068225814')
        self.text_edit.textChanged.connect(self.validate_input)

    def create_label(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 181, 31))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

    def create_label_result(self):
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(40, 220, 211, 31))
        self.label_result.setFrameShape(QtWidgets.QFrame.Box)
        self.label_result.setLineWidth(0)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Уничтожение"))
        self.destroy_button.setText(_translate("MainWindow", "DELETE"))
        self.count_button.setText(_translate("MainWindow", "Количество"))
        self.find_button.setText(_translate("MainWindow", "Найти"))
        self.text_edit.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.text_edit.setHtml(_translate("MainWindow", widgets_style.edit_text_html))
        self.label.setText(_translate("MainWindow", "Номер телефона"))
        self.label_result.setText(_translate("MainWindow", ""))

    def destroy_human(self):
        phone = self.text_edit.toPlainText()
        result = self.db_worker.destroy_man(phone)
        self.label_result.setText(result)

    def count_clients(self):
        count = len(self.db_worker.get_all())
        self.label_result.setText(f'Записей всего = {count}')

    def find_client(self):

        def string_answer(list_answer: list):
            result = [str(i) for i in list_answer if i]
            return ','.join(result)

        phone = self.text_edit.toPlainText()
        client = self.db_worker.get_by_phone(phone)
        result = 'Клиент не найден' if not client else string_answer(client)
        self.label_result.setText(result)


    def validate_input(self):
        input_string = self.text_edit.toPlainText()
        if not input_string.isdigit() and len(input_string) > 0:
            num_string = re.sub(r'\D', '', input_string)
            self.text_edit.setText(num_string)
