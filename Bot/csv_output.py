import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# 1️⃣ Read the CSV
csv_file = 'grocery_invoice_raw.csv'  # replace with your actual CSV filename
df = pd.read_csv(csv_file)

# 2️⃣ Clean Week column to numeric
df['Week_num'] = df['Week'].str.extract('(\d+)').astype(int)

# 3️⃣ Clean Item Name
df['Item Name'] = df['Item Name'].str.strip()

# 4️⃣ Aggregate weekly totals per item
weekly_totals = df.groupby(['Week_num', 'Item Name'], as_index=False)['Quantity'].sum()

# 5️⃣ Prepare a DataFrame for predictions
items = weekly_totals['Item Name'].unique()
prediction_results = []

# 6️⃣ Linear trend prediction for each item with gap handling
for item in items:
    item_data = weekly_totals[weekly_totals['Item Name'] == item].copy()
    
    # Fill missing weeks with 0 (assume missing = 0)
    all_weeks = pd.DataFrame({'Week_num': range(item_data['Week_num'].min(), item_data['Week_num'].max()+1)})
    item_data = all_weeks.merge(item_data, on='Week_num', how='left')
    item_data['Item Name'] = item
    item_data['Quantity'] = item_data['Quantity'].fillna(0)
    
    # Linear regression
    X = item_data['Week_num'].values.reshape(-1, 1)
    y = item_data['Quantity'].values
    if len(X) > 1:
        model = LinearRegression()
        model.fit(X, y)
        next_week = X.max() + 1
        predicted_qty = max(0, round(model.predict([[next_week]])[0]))  # avoid negative prediction
    else:
        predicted_qty = y[0]  # fallback if only 1 week exists
    
    prediction_results.append({'Week': f'week {next_week}', 'Item Name': item, 'Predicted Quantity': predicted_qty})

# 7️⃣ Convert to DataFrame
predictions_df = pd.DataFrame(prediction_results)

# 8️⃣ Combine historical data + predictions for Tableau
weekly_totals.rename(columns={'Week_num': 'Week'}, inplace=True)
weekly_totals['Week'] = 'week ' + weekly_totals['Week'].astype(str)
tableau_df = pd.concat([weekly_totals[['Week', 'Item Name', 'Quantity']], predictions_df.rename(columns={'Predicted Quantity':'Quantity'})], ignore_index=True)
tableau_df.sort_values(by=['Item Name', 'Week'], inplace=True)

# 9️⃣ Export to CSV
predictions_df.to_csv('predicted_next_week.csv', index=False)
tableau_df.to_csv('tableau_ready.csv', index=False)

print("✅ Predictions saved to 'predicted_next_week.csv' and 'tableau_ready.csv'")
