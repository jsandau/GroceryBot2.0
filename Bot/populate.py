import psycopg2
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------
# PostgreSQL Connection
# -----------------------
conn = psycopg2.connect(
    dbname="grocerybot",
    user="postgres",
    password="postgres",
    host="localhost"
)
cur = conn.cursor()

# -----------------------
# Users
# -----------------------
users = [f"User_{i}" for i in range(1, 16)]

# -----------------------
# Items with realistic weights
# -----------------------
items = [
    ("frozen berries", 0.03),
    ("everything bagels", 0.02),
    ("plain bagels", 0.03),
    ("non fat milk", 0.08),
    ("butter", 0.03),
    ("red solo cup", 0.02),
    ("plain greek yogurt", 0.05),
    ("apples", 0.06),
    ("oatmeal", 0.03),
    ("forks", 0.02),
    ("vanilla greek yogurt ", 0.05),
    ("tortillas", 0.03),
    ("oil spray", 0.02),
    ("famous amous cookies", 0.03),
    ("honey", 0.02),
    ("bacon", 0.04),
    ("paper plate", 0.02),
    ("trash bags", 0.02),
    ("potato chips", 0.03),
    ("chicken breast", 0.05),
    ("cereal", 0.03),
    ("soap", 0.02),
    ("orange juice", 0.03),
    ("lettuce", 0.02),
    ("chicken nuggets", 0.02),
    ("granola", 0.03),
    ("coffee grounds", 0.02),
    ("bourbon steak seasoning", 0.01),
    ("paper bowl", 0.03),
    ("whole milk", 0.05),
    ("hot sauce", 0.02),
    ("strawberries", 0.04),
    ("barbecue sauce", 0.03),
    ("limes", 0.02),
    ("bananas", 0.06),
    ("white bread", 0.03),
    ("mayonnaise", 0.02),
    ("paper towels", 0.03),
    ("cream cheese", 0.02),
    ("large eggs", 0.03),
    ("raspberries", 0.03),
    ("blueberries", 0.03),
    ("ranch dressing", 0.02),
    ("salsa", 0.02),
    ("peppers", 0.04),
    ("eggs", 0.03),
    ("garlic", 0.01),
    ("ground beef", 0.05),
    ("avocados", 0.04),
    ("blueberries", 0.01),
    ("toilet paper", 0.02),
    ("cheese", 0.03),
    ("reduced fat milk", 0.04),
    ("thai jasmine rice", 0.01),
    ("potatoes", 0.02),
    ("baby spinach", 0.01),
    ("worcestershire sauce", 0.01),
    ("popcorn", 0.02)
]

item_names, weights = zip(*items)

# -----------------------
# Generate 6 weeks of data
# -----------------------
start_date = datetime(2025, 9, 1)
weeks = [start_date + timedelta(weeks=i) for i in range(6)]

requests_data = []
out_of_data = []

for week_start in weeks:
    for user in users:
        # Each user makes 3-6 requests per week
        num_requests = random.randint(3, 6)
        requested_items = random.choices(item_names, weights=weights, k=num_requests)
        
        for item in requested_items:
            # Random timestamp within the week
            day_offset = random.randint(0, 6)
            timestamp = week_start + timedelta(days=day_offset)
            
            # Random quantity using Poisson
            quantity = max(1, int(np.random.poisson(lam=3)))
            
            requests_data.append((timestamp, user, item, quantity))
            
            # 10% chance item is out of stock
            if random.random() < 0.1:
                out_of_data.append((timestamp, user, item))

# -----------------------
# Insert into grocery_requests
# -----------------------
insert_query = """
INSERT INTO grocery_requests (timestamp, name, item_name, quantity)
VALUES (%s, %s, %s, %s)
"""
cur.executemany(insert_query, requests_data)

# -----------------------
# Insert into out_of_db
# -----------------------
insert_out_of = """
INSERT INTO out_of_db (timestamp, name, out_of)
VALUES (%s, %s, %s)
"""
cur.executemany(insert_out_of, out_of_data)

conn.commit()
cur.close()
conn.close()

print(f"✅ Inserted {len(requests_data)} requests and {len(out_of_data)} out-of-stock records.")
