import customtkinter
from lib import Lib


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Главная")
        self.geometry("400x220")

        self.title1 = customtkinter.CTkLabel(
            self, text="Добро пожаловать в нашу бибилиотеку", corner_radius=5)
        self.title1.place(x=70, y=10)
        self.title4 = customtkinter.CTkLabel(
            self, text="Для дальнейших действий авторизуйтесь", corner_radius=5)
        self.title4.place(x=70, y=40)
        self.title2 = customtkinter.CTkLabel(
            self, text="Введите логин и пароль", corner_radius=6)
        self.title2.place(x=110, y=70)

        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Login")
        self.entry1.place(x=30, y=110)
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Password")
        self.entry2.place(x=200, y=110)

        self.button = customtkinter.CTkButton(
            self, text="LogIn", command=self.button_callback)
        self.button.place(x=110, y=150)

        self.title3 = customtkinter.CTkLabel(self, text="")
        self.title3.place(x=100, y=190)

    def button_callback(self):
        logtrue = "admin"
        passtrue = "1234"
        login = self.entry1.get()
        password = self.entry2.get()

        if login == logtrue and password == passtrue:
            Lib(login)
        else:
            text = "Неверный логин или пароль"
            self.title3.configure(text=text)


app = App()
app.mainloop()
