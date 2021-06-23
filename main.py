import tkinter

from timer_view import TimerView


class Main:
    def __init__(self):
        root = tkinter.Tk()
        root.title("Timer")
        TimerView(master=root)
        root.mainloop()


if __name__ == "__main__":
    Main()
