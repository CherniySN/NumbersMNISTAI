from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1862, 837)
        Form.setStyleSheet("")
        self.openButton = QtWidgets.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(510, 760, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.openButton.setFont(font)
        self.openButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #093c57;\n"
"    border-radius: 9;\n"
"    border: 1px solid #07adba;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1388c5;\n"
"    border: 1px solid #057a83;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #154560;\n"
"    border: 2px solid #00ccff;\n"
"}\n"
"")
        self.openButton.setObjectName("openButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.openButton)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(-10, -50, 1891, 941))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Analysis treaty of share of the partnership/Фон1.jpg"))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1450, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1380, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.RunRe = QtWidgets.QPushButton(Form)
        self.RunRe.setGeometry(QtCore.QRect(680, 760, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.RunRe.setFont(font)
        self.RunRe.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #093c57;\n"
"    border-radius: 9;\n"
"    border: 1px solid #07adba;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1388c5;\n"
"    border: 1px solid #057a83;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #154560;\n"
"    border: 2px solid #00ccff;\n"
"}\n"
"")
        self.RunRe.setObjectName("RunRe")
        self.buttonGroup.addButton(self.RunRe)
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(1140, 760, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #093c57;\n"
"    border-radius: 9;\n"
"    border: 1px solid #07adba;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1388c5;\n"
"    border: 1px solid #057a83;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #154560;\n"
"    border: 2px solid #00ccff;\n"
"}\n"
"")
        self.Clear.setObjectName("Clear")
        self.buttonGroup.addButton(self.Clear)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1260, 110, 571, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.date_of_document = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.date_of_document.setFont(font)
        self.date_of_document.setStyleSheet("QLabel{color: white}")
        self.date_of_document.setObjectName("date_of_document")
        self.verticalLayout.addWidget(self.date_of_document)
        self.current_date = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.current_date.setFont(font)
        self.current_date.setStyleSheet("QLabel{color: white}")
        self.current_date.setObjectName("current_date")
        self.verticalLayout.addWidget(self.current_date)
        self.status_document = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.status_document.setFont(font)
        self.status_document.setStyleSheet("QLabel{color: white}")
        self.status_document.setObjectName("status_document")
        self.verticalLayout.addWidget(self.status_document)
        self.Year_of_document = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Year_of_document.setFont(font)
        self.Year_of_document.setStyleSheet("QLabel{color: white}")
        self.Year_of_document.setObjectName("Year_of_document")
        self.verticalLayout.addWidget(self.Year_of_document)
        self.deposit_amount = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.deposit_amount.setFont(font)
        self.deposit_amount.setStyleSheet("QLabel{color: white}")
        self.deposit_amount.setObjectName("deposit_amount")
        self.verticalLayout.addWidget(self.deposit_amount)
        self.numbers_of_flores = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.numbers_of_flores.setFont(font)
        self.numbers_of_flores.setStyleSheet("QLabel{color: white}")
        self.numbers_of_flores.setObjectName("numbers_of_flores")
        self.verticalLayout.addWidget(self.numbers_of_flores)
        self.number_of_flat = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.number_of_flat.setFont(font)
        self.number_of_flat.setStyleSheet("QLabel{color: white}")
        self.number_of_flat.setObjectName("number_of_flat")
        self.verticalLayout.addWidget(self.number_of_flat)
        self.flore = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.flore.setFont(font)
        self.flore.setStyleSheet("QLabel{color: white}")
        self.flore.setObjectName("flore")
        self.verticalLayout.addWidget(self.flore)
        self.value_of_rooms = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.value_of_rooms.setFont(font)
        self.value_of_rooms.setStyleSheet("QLabel{color: white}")
        self.value_of_rooms.setObjectName("value_of_rooms")
        self.verticalLayout.addWidget(self.value_of_rooms)
        self.Chek_INN = QtWidgets.QPushButton(Form)
        self.Chek_INN.setGeometry(QtCore.QRect(850, 760, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Chek_INN.setFont(font)
        self.Chek_INN.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #093c57;\n"
"    border-radius: 9;\n"
"    border: 1px solid #07adba;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1388c5;\n"
"    border: 1px solid #057a83;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #154560;\n"
"    border: 2px solid #00ccff;\n"
"}\n"
"")
        self.Chek_INN.setObjectName("Chek_INN")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(50, 110, 1161, 621))
        self.graphicsView.setStyleSheet("QGraphicsView {\n"
"    \n"
"    background-color: #FFFFFF;\n"
"    border-radius: 9;\n"
"    border: 2px solid #07adba;\n"
"\n"
"}\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.label_7.raise_()
        self.openButton.raise_()
        self.RunRe.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.Clear.raise_()
        self.verticalLayoutWidget.raise_()
        self.Chek_INN.raise_()
        self.graphicsView.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open(self):  # открываем файловый диалог
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]  # читаем путь до выбранного файла
        if fname:
                pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Автоматический расчет дохода АРД v.1.0"))
        self.openButton.setText(_translate("Form", "Открыть"))
        self.label.setText(_translate("Form", "8 961 390 31 38"))
        self.label_2.setText(_translate("Form", "По вопросам работы программы"))
        self.RunRe.setText(_translate("Form", "Обработать"))
        self.Clear.setText(_translate("Form", "Очистить"))
        self.date_of_document.setText(_translate("Form", "Дата документа:"))
        self.current_date.setText(_translate("Form", "Текущая дата:"))
        self.status_document.setText(_translate("Form", "Срок действия документа:"))
        self.Year_of_document.setText(_translate("Form", "Года за который начислялась зп:"))
        self.deposit_amount.setText(_translate("Form", "Количество месяцев:"))
        self.numbers_of_flores.setText(_translate("Form", "Общая сумма дохода:"))
        self.number_of_flat.setText(_translate("Form", "Доход за последние (3-6 месяцев):"))
        self.flore.setText(_translate("Form", "Среднемесячный доход:"))
        self.value_of_rooms.setText(_translate("Form", "ИНН организации:"))
        self.Chek_INN.setText(_translate("Form", "Проверка работодателя"))


