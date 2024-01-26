from tkinter import *
from tkinter import filedialog
import os, subprocess, sys

def run_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def open_file():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file:",
                                          filetypes= (("All files","*.*"),
                                          ("Text files","*.txt")))
    run_file(filepath)

window = Tk()
button = Button(text="Open",command=open_file)
button.pack()
window.mainloop()