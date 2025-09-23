# frontend/gui/user_view.py

import ttkbootstrap as ttk

def build_user_frame(root, user):
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="👤 Perfil de usuario", font=("Helvetica", 16)).pack(pady=10)
    ttk.Label(frame, text=f"Correo: {user['email']}").pack()
    ttk.Label(frame, text=f"Rol: {user['role']}").pack()
