from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        mensaje.set("Hola tonotos")
    except ValueError:
        pass

root = Tk()
root.geometry("300x150")
root.title("XD")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()


for i in range(1, 4):
    for j in range(1, 4):
        button = ttk.Button(mainframe, text="Calculate")
        button.grid(column=j, row=i, sticky=W)
        button.bind("<Button-1>")
        

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()