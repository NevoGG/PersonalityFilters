import sys
import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
import enum

from ZeroShot import Filters


VULGAR = "assets/vulgar.png"
MASCULINE = "assets/masculine.png"
FEMININE = "assets/feminine.png"
COOL = "assets/cool.png"
LOGO = "assets/logo_small.png"
EXIT = "assets/exit_small.png"
SUBMIT = "assets/submit_small.png"

VULGAR_P = "assets/vulgar_p.png"
MASCULINE_P = "assets/masculine_p.png"
FEMININE_P = "assets/feminine_p.png"
COOL_P = "assets/cool_p.png"

START_X = 400
START_Y = 200
Y_DIFF = 30
X_DIFF = 150
THRESHOLD = 7
NONE_NUM = 0
MASCULINE_NUM = 1
FEMININE_NUM = 2
COOL_NUM = 3
VULGAR_NUM = 4
FONT = "gisha"
SIZE = 20


class Form:
    # UI objects:
    window = Tk()
    zero_shot = Filters()
    vulgar = PhotoImage(file=VULGAR)
    masculine = PhotoImage(file=MASCULINE)
    feminine = PhotoImage(file=FEMININE)
    cool = PhotoImage(file=COOL)
    vulgar_p = PhotoImage(file=VULGAR_P)
    masculine_p = PhotoImage(file=MASCULINE_P)
    feminine_p = PhotoImage(file=FEMININE_P)
    cool_p = PhotoImage(file=COOL_P)
    logo = PhotoImage(file=LOGO)
    exit = PhotoImage(file=EXIT)
    submit = PhotoImage(file=SUBMIT)

    # variables:
    intensity_var = IntVar()
    prompt_var = StringVar()
    filter = NONE_NUM
    prev_filter = NONE_NUM

    # interactive:
    prompt_entry = Entry(window, bg="White", width=38)
    feminine_btn = tk.Button(window, width=80, height=80, image=feminine)
    masculine_btn = tk.Button(window, width=80, height=80,  image=masculine)
    cool_btn = tk.Button(window, width=80, height=80, image=cool)
    vulgar_btn = tk.Button(window, width=80, height=80, image=vulgar)
    submit_btn = tk.Button(window,  image=submit, bg="white", border=0)
    exit_btn = tk.Button(window,  image=exit, bg="white", border=0)

    # labels:
    logo_label = tk.Label(window, image=logo, bg="white", border=0, height=250, width=500)
    prompt_label = tk.Label(window, text="Enter Text Here:", background="white")
    answer_label = tk.Label(window, width=100, background="white")

    # configs:
    prompt_label.config(font=(FONT, SIZE))
    prompt_entry.config(font=(FONT, SIZE))
    answer_label.config(font=(FONT, SIZE))
    exit_btn.config(font=(FONT, SIZE), bg="white")
    submit_btn.config(font=(FONT, SIZE), bg="white")
    # answer_label.config(, width=200, height=80)
    masculine_btn["background"] = "white"
    masculine_btn["border"] = "0"
    feminine_btn["background"] = "white"
    feminine_btn["border"] = "0"
    cool_btn["background"] = "white"
    cool_btn["border"] = "0"
    vulgar_btn["background"] = "white"
    vulgar_btn["border"] = "0"

    def init_objects(self):
        self.window.title("Filters")
        self.window.attributes("-fullscreen", True)
        self.window.geometry("1000x1000")
        self.window.configure(background="white")

        self.feminine_btn.config(command=self.feminine_func)
        self.masculine_btn.config(command=self.masculine_func)
        self.cool_btn.config(command=self.cool_func)
        self.vulgar_btn.config(command=self.vulgar_func)
        self.submit_btn.config(command=self.apply_filter)
        self.exit_btn.config(command=sys.exit)

        # set interactive objects location:
        self.logo_label.place(x=START_X + X_DIFF * 0.5, y=START_Y - 5 * Y_DIFF)
        self.prompt_entry.place(x=START_X, y=START_Y + Y_DIFF * 5)
        self.submit_btn.place(x=START_X + X_DIFF * 4, y=START_Y + Y_DIFF * 4.7)
        self.feminine_btn.place(x=START_X, y=START_Y + Y_DIFF * 8)
        self.masculine_btn.place(x=START_X + X_DIFF, y=START_Y + Y_DIFF * 8)
        self.cool_btn.place(x=START_X + X_DIFF * 2, y=START_Y + Y_DIFF * 8)
        self.vulgar_btn.place(x=START_X + X_DIFF * 3, y=START_Y + Y_DIFF * 8)
        self.exit_btn.place(x=START_X + X_DIFF * 4, y=START_Y + Y_DIFF * 8.3)
        self.answer_label.place(x=START_X - X_DIFF * 3, y=START_Y + Y_DIFF * 14)


    def init(self):
        self.init_objects()
        self.window.mainloop()

    def apply_filter(self):
        after_filter = self.zero_shot.apply_filter(self.prompt_entry.get(), self.filter)
        self.answer_label.config(text=after_filter)

    def push_button(self):
        if self.filter == FEMININE_NUM:
            self.feminine_btn.configure(image=self.feminine_p)
        if self.filter == MASCULINE_NUM:
            self.masculine_btn.configure(image=self.masculine_p)
        if self.filter == COOL_NUM:
            self.cool_btn.configure(image=self.cool_p)
        if self.filter == VULGAR_NUM:
            self.vulgar_btn.configure(image=self.vulgar_p)
        if self.prev_filter == FEMININE_NUM:
            self.feminine_btn.configure(image=self.feminine)
        if self.prev_filter == MASCULINE_NUM:
            self.masculine_btn.configure(image=self.masculine)
        if self.prev_filter == COOL_NUM:
            self.cool_btn.configure(image=self.cool)
        if self.prev_filter == VULGAR_NUM:
            self.vulgar_btn.configure(image=self.vulgar)

    def feminine_func(self):
        self.prev_filter = self.filter
        self.filter = FEMININE_NUM
        self.push_button()

    def masculine_func(self):
        self.prev_filter = self.filter
        self.filter = MASCULINE_NUM
        self.push_button()

    def cool_func(self):
        self.prev_filter = self.filter
        self.filter = COOL_NUM
        self.push_button()

    def vulgar_func(self):
        self.prev_filter = self.filter
        self.filter = VULGAR_NUM
        self.push_button()







