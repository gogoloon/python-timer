from tkinter import ttk
from tkinter import *

from timer_main import TimerMain


class TimerView(ttk.LabelFrame):
    def __init__(self, master=None):

        __frame = ttk.LabelFrame(master, text="タイマー")
        __frame.pack(anchor="w", fill="x", expand=True, padx=30, pady=10)
        self.timer_main = TimerMain(__frame)

        __label = Label(__frame, text="タイマー入力")
        __label.grid(row=0, column=0)

        __label = Entry(__frame, justify="right", width="8", textvariable=self.timer_main.text_min)
        __label.grid(row=0, column=1)

        __label = Label(__frame, text="分")
        __label.grid(row=0, column=2)

        __label = Entry(__frame, justify="right", width="8", textvariable=self.timer_main.text_sec)
        __label.grid(row=0, column=3)

        __label = Label(__frame, text="秒")
        __label.grid(row=0, column=4)

        __label = Button(__frame, textvariable=self.timer_main.text_start_stop_button,
                         command=self.timer_main.click_timer_button)
        __label.grid(row=0, column=5)

        __label = Label(__frame, text="残時間")
        __label.grid(row=1, column=0)

        __label = Label(__frame, textvariable=self.timer_main.remain_min)
        __label.grid(row=1, column=1)

        __label = Label(__frame, text="分")
        __label.grid(row=1, column=2)

        __label = Label(__frame,  textvariable=self.timer_main.remain_sec)
        __label.grid(row=1, column=3)

        __label = Label(__frame, text="秒")
        __label.grid(row=1, column=4)

        __label = Label(__frame, text="推定終了時刻：")
        __label.grid(row=1, column=5)

        __label = Label(__frame, textvariable=self.timer_main.scheduled_finish_time)
        __label.grid(row=1, column=6)
