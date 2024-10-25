from tkinter import *

from window.main_window import Window

if __name__ == "__main__":
    root = Tk()
    root.title('Serial Filler') #заголовок
    root.geometry("800x600")
    root.resizable(False, False)
    app = Window(root)
    #lbl1.grid(column=0, row=0)

    root.mainloop() #отображение окна
    