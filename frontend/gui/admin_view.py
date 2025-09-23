# frontend/gui/admin_view.py

import ttkbootstrap as ttk
from backend.controllers.user_controller import get_all_users, delete_user

def build_admin_frame(root):
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="👤 Usuarios registrados", font=("Helvetica", 16)).pack(pady=10)

    users = get_all_users()
    for user in users:
        user_frame = ttk.Frame(frame)
        user_frame.pack(fill="x", pady=2)

        ttk.Label(user_frame, text=f"{user['email']} ({user['role']})").pack(side="left")
        ttk.Button(user_frame, text="Eliminar", bootstyle="danger", command=lambda e=user['email']: delete_user(e)).pack(side="right")
