import customtkinter


# Настройка внешнего вида и темы GUI-окна
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.width = 200
        self.height = 200

        self.protocol("WM_DELETE_WINDOW", self._on_closing)


    def _place(self):
        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (self.width / 2)
        y = (hs / 2) - (self.height / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

    @staticmethod
    def _on_closing():
        """Используется в протоколе окна, закрывает приложение при закрытии окна."""
        exit()