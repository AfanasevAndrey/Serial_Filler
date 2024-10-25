import tkinter as tk
from typing import Callable

from .settings_window import Window as StngsWin
class Menu(tk.Menu):
    """
    Класс отвечает за меню окна
    """
    def __init__(self, exit_command: Callable,):
        tk.Menu.__init__(self)
        self.add_cascade(label="Настройки", command=self.settings_win)
        self.add_cascade(label="Помощь")
        self.add_cascade(label="Выход", command=exit_command)

    def settings_win(self):
        """
        Открытие окна настроек
        """
        stngs = tk.Tk()
        stngs.title('Settings') #заголовок
        stngs.geometry("300x400")
        stngs.resizable(False, False)
        settings_frame = StngsWin(stngs)