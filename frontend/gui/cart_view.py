# frontend/gui/cart_view.py

import ttkbootstrap as ttk
from backend.controllers.cart_controller import calculate_total

def build_cart_frame(root, cart_items):
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="🛒 Carrito de compras", font=("Helvetica", 16)).pack(pady=10)

    for item in cart_items:
        ttk.Label(frame, text=f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}").pack()

    total = calculate_total(cart_items)
    ttk.Label(frame, text=f"Total: ${total:.2f}", font=("Helvetica", 14)).pack(pady=10)
