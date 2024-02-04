import tkinter as tk

win = tk.Tk()
win.title("Nick's Python Journal")
win.geometry('1000x900')
win.resizable(True, True)
win.iconbitmap('/Users/nick/PycharmProjects/journal/favicon.ico')

def read() :
    f = open("journal.txt", "r")
    a.config(text=f.read())

photo = tk.PhotoImage(file='/Users/nick/PycharmProjects/journal/pjg.png')
a = tk.Label(win, text="")
image1 = tk.Label(image=photo)
image1.pack()
a.pack()
tk.Button(win, text="Read Entries", command=read).pack()

win.mainloop()


