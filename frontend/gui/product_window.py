# frontend/gui/product_view.py

import ttkbootstrap as ttk
from backend.controllers.product_controller import get_all_products
from frontend.gui.cart_view import build_cart_frame

def build_product_frame(root):
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="🛍️ Catálogo de productos", font=("Helvetica", 16)).pack(pady=10)

    products = get_all_products(limit=20)
    cart = []

    for product in products:
        product_frame = ttk.Frame(frame)
        product_frame.pack(fill="x", pady=2)

        ttk.Label(product_frame, text=f"{product['name']} - ${product['price']}").pack(side="left")
        ttk.Button(product_frame, text="Agregar al carrito", command=lambda p=product: cart.append(p)).pack(side="right")

    ttk.Button(frame, text="Ver carrito", bootstyle="info", command=lambda: build_cart_frame(root, cart)).pack(pady=10)
