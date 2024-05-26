import tkinter as tk
from tkinter import messagebox


# login window
root = tk.Tk()

lbl1 = tk.Label(root, text="Username", bg="white")
lbl1.pack()
lbl1.place(x=10, y=10)

lbl2 = tk.Label(root, text="Password", bg="white")
lbl2.pack()
lbl2.place(x=10, y=40)

# login function
entry1 = tk.Entry(root, width=20)
entry1.pack()
entry1.place(x=100, y=10)
entry2 = tk.Entry(root, width=20)
entry2.pack()
entry2.place(x=100, y=40)


def login():
    username = entry1.get()
    password = entry2.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Operación exitosa")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")


root.resizable
button = tk.Button(root, text="Login", command=login)
button.pack()
button.place(x=10, y=200)

# estilizando la ventana

root.resizable(0, 0)
root.configure(bg="black")
root.iconbitmap("./images/Logo_UNAP.ico")
root.geometry("540x250")
root.title("Login")

# estilizando el boton y los labels

button.config(bg="white", fg="black", padx=10,
              font="Sans 12", relief="solid", foreground="black",
              activebackground="white")
lbl1.config(bg="white", fg="black", padx=10,
            relief="solid", font="Helvetica 12")
lbl2.config(bg="white", fg="black", padx=10,
            relief="solid", font="Helvetica 12")
entry1.config(show="", font="Helvetica 12", bd=2, relief="solid")
entry2.config(show="*", font="Helvetica 12", bd=2, relief="solid")

# agregando imagen al costado de la ventana con grid
image = tk.PhotoImage(file="./images/images.png")
label = tk.Label(root, image=image)
label.pack()
label.place(x=300, y=5)


# register func

def register():
    messagebox.askquestion("Register", "¿Desea registrarse?")


lbl3 = tk.Label(root, text="¿No tienes cuenta?", bg="white")
lbl3.pack()
lbl3.place(x=12, y=70)

button2 = tk.Button(root, text="Regístrate", command=register)
button2.pack()
button2.place(x=12, y=100)


root.mainloop()
