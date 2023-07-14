import tkinter as tk # con esto creamos la ventana
from tkinter import ttk # con esto creamos los elementos



def d_welcome(user):
    global ventana
    ventana = tk.Tk()
    ventana.config(width=200, height=200)
    ventana.title("Login de usuario en tkinter")
    label_user = ttk.Label(text=f"Hola {user}", font=font)
    label_user.place(x=20, y=20)

def login():
    username = entry_user.get()
    print("User: ", entry_user.get())
    print("Password", entry_pass.get())
    ventana.destroy()
    d_welcome(username)

def d_login():
    global entry_user, entry_pass

    label_user = ttk.Label(text="Ingrese su usuario", font=font)
    label_user.place(x=20, y=20)

    entry_user = ttk.Entry(font=font)
    entry_user.place(x=20, y=60)

    label_pass = ttk.Label(text="Ingrese su contraseña", font=font)
    label_pass.place(x=20, y=100)

    entry_pass = ttk.Entry(font=font)
    entry_pass.place(x=20, y=140)

    button = ttk.Button(text="Login", command=login, style="W.TButton", width=21)
    button.place(x=20, y=200)

# Variables
ventana = None
entry_user = None
entry_pass = None

# Programa
font = ("Arial", 20)

ventana = tk.Tk()
ventana.config(width=350, height=400)
ventana.title("Login de usuario en tkinter")
style = ttk.Style()
style.configure('W.TButton', font =
               ('calibri', 20, 'bold', 'underline'),
                foreground = 'blue')

d_login()

ventana.mainloop()