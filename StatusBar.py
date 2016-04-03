import tkinter as tk


class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.variable = tk.StringVar()
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',16,'normal'))
        self.variable.set('Status Bar')
        self.label.pack(fill=tk.X)
        self.pack()
