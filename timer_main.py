import tkinter as tk


class TimerMain():
    def __init__(self, timer_frame):

        self.__frame = timer_frame
        self.__start_status = True

        self.__text_min = tk.StringVar()
        self.__text_sec = tk.StringVar()
        self.__remain_min = tk.StringVar()
        self.__remain_sec = tk.StringVar()

        self.__text_min.set(str(60))
        self.__text_sec.set(str(0))
        self.__remain_min.set(str("-"))
        self.__remain_sec.set(str("-"))

        self.__text_start_stop_button = tk.StringVar()
        self.__text_start_stop_button.set("Start")

        self.__scheduled_finish_time = tk.StringVar()
        self.__scheduled_finish_time.set(str("-"))

    def click_timer_button(self):
        if self.__start_status:
            self.__start_status = False
            self.__text_start_stop_button.set("Stop")
            self.__remain_min.set(int(self.__text_min.get()))
            self.__remain_sec.set(int(self.__text_sec.get()))
            self.exec_timer()

        else:
            self.__start_status = True
            self.__text_start_stop_button.set("Start")
            self.__remain_sec.set(str("-"))
            self.__remain_min.set(str("-"))

    def exec_timer(self):

        if not self.__start_status:
            __tmp_time_min = int(self.__remain_min.get())
            __tmp_time_sec = int(self.__remain_sec.get())

            if __tmp_time_min >= 0:
                __tmp_time_sec -= 1
                self.__remain_sec.set(str(__tmp_time_sec))

            if __tmp_time_sec == -1:
                __tmp_time_min -= 1
                self.__remain_min.set(str(__tmp_time_min))
                self.__remain_sec.set("59")

            self.__frame.after(1000, self.exec_timer)

    @property
    def text_min(self):
        return self.__text_min

    @property
    def text_sec(self):
        return self.__text_sec

    @property
    def text_start_stop_button(self):
        return self.__text_start_stop_button

    @property
    def remain_min(self):
        return self.__remain_min

    @property
    def remain_sec(self):
        return self.__remain_sec

    @property
    def scheduled_finish_time(self):
        return self.__scheduled_finish_time
