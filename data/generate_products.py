# data/generate_products.py

from faker import Faker
from datetime import datetime
import random

fake = Faker()

# Categorías simuladas
CATEGORIES = ["electrónica", "ropa", "hogar", "libros", "juguetes", "deportes", "belleza"]

def generate_product():
    return {
        "name": fake.unique.word().capitalize(),
        "description": fake.sentence(nb_words=8),
        "price": round(random.uniform(10.0, 1500.0), 2),
        "stock": random.randint(1, 1000),
        "category": random.choice(CATEGORIES),
        "created_at": datetime.utcnow()
    }

def generate_bulk_products(total=500_000, batch_size=5000):
    """
    Genera productos en lotes para inserción eficiente.
    """
    for _ in range(total // batch_size):
        yield [generate_product() for _ in range(batch_size)]
