# -*- coding:utf-8 -*-
__author__ = "ganbin"
try:
    from tkinter import *
except ImportError:
    from TKinter import *
try:
    from pyperclip import copy as copy_board
except ImportError:
    from win32clipboard import SetClipboardData as copy_board



class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def add_copy(self):
        copy = Button(self)
        copy["text"] = "copy"
        copy["command"] = lambda: self.copy_data(text=text)
        copy.pack({"side": "bottom"})
        text = Text(self, width=25, height=1.5)
        text.pack({"side": "bottom"})

    def copy_data(self, text):
        copy_board(text.get('0.0', 'end'))


    def createWidgets(self):
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["fg"] = "red"
        QUIT["command"] = self.quit

        QUIT.pack({"side": "top"})

        add = Button(self)
        add["text"] = "Add",
        add["command"] = self.add_copy
        add.pack({"side": "top"})


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
