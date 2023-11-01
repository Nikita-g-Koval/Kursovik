import os
import json
from random import random
from tkinter import *
from tkinter import messagebox


main_window = Tk()
main_window.title("Авторизация")
main_window.geometry('450x230')
main_window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
lable_font = ('Arial',  11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked():
    username_entry.get()

main_label = Label(main_window, text='Авторизация', font = font_header, justify=CENTER, **header_padding)
main_label.pack()

username_entry = Entry(main_window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

send_btn = Button(main_window, text='Перейти к тесту', command=clicked())
send_btn.pack(**base_padding)

main_window.mainloop()











