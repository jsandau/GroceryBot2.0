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
[https://public.tableau.com/views/GroceryBotData/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]   
'''<div class='tableauPlaceholder' id='viz1761270711972' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gr&#47;GroceryBotData&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='GroceryBotData&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gr&#47;GroceryBotData&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1761270711972');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1177px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''   
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
