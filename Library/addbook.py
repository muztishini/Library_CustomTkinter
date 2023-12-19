import customtkinter
import sqlite3

con = sqlite3.connect("libdb.db")
cursor = con.cursor()


class AddBook:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_window = customtkinter.CTk()
        self.new_window.geometry("400x350")
        self.new_window.title("Добавить книгу")

        self.label1 = customtkinter.CTkLabel(self.new_window, text="Введите данные книги:")
        self.label1.place(x=10, y=10)

        self.label2 = customtkinter.CTkLabel(self.new_window, text="Название:")
        self.label2.place(x=10, y=50)
        self.entry1 = customtkinter.CTkEntry(self.new_window, placeholder_text="Название")
        self.entry1.place(x=150, y=50)

        self.label3 = customtkinter.CTkLabel(self.new_window, text="Автор:")
        self.label3.place(x=10, y=80)
        self.entry2 = customtkinter.CTkEntry(self.new_window, placeholder_text="Автор")
        self.entry2.place(x=150, y=80)

        self.label4 = customtkinter.CTkLabel(self.new_window, text="Жанр:")
        self.label4.place(x=10, y=110)
        self.entry3 = customtkinter.CTkEntry(self.new_window, placeholder_text="Жанр")
        self.entry3.place(x=150, y=110)

        self.label5 = customtkinter.CTkLabel(self.new_window, text="Количество страниц:")
        self.label5.place(x=10, y=140)
        self.entry4 = customtkinter.CTkEntry(self.new_window, placeholder_text="Количество страниц")
        self.entry4.place(x=150, y=140)

        self.label6 = customtkinter.CTkLabel(self.new_window, text="Год издания:")
        self.label6.place(x=10, y=170)
        self.entry5 = customtkinter.CTkEntry(self.new_window, placeholder_text="Год издания")
        self.entry5.place(x=150, y=170)

        self.label7 = customtkinter.CTkLabel(self.new_window, text="Количество книг:")
        self.label7.place(x=10, y=200)
        self.entry6 = customtkinter.CTkEntry(self.new_window, placeholder_text="Количество книг")
        self.entry6.place(x=150, y=200)

        self.textbox = customtkinter.CTkTextbox(master=self.new_window, width=400, height=50)
        self.textbox.place(x=10, y=235)

        self.button = customtkinter.CTkButton(self.new_window, text="Добавить", command=self.add_book)
        self.button.place(x=120, y=300)

        self.new_window.mainloop()

    def add_book(self):
        name = self.entry1.get()
        author = self.entry2.get()
        genre = self.entry3.get()
        pages = self.entry4.get()
        year = self.entry5.get()
        quantity = self.entry6.get()

        # Проверяем, что введены только целые числа
        if not pages.isdigit() or not year.isdigit() or not quantity.isdigit():
            self.textbox.delete(1.0, 'end')
            self.textbox.insert("0.0",
                                text="Пожалуйста, введите целые числа для полей количества страниц, года издания и "
                                     "количества книг")
            return

        book = (name, author, genre, pages, year, quantity)
        cursor.execute("INSERT INTO book (name, author, genre, pages, year, quantity) VALUES (?, ?, ?, ?, ?, ?)", book)
        con.commit()
        self.textbox.delete(1.0, 'end')
        self.textbox.insert("0.0", text="Книга добавлена успешно")
