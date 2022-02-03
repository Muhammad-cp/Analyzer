# Импортирование библиотек и модулей
import sqlite3
import sys
import requests
import datetime

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

# Обьявление переменных
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
count_balance = 0
count_balance_round = 0
number_dollar = data['Valute']['USD']['Value']
dt_now = datetime.datetime.now()
value_id_income = 0
value_id_expenses = 0


class MainForm(QMainWindow):
    def __init__(self):
        global count_balance
        global count_balance_round
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 520)
        self.setWindowTitle('Анализатор')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Main_Window.jpg'))
        self.setStyleSheet("background-color: rgb(97, 97, 97);")

        self.label = QLabel(self)
        self.label.move(120, 320)
        self.label.resize(231, 41)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setStyleSheet("font: 75 italic 20pt \"Times New Roman\";")
        self.label.setText("Balance")

        self.label_2 = QLabel(self)
        self.label_2.move(220, 320)
        self.label_2.resize(221, 41)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 italic 20pt \"Times New Roman\";")
        self.label_2.setText("0,00 руб")

        self.pushButton = QPushButton(self)
        self.pushButton.move(150, 210)
        self.push# Импортирование библиотек и модулей
import sqlite3
import sys
import requests
import datetime

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

# Обьявление переменных
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
count_balance = 0
count_balance_round = 0
number_dollar = data['Valute']['USD']['Value']
dt_now = datetime.datetime.now()
value_id_income = 0
value_id_expenses = 0


class MainForm(QMainWindow):
    def __init__(self):
        global count_balance
        global count_balance_round
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 520)
        self.setWindowTitle('Анализатор')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Main_Window.jpg'))
        self.setStyleSheet("background-color: rgb(97, 97, 97);")

        self.label = QLabel(self)
        self.label.move(120, 320)
        self.label.resize(231, 41)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setStyleSheet("font: 75 italic 20pt \"Times New Roman\";")
        self.label.setText("Balance")

        self.label_2 = QLabel(self)
        self.label_2.move(220, 320)
        self.label_2.resize(221, 41)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 italic 20pt \"Times New Roman\";")
        self.label_2.setText("0,00 руб")

        self.pushButton = QPushButton(self)
        self.pushButton.move(150, 210)
        self.pushButton.resize(151, 41)
        self.pushButton.setText("История расходов")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"Times New Roman\";\n"
                                      "border-radius: 20px;\n"
                                      "border-style: outset;\n"
                                      "padding: 5px;\n"
                                      "QPushButton:hover")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.move(150, 260)
        self.pushButton_2.resize(151, 41)
        self.pushButton_2.setText("История доходов")
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"Times New Roman\";\n"
                                        "border-radius: 20px;\n"
                                        "border-style: outset;\n"
                                        "padding: 5px;\n"
                                        "QPushButton:hover")

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.move(150, 160)
        self.pushButton_3.resize(151, 41)
        self.pushButton_3.setText("Добавить в бюджет")
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"Times New Roman\";\n"
                                        "border-radius: 20px;\n"
                                        "border-style: outset;\n"
                                        "padding: 5px;\n"
                                        "QPushButton:hover\n"
                                        "")

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.move(150, 110)
        self.pushButton_4.resize(151, 41)
        self.pushButton_4.setText("Вычесть с бюджета")
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"Times New Roman\";\n"
                                        "border-radius: 20px;\n"
                                        "border-style: outset;\n"
                                        "padding: 5px;\n"
                                        "QPushButton:hover")

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setText("Конвентор")
        self.pushButton_5.move(150, 60)
        self.pushButton_5.resize(151, 41)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"Times New Roman\";\n"
                                        "border-radius: 20px;\n"
                                        "border-style: outset;\n"
                                        "padding: 5px;\n"
                                        "QPushButton:hover")

        # Соединения с методами
        self.pushButton_3.clicked.connect(self.open_income_form)
        self.pushButton_4.clicked.connect(self.open_expenses_form)
        self.pushButton_5.clicked.connect(self.open_convert_form)
        self.pushButton_2.clicked.connect(self.open_income_story_form)
        self.pushButton.clicked.connect(self.open_expenses_story_form)

    # Метод для открытия окна внесения дохода
    def open_income_form(self):
        self.income_form = IncomeForm()
        self.income_form.show()

    # Метод для открытия окна внесения вычета
    def open_expenses_form(self):
        self.expenses_form = ExpensesForm()
        self.expenses_form.show()

    # Метод для изменения баланса
    def change_balance(self):
        self.label_2.setText(str(count_balance_round) + ' руб')

    # Метод для открытия окна конвертирования
    def open_convert_form(self):
        self.convert_form = ConvertForm()
        self.convert_form.show()

    # Метод для открытия окна истории дохода
    def open_income_story_form(self):
        self.income_story_form = IncomeStoryForm()
        self.income_story_form.show()

    # Метод для открытия окна истории дохода
    def open_expenses_story_form(self):
        self.expenses_story_form = ExpensesStoryForm()
        self.expenses_story_form.show()


class IncomeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 402, 167)
        self.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.setWindowTitle('Добавить в бюджет')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Income_Window.png'))

        self.label = QLabel(self)
        self.label.move(10, 20)
        self.label.resize(151, 21)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 italic 16pt \"Calibri\";")
        self.label.setText("Введите сумму:")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(160, 20)
        self.lineEdit.resize(171, 21)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 italic 16pt \"Calibri\";")

        self.label_2 = QLabel(self)
        self.label_2.move(10, 50)
        self.label_2.resize(191, 21)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 italic 16pt \"Calibri\";")
        self.label_2.setText("Категория дохода:")

        self.comboBox = QComboBox(self)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.move(190, 50)
        self.comboBox.resize(141, 21)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setPlaceholderText("Зарплата")
        self.comboBox.addItem("Зарплата")
        self.comboBox.addItem("Подарок")
        self.comboBox.addItem("Победа на ставках")
        self.comboBox.addItem("Вернули долг")

        self.pushButton = QPushButton(self)
        self.pushButton.move(230, 130)
        self.pushButton.resize(75, 23)
        self.pushButton.setText("ОK")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.move(310, 130)
        self.pushButton_2.resize(75, 23)
        self.pushButton_2.setText("Отмена")
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_3 = QLabel(self)
        self.label_3.move(10, 130)
        self.label_3.resize(221, 21)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_3.setText("Введите сумму корректно")

        # Соединения с методами
        self.pushButton.clicked.connect(self.ok_close_form)
        self.pushButton_2.clicked.connect(self.cancel_close_form)

    def ok_close_form(self):
        global count_balance
        global count_balance_round
        global dt_now
        global value_id_income

        try:
            # Обьявление локальных переменных
            list_data_income = []
            data_all = []

            # Подключение и создание курсора
            con = sqlite3.connect("MyBD.sqlite")
            cur = con.cursor()

            value_id_income += 1
            count_balance += float(self.lineEdit.text())
            count_balance_round = round(count_balance, 2)
            ex.change_balance()

            # Обновление данных для ввода в таблицу БД
            data_all.append(value_id_income)
            data_all.append(float(self.lineEdit.text()))
            data_all.append(self.comboBox.currentText())
            data_all.append(dt_now)
            list_data_income.append(tuple(data_all))

            # Ввод изменений, выход из БД и окна
            cur.executemany("INSERT INTO Income_Story(id, Total, Category, Date) VALUES (?, ?, ?, ?)", list_data_income)
            con.commit()
            con.close()
            self.close()
        except ValueError:
            self.label_3.setStyleSheet("color: rgb(250, 0, 0)")
            self.label_3.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
            self.label_3.adjustSize()
            self.label_3.setText('Некорректная сумма')

    def cancel_close_form(self):
        self.close()


class ExpensesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 402, 165)
        self.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.setWindowTitle('Вычесть с бюджета')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Deduction_Window.png'))

        self.label = QLabel(self)
        self.label.move(10, 20)
        self.label.resize(151, 21)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 italic 16pt \"Calibri\";")
        self.label.setText("Введите сумму:")

        self.label_2 = QLabel(self)
        self.label_2.move(10, 50)
        self.label_2.resize(201, 21)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 italic 16pt \"Calibri\";")
        self.label_2.setText("Категория списания:")

        self.comboBox = QComboBox(self)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.move(210, 50)
        self.comboBox.resize(141, 21)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setPlaceholderText("Погашения кредита")
        self.comboBox.addItem("Оплата за проезд")
        self.comboBox.addItem("Покупка товара")
        self.comboBox.addItem("Оплата налогов")

        self.label_3 = QLabel(self)
        self.label_3.move(10, 130)
        self.label_3.resize(221, 21)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_3.setText("Введите сумму корректно")

        self.pushButton = QPushButton(self)
        self.pushButton.move(230, 130)
        self.pushButton.resize(75, 23)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("ОK")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.move(310, 130)
        self.pushButton_2.resize(75, 23)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Отмена")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(160, 20)
        self.lineEdit.resize(171, 21)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 italic 16pt \"Calibri\";")

        # Соединение с методами
        self.pushButton.clicked.connect(self.ok_close_form)
        self.pushButton_2.clicked.connect(self.cancel_close_form)

    def ok_close_form(self):
        global count_balance
        global count_balance_round
        global value_id_expenses

        try:
            # Обьявление локальных переменных
            data_all = []
            list_data_expenses = []

            # Подключение и создание курсора БД
            con = sqlite3.connect("MyBD.sqlite")
            cur = con.cursor()

            value_id_expenses += 1
            count_balance -= float(self.lineEdit.text())
            count_balance_round = round(count_balance, 2)
            ex.change_balance()

            # Обновление данных для ввода в таблицу БД
            data_all.append(value_id_expenses)
            data_all.append(float(self.lineEdit.text()))
            data_all.append(self.comboBox.currentText())
            data_all.append(dt_now)
            list_data_expenses.append(tuple(data_all))

            # Ввод изменений, выход из БД и окна
            cur.executemany("INSERT INTO Expenses_Story(id, Total, Category, Date) VALUES (?, ?, ?, ?)",
                            list_data_expenses)
            con.commit()
            con.close()
            self.close()
        except ValueError:
            self.label_3.setStyleSheet("color: rgb(250, 0, 0)")
            self.label_3.setFont(QtGui.QFont('Times', 14, QtGui.QFont.Bold))
            self.label_3.adjustSize()
            self.label_3.setText('Некорректная сумма')

    def cancel_close_form(self):
        self.close()


class ConvertForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.convert_balance = 0

        self.setGeometry(100, 100, 439, 173)
        self.setWindowTitle('Конвентор')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Convert_Window.jpg'))
        self.setStyleSheet("background-color: rgb(97, 97, 97);")

        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(181, 21)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 14pt \"Times New Roman\";")
        self.label.setText("Валюта для перевода")

        self.label_2 = QLabel(self)
        self.label_2.move(10, 70)
        self.label_2.resize(181, 16)
        self.label_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setText("Введите сумму")

        self.comboBox = QComboBox(self)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.move(10, 40)
        self.comboBox.resize(171, 21)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.addItem("Доллар")

        self.label_3 = QLabel(self)
        self.label_3.move(260, 40)
        self.label_3.resize(131, 16)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_3.setText("Результат (Руб)")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10, 100)
        self.lineEdit.resize(161, 21)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.move(260, 70)
        self.lineEdit_2.resize(161, 31)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setReadOnly(True)

        self.label_4 = QLabel(self)
        self.label_4.move(10, 140)
        self.label_4.resize(191, 21)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Times New Roman\";")
        self.label_4.setText("Введите сумму корректно")

        self.pushButton = QPushButton(self)
        self.pushButton.move(200, 70)
        self.pushButton.resize(31, 21)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("⥬")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.move(200, 130)
        self.pushButton_2.resize(111, 31)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Добавить в баланс")

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.move(320, 130)
        self.pushButton_3.resize(111, 31)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("Отмена")

        # Соединение с методами
        self.pushButton_2.clicked.connect(self.add_in_balance)
        self.pushButton_3.clicked.connect(self.cancel_close_form)
        self.pushButton.clicked.connect(self.convert_money)

    def cancel_close_form(self):
        self.close()

    def convert_money(self):
        global number_dollar

        if len(self.lineEdit.text()) != 0:
            try:
                self.convert_balance = round(float(self.lineEdit.text()) * number_dollar, 2)
                self.lineEdit_2.setText(str(self.convert_balance))
            except ValueError:
                self.label_4.setStyleSheet("color: rgb(250, 0, 0)")
                self.label_4.setFont(QtGui.QFont('Times', 12, QtGui.QFont.Bold))
                self.label_4.adjustSize()
                self.label_4.setText('Некорректная сумма')

    def add_in_balance(self):
        global count_balance
        global count_balance_round
        global data
        global value_id_income

        # Обьявление локальных переменных
        list_data_expenses = []
        data_all = []

        # Создание подключение и курсора БД
        con = sqlite3.connect("MyBD.sqlite")
        cur = con.cursor()

        # Изменение данных для ввода в таблицу БД
        value_id_income += 1
        count_balance += self.convert_balance
        count_balance_round = round(count_balance, 2)
        data_all.append(value_id_income)
        data_all.append(float(self.lineEdit_2.text()))
        data_all.append('Конвертация(Доллар)')
        data_all.append(dt_now)
        list_data_expenses.append(tuple(data_all))

        # Ввод изменений, выход из БД и окна
        cur.executemany("INSERT INTO Income_Story(id, Total, Category, Date) VALUES (?, ?, ?, ?)",
                        list_data_expenses)
        con.commit()
        con.close()
        self.close()
        ex.change_balance()


class IncomeStoryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('История доходов')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Story.png'))
        self.setGeometry(100, 100, 672, 354)
        self.setStyleSheet("background-color: rgb(97, 97, 97);")

        self.tableView = QTableView(self)
        self.tableView.move(10, 40)
        self.tableView.resize(651, 261)
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(170, 20)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 14pt \"Times New Roman\";")
        self.label.setText("Валюта для перевода")

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.move(540, 310)
        self.pushButton_3.resize(101, 31)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("Отмена")

        self.pushButton_3.clicked.connect(self.cancel_close_form)

        # Открытие БД
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('MyBD.sqlite')
        self.db.open()

        # Отображение таблицы в виджет
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('Income_Story')
        self.model.select()
        self.tableView.setModel(self.model)

    def cancel_close_form(self):
        self.close()


class ExpensesStoryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('История расходов')
        self.setWindowIcon(QIcon('Image_Icon/Icon_Story.png'))

        self.setGeometry(100, 100, 672, 354)
        self.setStyleSheet("background-color: rgb(97, 97, 97);")

        self.tableView = QTableView(self)
        self.tableView.move(10, 40)
        self.tableView.resize(651, 261)
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(170, 20)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 14pt \"Times New Roman\";")
        self.label.setText("Валюта для перевода")

        self.pushButton = QPushButton(self)
        self.pushButton.move(540, 310)
        self.pushButton.resize(101, 31)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("Отмена")
        self.pushButton.clicked.connect(self.cancel_close_form)

        # Открытие БД
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('MyBD.sqlite')
        self.db.open()

        # Отображение таблицы в виджет
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('Expenses_Story')
        self.model.select()
        self.tableView.setModel(self.model)

    def cancel_close_form(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())