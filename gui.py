import tkinter as tk
import main
import time
x = time.time()
timee = str(x)
window = tk.Tk()
frame_a = tk.Frame()

entry_displays = tk.Label(text="", master=frame_a)
entry_journal= tk.StringVar()
journal_entry = tk.Entry(textvariable=entry_journal, text="Enter entry here: ")

def entry():
    journal = entry_journal.get()
    entry_journal.set("")


def btn1():
    f = open("journal.txt", "r")
    strconv = str(f.read())
    entry_displays.config(text=strconv)
    entry_displays.pack()
    f.close()

def btn2() :
    f = open("journal.txt", "a")
    f.write(timee)
    entry()
    f.write("\n")
    user = str(entry)
    f.write(user)
    f.write("\n")
    f.close()

greeting = tk.Label(text="Hello, Nick", width = 10, height = 10, master=frame_a)
Read_Button = tk.Button(text="Read Entries", width=25, height=5, command=btn1(), master=frame_a)
Write_Button = tk.Button(text="Write an Entry", width=25, height=5, command=btn2(), master=frame_a)
entry_displays = tk.Label(text="", master=frame_a)



def window_func():
    greeting.pack()
    Read_Button.pack()
    Write_Button.pack()
    entry()
    frame_a.pack()
    window.mainloop()