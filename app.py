import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QInputDialog
import main
import keyboard


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        with open('radios.txt', encoding='utf-8') as f:
            self.radios = [x.strip().split('*') for x in f]
        for m in self.radios:
            listWidgetItem = QListWidgetItem(m[0])
            self.radio_list.addItem(listWidgetItem)
        with open('books.txt', encoding='utf-8') as f:
            self.books = [x.strip() for x in f]
        for m in self.books:
            listWidgetItem = QListWidgetItem(m)
            self.books_list.addItem(listWidgetItem)
        with open('friends.txt', encoding='utf-8') as f:
            self.friends = [x.strip().split() for x in f]
        for m in self.friends:
            listWidgetItem = QListWidgetItem(m[0])
            self.friend_list.addItem(listWidgetItem)

        self.add_book_but.clicked.connect(self.add_book)
        self.add_radio_but.clicked.connect(self.add_radio)
        self.add_friend_but.clicked.connect(self.add_friend)
        self.start_app_but.clicked.connect(self.start_app)
        keyboard.add_hotkey("ctrl+f", self.start_app)

    def add_book(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите название книги", 
                                                "Добавить книгу")
        if ok_pressed:
            with open('books.txt', 'a', encoding='utf-8') as f:
                f.write('\n')
                f.write(name)
        self.books_list.clear()
        with open('books.txt', encoding='utf-8') as f:
            self.books = [x.strip() for x in f]
        for m in self.books:
            listWidgetItem = QListWidgetItem(m)
            self.books_list.addItem(listWidgetItem)

    def add_radio(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите название", 
                                                "Добавить название")
        if ok_pressed:
            adress, ok_pressed_1 = QInputDialog.getText(self, "Введите адрес", 
                                        "Добавить радио")
            if ok_pressed_1:
                with open('radios.txt', 'a', encoding='utf-8') as f:
                    f.write('\n')
                    f.write(f'{name}*{adress}')
        self.radio_list.clear()
        with open('radios.txt', encoding='utf-8') as f:
            self.radios = [x.strip().split('*') for x in f]
        for m in self.radios:
            listWidgetItem = QListWidgetItem(m[0])
            self.radio_list.addItem(listWidgetItem)

    def add_friend(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя друга", 
                                                "Добавить друга")
        if ok_pressed:
            id, ok_pressed_1 = QInputDialog.getText(self, "Введите его id", 
                                        "Добавить id")
            if ok_pressed_1:
                with open('friends.txt', 'a', encoding='utf-8') as f:
                    f.write('\n')
                    f.write(f'{name} {id}')
        self.friend_list.clear()
        with open('friends.txt', encoding='utf-8') as f:
            self.friends = [x.strip().split() for x in f]
        for m in self.friends:
            listWidgetItem = QListWidgetItem(m[0])
            self.friend_list.addItem(listWidgetItem)

    def start_app(self):
        main.provodnik()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())