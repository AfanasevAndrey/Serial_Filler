import tkinter as tk
import json

class Window(tk.Frame):
    """
    Класс окна настроек
    """
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self, master)
        self.config = self.load_config()
        self.init_window()
    
    def init_window(self):
        self.pack(fill=tk.BOTH, expand=1)

        server_ip_lbl = tk.Label(self, text="Server IP:")
        self.server_ip_box = tk.Text(self, height=1, width=20)
        self.server_ip_box.insert(tk.END, self.config.get("server_ip", ''))
        
        prog_ip_lbl = tk.Label(self, text="ProgMB IP:")
        self.prog_ip_box = tk.Text(self, height=1, width=20)
        self.prog_ip_box.insert(tk.END, self.config.get("prog_ip", ''))

        server_ip_lbl.grid(row=0, column=0, columnspan=2)
        self.server_ip_box.grid(row=0, column=5, columnspan=2)

        prog_ip_lbl.grid(row=1, column=0, columnspan=2)
        self.prog_ip_box.grid(row=1, column=5, columnspan=2)

        save_btn = tk.Button(self, text="Save", command=self.save_config)
        save_btn.grid(row=2, column=3, columnspan=2)

    def load_config(self) -> dict:
        with open("e:/scripts/serial_filler/config.json", 'r') as fh:
            return json.load(fh)

    def save_config(self) -> None:
        self.config["server_ip"] = self.server_ip_box.get("1.0", "end-1c")
        self.config["prog_ip"] = self.prog_ip_box.get("1.0", "end-1c")

        with open("e:/scripts/serial_filler/config.json", 'w') as fh:
            json.dump(self.config, fh, indent=4)
