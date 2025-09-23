# frontend/gui/auth_view.py

import ttkbootstrap as ttk
from backend.controllers.auth_controller import login, register
from tkinter import messagebox

def build_auth_frame(root, on_success):
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    email_var = ttk.StringVar()
    pass_var = ttk.StringVar()

    ttk.Label(frame, text="Correo:").pack()
    ttk.Entry(frame, textvariable=email_var).pack()

    ttk.Label(frame, text="Contraseña:").pack()
    ttk.Entry(frame, textvariable=pass_var, show="*").pack()

    def handle_login():
        user = login(email_var.get(), pass_var.get())
        if user:
            on_success(user)
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

    def handle_register():
        user = register(email_var.get(), pass_var.get())
        if user:
            messagebox.showinfo("Registro", "Usuario creado correctamente")
        else:
            messagebox.showerror("Error", "Correo ya registrado")

    ttk.Button(frame, text="Ingresar", command=handle_login).pack(pady=5)
    ttk.Button(frame, text="Registrarse", command=handle_register).pack()
