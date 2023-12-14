from customtkinter import CTk, CTkRadioButton, IntVar, CTkLabel, CTkEntry, CTkButton, CTkTextbox, CTkInputDialog
import sqlite3

con = sqlite3.connect("libdb.db")
cursor = con.cursor()


class FindBook(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x350")
        self.title("Найти книгу")

        self.label1 = CTkLabel(self, text="Поиск книги по кретериям:")
        self.label1.place(x=10, y=10)

        self.radio_var = IntVar()
        self.radio1 = CTkRadioButton(self, text="Название", variable=self.radio_var, value=1)
        self.radio1.place(x=10, y=40)
        self.entry1 = CTkEntry(self, placeholder_text="Название")
        self.entry1.place(x=200, y=40)
        self.radio2 = CTkRadioButton(self, text="Автор", variable=self.radio_var, value=2)
        self.radio2.place(x=10, y=70)
        self.entry2 = CTkEntry(self, placeholder_text="Автор")
        self.entry2.place(x=200, y=70)
        self.radio3 = CTkRadioButton(self, text="Жанр", variable=self.radio_var, value=3)
        self.radio3.place(x=10, y=100)
        self.entry3 = CTkEntry(self, placeholder_text="Жанр")
        self.entry3.place(x=200, y=100)
        self.radio4 = CTkRadioButton(self, text="Количество страниц", variable=self.radio_var, value=4)
        self.radio4.place(x=10, y=130)
        self.entry4 = CTkEntry(self, placeholder_text="Количество страниц")
        self.entry4.place(x=200, y=130)
        self.radio5 = CTkRadioButton(self, text="Год издания", variable=self.radio_var, value=5)
        self.radio5.place(x=10, y=160)
        self.entry5 = CTkEntry(self, placeholder_text="Год издания")
        self.entry5.place(x=200, y=160)

        self.button1 = CTkButton(self, text="Найти", command=self.find_book)
        self.button1.place(x=10, y=200)

        self.button2 = CTkButton(self, text="Выдать", command=self.out_book)
        self.button2.place(x=230, y=200)

        self.button3 = CTkButton(self, text="Получить", command=self.in_book)
        self.button3.place(x=450, y=200)

        self.label = CTkLabel(self, text="Информация:", corner_radius=5)
        self.label.place(x=5, y=230)
        self.textbox1 = CTkTextbox(master=self, width=800, height=100, corner_radius=0)
        self.textbox1.place(x=5, y=250)
        self.textbox1.delete(1.0, 'end')

    def out_book(self):
        dialog = CTkInputDialog(text="Введите название книги:", title="Выдача книги")
        name = dialog.get_input()
        try:
            cursor.execute("SELECT * FROM book WHERE name=?", (name,))
            result = cursor.fetchone()
            new_quantity = result[6] - 1
            query = f"UPDATE book SET quantity = ? WHERE name = ?"
            cursor.execute(query, (new_quantity, name))
            con.commit()
            self.textbox1.delete(1.0, 'end')
            cursor.execute("SELECT * FROM book WHERE name=?", (name,))
            result = cursor.fetchone()
            text = f"Книга с названием '{result[1]}' выдана, остаток {result[6]} шт."
            self.textbox1.insert("0.0", text=text)
        except TypeError:
            self.textbox1.delete(1.0, 'end')
            self.textbox1.insert("0.0", text="Такой книги нет")

    def in_book(self):
        dialog = CTkInputDialog(text="Введите название книги:", title="Получение книги")
        name = dialog.get_input()
        try:
            cursor.execute("SELECT * FROM book WHERE name=?", (name,))
            result = cursor.fetchone()
            new_quantity = result[6] + 1
            query = f"UPDATE book SET quantity = ? WHERE name = ?"
            cursor.execute(query, (new_quantity, name))
            con.commit()
            self.textbox1.delete(1.0, 'end')
            cursor.execute("SELECT * FROM book WHERE name=?", (name,))
            result = cursor.fetchone()
            text = f"Книга с названием '{result[1]}' получена, остаток {result[6]} шт."
            self.textbox1.insert("0.0", text=text)
        except TypeError:
            self.textbox1.delete(1.0, 'end')
            self.textbox1.insert("0.0", text="Такой книги нет")

    def clear_entry(self):
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")

    def find_book(self):
        if self.radio_var.get() == 1:
            name = self.entry1.get()
            cursor.execute("SELECT * FROM book WHERE name=?", (name,))
            self.results = cursor.fetchall()
            self.clear_entry()
        elif self.radio_var.get() == 2:
            author = self.entry2.get()
            cursor.execute("SELECT * FROM book WHERE author=?", (author,))
            self.results = cursor.fetchall()
            self.clear_entry()
        elif self.radio_var.get() == 3:
            genre = self.entry3.get()
            cursor.execute("SELECT * FROM book WHERE genre=?", (genre,))
            self.results = cursor.fetchall()
            self.clear_entry()
        elif self.radio_var.get() == 4:
            pages = self.entry4.get()
            cursor.execute("SELECT * FROM book WHERE pages=?", (pages,))
            self.results = cursor.fetchall()
            self.clear_entry()
        elif self.radio_var.get() == 5:
            year = self.entry5.get()
            cursor.execute("SELECT * FROM book WHERE year=?", (year,))
            self.results = cursor.fetchall()
            self.clear_entry()

        self.textbox1.delete(1.0, 'end')
        self.text = "Найденные книги: \n"
        if self.results == []:
            self.text += "Ничего не найдено"
        else:
            for item in self.results:
                self.text += f"Название: {item[1]}, Автор: {item[2]}, Жанр: {item[3]}, Страниц: {item[4]}, Год: {item[5]}, Количество: {item[6]} \n"
        self.textbox1.insert("0.0", text=self.text)
