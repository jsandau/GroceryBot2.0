# 🛒 GroceryBot

A lightweight **Python + Flask application** that tracks weekly grocery requests, stores them in a **SQL database**, and generates forecasts for inventory and ordering. Data is exported to CSV for visualization in **Tableau dashboards**.  

# Why?
While in my college fraternity, I noticed inefficiencies in our weekly grocery ordering process. Our VP of Finance would text the GroupMe an hour before placing the order, asking for requests. This led to a flood of messages in the chat, and many members would forget items they had thought of earlier in the week. To address this, I developed a bot to streamline the process and ensure everyone’s requests were captured. To take it a step further, I added a simple prediction system that uses historical data to estimate how much of each item we’ll need in upcoming weeks. This helps avoid over-ordering or running out of popular items, making the ordering process more efficient and reducing waste.

## 🚀Features

**Automated Request Logging:** Captures grocery item requests via GroupMe Bot or through *population.py* to simulate weekly grocery requests.   

**SQL Database Integration:** Stores weekly item counts and stock status.   

**Predictive Forecasting:** Uses six weeks of data to flag and estimate upcoming needs.    

**Tableau Visualization:** Displays trends in item demand, stock status, and predicted orders.   

**Data Export:** Weekly reports are saved as .csv for use in Tableau or other analytics tools.   

---   

## 🧰 Tech Stack

**Languages:** Python   
**Frameworks:** Flask   
**Database:** PostgreSQL
**Libraries:** numpy, pandas, scikit-learn, SQLAlchemy  
**Visualization:** Tableau (connected via CSV extracts)   

---   

## 📈 Workflow   
Grocery requests are logged by the bot or entered manually through populate.py.   
Data is stored in PostgreSQL (grocery_requests and out_of_db).   
A forecasting script analyzes weekly quantities and generates predicted quantities.   
Results are exported to CSV (tableau_grocery_db_only.csv).   
CSV files are uploaded to Tableau for dashboard visualization.   

---   

## 📊 Tableau Dashboard
[View Dashboard](https://public.tableau.com/views/GroceryBotData/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)     
* Track item trends over time
* Identify out-of-stock patterns
* View predicted upcoming needs
* Filter by week or item for detailed analysis

---   

## 💡 Future Improvements
- Add an interactive front-end dashboard.   
- Automate Tableau data refreshes.   
- Implement machine learning for more accurate demand forecasting.   

---   

## 👨‍💻 Author
Jacob Sandau
University of Minnesota
📬 LinkedIn: [https://www.linkedin.com/in/jacob-sandau-204743233/]
📧 Email: jsandau@sandau.com
