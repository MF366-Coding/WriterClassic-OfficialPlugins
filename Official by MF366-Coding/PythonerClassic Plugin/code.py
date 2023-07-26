import os
import sys
from tkinter import messagebox as mb

if sys.platform == "linux" or sys.platform == "darwin":
    title = "Run file with Python 3"
else:
    title = "Run file with PATH Python"

def plugin(tk_root, tk_text, _file):
    if _file == False:
        mb.showinfo("PythonerClassic", "The file must be saved.")
    elif _file != False and _file.endswith(".py"):
        with open(_file, "r", encoding="utf-8") as filech:
            filez = filech.read()
        if filez == "":
            mb.showinfo("PythonerClassic", "The file musn't be empty.")
        elif filez != "":
            if sys.platform == "win32":
                os.system(f"python {_file}")
            elif sys.platform == "linux" or sys.platform == "darwin":
                os.system(f"python3 {_file}")
    else:
        mb.showinfo("PythonerClassic", "The file must be a non-compiled regular Python file.")