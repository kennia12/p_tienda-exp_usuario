# frontend/gui/main_window.py

import tkinter as tk
from frontend.gui.theme_config import apply_theme
from frontend.gui.auth_view import build_auth_frame
from frontend.gui.dashboard_view import build_dashboard

def launch_app():
    root = tk.Tk()
    style = apply_theme()
    root.title("Tienda Python")
    root.geometry("1024x768")

    def on_login_success(user):
        for widget in root.winfo_children():
            widget.destroy()
        build_dashboard(root, user)

    build_auth_frame(root, on_login_success)
    root.mainloop()
