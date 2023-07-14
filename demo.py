import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.config(width=200, height=200)
user_label=""
pass_label=""
# Form login
def login():
    global user_label, pass_label
    title = ttk.Label(text="Login")
    title.place(x=20, y=10)
    user_label_1 = ttk.Label(text="User")
    user_label_1.place(x=20, y=30)
    user_label = ttk.Entry(width=150)
    user_label.place(x=20, y=50, width=100)
    pass_label = ttk.Entry(width=150)
    pass_label.place(x=20, y=100, width=100)
    boton_convertir = ttk.Button(text="Convertir", command=validate)
    boton_convertir.place(x=20, y=150)

def validate():
    global ventana
    print(user_label.get())
    print(pass_label.get())
    ventana.destroy()
    ventana = tk.Tk()
    ventana.config(width=200, height=200)
    login()

login()
ventana.mainloop()