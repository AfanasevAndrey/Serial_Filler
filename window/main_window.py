import tkinter as tk

from .menu import Menu

class Window(tk.Frame):
    """
    Основной класс графиического интерфейса, отвечает за все элементы интерфейса
    """
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self, master)
        self.init_menu()
        self.init_window()
        
    def init_window(self):
        self.pack(fill=tk.BOTH, expand=1)

        quit_button = tk.Button(self, text="Exit", command=self.master.destroy)
        start_button = tk.Button(self, text="Browse", command=self.on_click)

        self.label = tk.Label(self, text="Hello")

        quit_button.grid(row=0, column=0)
        start_button.grid(row=0, column=1)

        self.label.grid(row=1, column=0, columnspan=2)
    
    def init_menu(self):
        main_menu = Menu(exit_command=self.master.destroy)
        
 
        self.master.config(menu=main_menu)

    def on_click(self):
        self.label['text'] = "Starting..."

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()