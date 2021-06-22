from tkinter import ttk
from tkinter import *

from timer_main import TimerMain


class TimerView(ttk.LabelFrame):
    def __init__(self, master=None):
        self.timer_main = TimerMain()
        __frame = ttk.LabelFrame(master, text="タイマー")
        __frame.pack(anchor="w", fill="x", expand=True, padx=30, pady=10)

        __label = Label(__frame, text="タイマー入力")
        __label.grid(row=0, column=0)

        __label = Entry(__frame, justify="right", width="8", textvariable="")
        __label.grid(row=0, column=1)

        __label = Label(__frame, text="分")
        __label.grid(row=0, column=2)

        __label = Entry(__frame, justify="right", width="8", textvariable="")
        __label.grid(row=0, column=3)

        __label = Label(__frame, text="秒")
        __label.grid(row=0, column=4)

        __label = Button(__frame, text="Start",
                         command=self.timer_main.click_timer_button)
        __label.grid(row=0, column=5)

        __label = Label(__frame, text="残時間")
        __label.grid(row=1, column=0)

        __label = Label(__frame, text="<残りの分>")
        __label.grid(row=1, column=1)

        __label = Label(__frame, text="分")
        __label.grid(row=1, column=2)

        __label = Label(__frame, text="<残りの秒>")
        __label.grid(row=1, column=3)

        __label = Label(__frame, text="秒")
        __label.grid(row=1, column=4)

        __label = Label(__frame, text="推定終了時刻：")
        __label.grid(row=1, column=5)

        __label = Label(__frame, text="<推定終了時刻が入る>")
        __label.grid(row=1, column=6)
