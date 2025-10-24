GroceryBot 🛒

A lightweight Python + Flask application that tracks weekly grocery requests, stores them in a SQL database, and generates forecasts for inventory and ordering. Data is exported to CSV for visualization in Tableau dashboards.

🚀 Features

Automated Request Logging: Captures grocery item requests via GroupMe Bot or manual entry.

SQL Database Integration: Stores weekly item counts and stock status.

Predictive Forecasting: Uses six weeks of data to flag and estimate upcoming needs.

Tableau Visualization: Displays trends in item demand, stock status, and predicted orders.

Data Export: Weekly reports are saved as .csv for use in Tableau or other analytics tools.

🧰 Tech Stack

Languages: Python

Frameworks: Flask

Database: SQL (local or hosted)

Libraries: openpyxl, pandas

Visualization: Tableau (connected via CSV extracts)

📈 Example Workflow

Grocery requests are logged by the bot or entered manually.

Data is stored in the SQL database (grocery_db).

A forecast script analyzes weekly quantities and generates a predicted column.

Results are exported to CSV and uploaded to Tableau for dashboard visualization.

📊 Tableau Dashboard
(Dashboard)[https://public.tableau.com/views/GroceryBotData/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]
The dashboard highlights:

Item trends over time

Out-of-stock patterns

Predicted upcoming needs

Filtering by week or item


💡 Future Improvements

Add an interactive front-end dashboard.

Automate Tableau data refreshes.

Implement machine learning for more accurate demand forecasting.

👨‍💻 Author

Jacob Sandau
University of Minnesota
📬 LinkedIn: [https://www.linkedin.com/in/jacob-sandau-204743233/] - jsandau@sandau.com
