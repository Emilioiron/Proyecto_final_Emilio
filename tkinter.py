import tkinter as tk
import main
!pip install tkinter

WINDOW_SIZE = "600x400"

root = tk.Tk()
root.geometry(WINDOW_SIZE)

btn = tk.Button(root, text="Insuline you need!", command=main.main)
btn.pack()