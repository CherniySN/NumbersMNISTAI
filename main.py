import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *
from datetime import datetime
import Teseract
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By


class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.doc = ''
        self.set()
        self.fname = ''

    def run(self):
        try:
            Teseract.teseracted(self.fname)
            print(self.fname)
            self.image_qt = QImage('C:/Users/pc/PycharmProjects/NumbersMNISTAI-master/result.jpg')
            pic = QGraphicsPixmapItem()
            pic.setPixmap(QPixmap.fromImage(self.image_qt))
            self.scene.setSceneRect(0, 0, 1600, 1600)
            self.scene.addItem(pic)
        except:
            print('Чет не то')

    def open(self):  # открываем файловый диалог
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]  # читаем путь до выбранного файла
        self.fname = fname

        if fname:
            self.image_qt = QImage(fname)

            pic = QGraphicsPixmapItem()
            pic.setPixmap(QPixmap.fromImage(self.image_qt))
            self.scene.setSceneRect(0, 0, 1600, 1600)
            self.scene.addItem(pic)

    def check(self):

        browser = webdriver.Chrome()  # запускаем брайзер
        browser.get("https://zachestnyibiznes.ru/")
        browser.implicitly_wait(5)  # что бы сайт не закрывался

        try:
            find = browser.find_element(By.ID, 'autocomplete-0-input')
            find.send_keys('7736646678')

            time.sleep(2)

            share = browser.find_element(By.CLASS_NAME, 'aa-SubmitIcon')
            share.click()

            # objects = browser.find_element(By.CSS_SELECTOR, '[data-name="CardComponent"] h1') # ищем заголовок с помощью селектора
            # print(objects.text) # получаем и выводим текст
        except:
            print('Что-то идет не так.')

        time.sleep(10)
        browser.close()  # обяхательно закрываем сайт

    def clear(self):
        self.scene.clear()
        self.w_root.graphicsView.setScene(self.scene)
        self.w_root.date_of_document.setText('Дата документа:')
        self.w_root.current_date.setText('Дата документа: ' + str(datetime.now().date()))
        self.w_root.status_document.setText('Срок действия документа:')
        self.w_root.Year_of_document.setText('Года за который начислялась зп:')
        self.w_root.value_of_nouth.setText('Количество месяцев:')
        self.w_root.total_salary.setText('Общая сумма дохода:')
        self.w_root.salary.setText('Доход за последние (3-6 месяцев):')
        self.w_root.avg_salary.setText('Среднемесячный доход:')
        self.w_root.INN_of_comp.setText('ИНН организации:')

    def set(self):
        self.w_root = uic.loadUi('UI.ui')
        self.w_root.current_date.setText('Дата документа: ' + str(datetime.now().date()))
        self.w_root.openButton.clicked.connect(self.open)  # событие нажатие на кнопку
        self.w_root.Clear.clicked.connect(self.clear)  # очищаем поле
        self.w_root.RunRe.clicked.connect(self.run)  # событие нажатие на кнопку
        self.w_root.Chek_INN.clicked.connect(self.check)  # событие нажатие на кнопку
        self.scene = QGraphicsScene()
        self.w_root.graphicsView.setScene(self.scene)
        self.w_root.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
