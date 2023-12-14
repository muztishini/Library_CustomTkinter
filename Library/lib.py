import customtkinter
import sqlite3
from addbook import AddBook
from findbook import FindBook

con = sqlite3.connect("libdb.db")
cursor = con.cursor()


class Lib(customtkinter.CTk):
    def __init__(self, login, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Библиотека")
        self.geometry("800x800")

        self.login = login

        self.title1 = customtkinter.CTkLabel(self, text=f"Добро пожаловать в нашу бибилиотеку {self.login}!",
                                             corner_radius=5)
        self.title1.place(x=250, y=10)

        self.button1 = customtkinter.CTkButton(self, text="Добавить книгу", command=self.add_book)
        self.button1.place(x=300, y=50)

        self.button2 = customtkinter.CTkButton(self, text="Посмотреть список книг", command=self.show_books)
        self.button2.place(x=300, y=100)

        self.button3 = customtkinter.CTkButton(self, text="Найти книгу", command=self.find_book)
        self.button3.place(x=300, y=150)

        self.title = customtkinter.CTkLabel(self, text="Список книг в библиотеке:", corner_radius=5)
        self.title.place(x=5, y=170)
        self.textbox2 = customtkinter.CTkTextbox(master=self, width=800, height=600, corner_radius=0)
        self.textbox2.place(x=5, y=200)

    def add_book(self):
        AddBook()

    def find_book(self):
        FindBook()

    def show_books(self):
        cursor.execute("SELECT * FROM book")
        books = cursor.fetchall()
        self.textbox2.delete(1.0, 'end')
        for item in books:
            text = f"Название: {item[1]}, Автор: {item[2]}, Жанр: {item[3]}, Страниц: {item[4]}, Год: {item[5]}, Количество: {item[6]} \n"
            self.textbox2.insert("0.0", text=text)
