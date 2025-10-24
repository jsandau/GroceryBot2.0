import pandas as pd
import numpy as np
from datetime import timedelta
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/grocerybot")

# Load requests and out-of-stock data
df_requests = pd.read_sql("SELECT * FROM grocery_requests", engine)
df_out_of = pd.read_sql("SELECT DISTINCT out_of FROM out_of_db", engine)

# Step 2: Clean and prepare data

# Map verbose item names to simplified names
item_map = { "Kirkland Signature Three Berry Blend 4 lbs": "frozen berries", "Thomas' Bagels Everything 12 ct": "everything bagels", "Thomas' Bagels Plain 12 ct": "plain bagels", "Kirkland Signature Non Fat Milk 1 Gallon": "non fat milk", "Kerrygold Pure Irish Butter Salted 8 oz 4 ct": "butter", "Kirkland Signature Plastic Cold Cup Red 18 oz 240 ct": "red solo cup", "Kirkland Signature Organic Greek Nonfat Yogurt Plain 3 lbs": "plain greek yogurt", "Honeycrisp Apples 5 lbs": "apples", "Quaker Instant Oatmeal Variety Pack 1.51 oz 52 ct": "oatmeal", "Solo Plastic Fork Heavyweight White 500 ct": "forks", "Chobani Blended Greek Yogurt Vanilla 40 oz": "vanilla greek yogurt", "La Banderita 10\" Flour Tortillas 20 ct": "tortillas", "Chosen Foods Avocado Oil Spray 13.5 oz 2 ct": "oil spray", "Famous Amos Cookies Chocolate Chip 2 oz 42 ct": "famous amous cookies", "Sue Bee Pure Honey Midwest Raw Unfiltered Honey 80 oz": "honey", "Kirkland Signature Fully-Cooked Bacon Hickory Wood Smoked 1 lb": "bacon", "Dixie Ultra Paper Plate 8-1/2\" 240 ct": "paper plate", "Kirkland Signature Outdoor Trash Bags 50 Gallon 70 ct": "trash bags", "Miss Vickie’s Kettle Cooked Potato Chips Variety Pack 1-3/8 oz 30 ct": "potato chips", "Kirkland Signature Lightly Breaded Chicken Breast Chunks 4 lbs": "chicken breast", "Kellogg's Cereal Mini Boxes Variety Pack 25 ct": "cereal", "Dial Antibacterial Foaming Hand Wash + Aloe Spring Water Scent 7.5 fl oz 4 ct": "soap", "Bolthouse Farms 100% Orange Juice 52 fl oz 2 ct": "orange juice", "Shredded Lettuce 5 lbs": "lettuce", "Kirkland Signature Ancient Grains Probiotic Granola 35.3 oz": "granola", "Kirkland Signature Whole Milk 1 Gallon": "whole milk", "Sweet Baby Ray's Barbecue Sauce 40 oz 2 ct": "barbecue sauce", "Bananas 3 lbs": "bananas", "Village Hearth Cottage White Bread 24 oz 2 ct": "white bread", "Hellmann's Real Mayonnaise 1 Gallon": "mayonnaise", "Kirkland Signature 2-Ply Paper Towels White 160 Create-A-Size Sheets 12 ct": "paper towels", "PHILADELPHIA Cream Cheese Spread Original 48 oz": "cream cheese", "Large Eggs 15 Dozen": "large eggs", "Raspberries 12 oz": "raspberries", "Premium Blueberries 18 oz": "blueberries", "Hidden Valley Ranch Homestyle Dressing 40 fl oz 2 ct": "ranch dressing", "Mateo's Gourmet Salsa Medium 32 oz": "salsa", "Mixed Bell Peppers 6 ct": "peppers", "Extra Large Eggs 15 Dozen": "eggs", "Christopher Ranch Monviso Peeled Garlic 3 lbs": "garlic", "Kirkland Signature Organic Ground Beef 85% Lean 15% Fat 4 lbs": "ground beef", "Avocados 6 ct": "avocados", "Kirkland Signature IQF Blueberries 5 lbs": "blueberries", "Kirkland Signature Bath Tissue 30 ct": "toilet paper", "Cascade Dairy Mexican Four Cheese Blend Shredded 5 lbs": "cheese", "Kirkland Signature 2% Reduced Fat Milk 1 Gallon": "reduced fat milk", "Kirkland Signature Thai Hom Mali Jasmine Rice 50 lbs": "thai jasmine rice", "Baking Potatoes 10 lbs": "potatoes", "Organic Baby Spinach 1 lb": "baby spinach", "Lea & Perrins Worcestershire Sauce 20 fl oz 2 ct": "worcestershire sauce", "Kirkland Signature Microwave Popcorn 3.3 oz 44 ct": "popcorn", "Case Sale Jumbo Halal Chicken Breast Boneless Skinless 40 lbs": "chicken breast", "Dunkin' Original Blend Ground Coffee Medium Roast 40 oz": "coffee grounds", "Kirkland Signature Medium Roast Coffee 2.5 lbs": "coffee grounds", "Kinder's Organic Seasoning Bourbon Steak 12.4 oz": "bourbon steak seasoning", "Dixie Ultra Paper Bowl 20 oz 135 ct": "paper bowl", "Cholula Hot Sauce Original 12 fl oz 2 ct": "hot sauce", "Premium Strawberries 2 lbs": "strawberries" }

df_requests['item_name'] = df_requests['item_name'].str.strip()
df_requests['timestamp'] = pd.to_datetime(df_requests['timestamp'])
df_requests['week'] = df_requests['timestamp'].dt.to_period('W').apply(lambda r: r.start_time)
df_requests['item_simple'] = df_requests['item_name'].map(item_map).fillna(df_requests['item_name'])
df_requests['quantity'] = pd.to_numeric(df_requests['quantity'], errors='coerce').fillna(0)

# Aggregate weekly quantities
weekly_data = df_requests.groupby(['week', 'item_simple'])['quantity'].sum().reset_index()
weekly_data['was_out_of_stock'] = weekly_data['item_simple'].isin(df_out_of['out_of'])

# Step 3: Forecast next week

all_output = []
items = weekly_data['item_simple'].unique()
next_week_start = weekly_data['week'].max() + timedelta(weeks=1)

for item in items:
    item_data = weekly_data[weekly_data['item_simple'] == item].sort_values('week').reset_index(drop=True)
    item_data['week_idx'] = np.arange(len(item_data))

    # Forecast using linear regression if enough data
    if len(item_data) >= 2:
        X = item_data['week_idx'].values.reshape(-1, 1)
        y = item_data['quantity'].values
        model = LinearRegression()
        model.fit(X, y)
        predicted_qty = model.predict(np.array([[len(item_data)]]))[0]
        if item_data['was_out_of_stock'].any():
            predicted_qty *= 1.2
        predicted_qty = max(0, round(predicted_qty))
    else:
        predicted_qty = int(item_data['quantity'].iloc[-1])

    # Add historical rows
    for _, row in item_data.iterrows():
        all_output.append({
            'week_start': row['week'],
            'item_name': item,
            'quantity': row['quantity'],
            'was_out_of_stock': row['was_out_of_stock'],
            'predicted': False
        })

    # Add predicted row
    all_output.append({
        'week_start': next_week_start,
        'item_name': item,
        'quantity': predicted_qty,
        'was_out_of_stock': item_data['was_out_of_stock'].any(),
        'predicted': True
    })

# Step 4: Save to CSV

final_df = pd.DataFrame(all_output)
final_df.to_csv("tableau_grocery_db_only.csv", index=False)
print("✅ Predicted + historical database data saved to 'tableau_grocery_db_only.csv'")
