import sys
from typing import Optional
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase
from design import Ui_MainWindow
from secwin import Equations
from operator import add, sub, mul, truediv

operations = {
    '+': add,
    '-': sub,
    '×': mul,
    '/': truediv,
}  # словарь функций
error_zero_div = 'На ноль делить нельзя'  # ошибки
error_undefined = 'Результат не определен'

default_font_size = 16  # обычные размеры шрифта
default_entry_font_size = 40  # обычные размеры шрифта для поля ввода


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #инициализация дизайна
        self.entry_max_len = self.ui.lineEdit.maxLength()
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.buttn_0.clicked.connect(self.add_digit)
        self.ui.buttn_1.clicked.connect(self.add_digit)
        self.ui.buttn_2.clicked.connect(self.add_digit)
        self.ui.buttn_3.clicked.connect(self.add_digit)
        self.ui.buttn_4.clicked.connect(self.add_digit)
        self.ui.buttn_5.clicked.connect(self.add_digit)
        self.ui.buttn_6.clicked.connect(self.add_digit)
        self.ui.buttn_7.clicked.connect(self.add_digit)
        self.ui.buttn_8.clicked.connect(self.add_digit)
        self.ui.buttn_9.clicked.connect(self.add_digit)

        self.ui.buttn_opwin.clicked.connect(self.show_secwin)
        self.ui.buttn_delal.clicked.connect(self.clear_all)
        self.ui.buttn_delwr.clicked.connect(self.clear_entry)
        self.ui.buttn_comm.clicked.connect(self.add_point)

        self.ui.buttn_calc.clicked.connect(self.calculate)
        self.ui.buttn_plus.clicked.connect(self.math_operation)
        self.ui.buttn_min.clicked.connect(self.math_operation)
        self.ui.buttn_mult.clicked.connect(self.math_operation)
        self.ui.buttn_div.clicked.connect(self.math_operation)
        self.ui.buttn_negat.clicked.connect(self.negate)
        self.ui.buttn_back.clicked.connect(self.backspace)

    def show_secwin(self):  # показ второго окна
        self.w2 = Equations()
        self.w2.show()

    def add_digit(self):  # добавление цифр
        self.remove_error()
        self.clear_temp_if_equality()
        buttn = self.sender()  # сигнал, передача нажатой кнопки

        digit_buttons = ('buttn_0', 'buttn_1', 'buttn_2', 'buttn_3', 'buttn_4',
                         'buttn_5', 'buttn_6', 'buttn_7', 'buttn_8', 'buttn_9')  # массив цифр
        if buttn.objectName() in digit_buttons:  # если имя сигнала есть в массиве заменяем или добавляем цифру
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(buttn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + buttn.text())
            self.adjust_entry_font_size()

    def clear_all(self) -> None:  # отчистка всех полей
        self.remove_error()
        self.ui.lineEdit.setText('0')
        self.adjust_entry_font_size()
        self.ui.label.clear()
        self.adjust_entry_font_size()

    def clear_entry(self) -> None:  # отчистка поля ввода
        self.remove_error()
        self.clear_temp_if_equality()
        self.ui.lineEdit.setText('0')
        self.adjust_entry_font_size()

    def add_point(self) -> None:  # добавление точки
        self.clear_temp_if_equality()
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')
            self.adjust_entry_font_size()

    def add_temp(self) -> None:
        buttn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.lineEdit.text())

        if not self.ui.label.text() or self.get_math_sign() == '=':  # проверка есть ли текст в поле или есть ли равенство
            self.ui.label.setText(entry + f' {buttn.text()} ')  # число/аргумент + знак
            self.ui.lineEdit.setText('0')  # отчистка поля
            self.adjust_entry_font_size()

    def negate(self) -> None:
        self.clear_temp_if_equality()
        entry = self.ui.lineEdit.text()
        if '-' not in entry:  # если отрицария нет - добавляем
            if entry != '0':
                entry = '-' + entry
        else:  # инчае убираем левый символ, т.е отрицание
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:  # увеличиваем макс длинну для отрицания по необходимости
            self.ui.lineEdit.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.lineEdit.setMaxLength(self.entry_max_len)

        self.ui.lineEdit.setText(entry)
        self.adjust_entry_font_size()

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.ui.lineEdit.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText(entry[:-1])  # вывод всех элементов до последней цифры, т.е. исключая её
        else:
            self.ui.lineEdit.setText('0')
        self.adjust_entry_font_size()

    def clear_temp_if_equality(self) -> None:  # отчистка врем. выр. после равенства
        if self.get_math_sign() == '=':
            self.ui.label.clear()
            self.adjust_entry_font_size()

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def get_entry_num(self) -> int | float:  # получ числа из поля ввода
        entry = self.ui.lineEdit.text().strip('.')  # созд перем и обрезание точки
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> int | float:
        if self.ui.label.text():
            temp = self.ui.label.text().strip('.').split()[0]  # обрез точки, делим по пробелам и берём первый элемент
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:  # возврат либо строки, либо ничего
        if self.ui.label.text():  # есть ли текст
            return self.ui.label.text().strip('.').split()[-1]  # обрез точки, делим по пробелам и вытащить последний элемент

    def calculate(self) -> Optional[str]:
        entry = self.ui.lineEdit.text()
        temp = self.ui.label.text()

        if temp:  # если в label есть текст
            try:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](self.get_temp_num(),
                                                         self.get_entry_num())))  # обрезание нулей, привод к строке, взятие операции из словаря по знаку, указание с какими числами провести операцию 1-врем выр, 2- поле ввода
                self.ui.label.setText(temp + self.remove_trailing_zeros(
                    entry) + ' =')  # добавление в label число из поля ввода и знак равно
                self.ui.lineEdit.setText(result)  # ставим результат в поле ввода
                self.adjust_entry_font_size()
                return result  # возвращаем результат
            except KeyError:  # при ошибке ввода ничего не делать
                pass
            except ZeroDivisionError:
                if self.get_temp_num() == 0:  # число равно 0, т.е. выр 0/0
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)

    def math_operation(self) -> None:
        temp = self.ui.label.text()
        buttn = self.sender()

        try:
            if not temp:  # добавляем выражение в label если его нет
                self.add_temp()
            else:
                if self.get_math_sign() != buttn.text():  # если не равен знаку агрумента-метода
                    if self.get_math_sign() == '=':
                        self.add_temp()  # вывод в label
                    else:
                        self.ui.label.setText(
                            temp[:-2] + f'{buttn.text()} ')  # иначе меняем знак выражения на знак нажатой кнопки
                else:
                    self.ui.label.setText(
                        self.calculate() + f' {buttn.text()}')  # считаем выражение и добавяем в конец знак
        except TypeError:
            pass
        self.adjust_temp_font_size()

    def show_error(self, text: str) -> None:
        self.ui.lineEdit.setMaxLength(len(text))  # установление макс. длинны поля размеру ошибки
        self.ui.lineEdit.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:  # удаление ошибки
        if self.ui.lineEdit.text() in (error_undefined, error_zero_div):
            self.ui.lineEdit.setMaxLength(self.entry_max_len)
            self.ui.lineEdit.setText('0')
            self.adjust_entry_font_size()
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:  # деактивация кнопок при подаче True и активация при False
        self.ui.buttn_calc.setDisabled(disable)
        self.ui.buttn_plus.setDisabled(disable)
        self.ui.buttn_min.setDisabled(disable)
        self.ui.buttn_mult.setDisabled(disable)
        self.ui.buttn_div.setDisabled(disable)
        self.ui.buttn_negat.setDisabled(disable)
        self.ui.buttn_comm.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:  # передача цвета переднего плана
        self.ui.buttn_calc.setStyleSheet(css_color)
        self.ui.buttn_plus.setStyleSheet(css_color)
        self.ui.buttn_min.setStyleSheet(css_color)
        self.ui.buttn_mult.setStyleSheet(css_color)
        self.ui.buttn_div.setStyleSheet(css_color)
        self.ui.buttn_negat.setStyleSheet(css_color)
        self.ui.buttn_comm.setStyleSheet(css_color)

    def get_entry_text_width(self) -> int: #возвращает длинну ограничивающего текст прямоугольника
        return self.ui.lineEdit.fontMetrics().boundingRect(
            self.ui.lineEdit.text()).width()

    def get_temp_text_width(self) -> int:
        return self.ui.label.fontMetrics().boundingRect(
            self.ui.label.text()).width()

    def adjust_entry_font_size(self) -> None:
        font_size = default_entry_font_size

        while self.get_entry_text_width() > self.ui.lineEdit.width() - 15: #пока ширина текста больше ширины поля, уменьшаем шрифт
            font_size -= 1

            self.ui.lineEdit.setStyleSheet('font-size: ' + str(font_size) + 'pt;')
        font_size = 1
        while self.get_entry_text_width() < self.ui.lineEdit.width() - 60:
            font_size += 1

            if font_size > default_entry_font_size:
                break

            self.ui.lineEdit.setStyleSheet(
                'font-size: ' + str(font_size) + 'pt;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.ui.label.width() - 10:
            font_size -= 1
            self.ui.label.setStyleSheet(
                'font-size: ' + str(font_size) + 'pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.ui.label.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break

            self.ui.label.setStyleSheet(
                'font-size: ' + str(font_size) + 'pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
