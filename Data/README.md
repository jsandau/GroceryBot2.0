# 🛒 GroceryBot

A simple **GroupMe bot** built with **Python, Flask, and ngrok** that listens for messages in a group chat and logs grocery requests to an Excel file.

# Why?
While in my college fraternity, I noticed inefficiencies in our weekly grocery ordering process. Our VP of Finance would text the GroupMe an hour before placing the order, asking for requests. This led to a flood of messages in the chat, and many members would forget items they had thought of earlier in the week. To address this, I developed a bot to streamline the process and ensure everyone’s requests were captured efficiently.
## 🚀 Features

- Listens for GroupMe messages using a webhook  
- Responds to commands like `!request milk`  
- Saves all requests with a timestamp and sender name to `GroceryRequests.xlsx`  
- Automatically greets users who say “hello”  

## 🧰 Technologies Used

- Python 3  
- Flask  
- openpyxl  
- requests  
- ngrok (for tunneling localhost)  
- GroupMe Bots API

## INSTALL REQUIREMENTS ##
pip install -r requirements.txt

## ⚙️ How It Works

1. Run the Flask app locally:  
   ```bash
   python app.py

2. In a separate Terminal, start ngrok with:
ngrok http 5000

3. Copy the https URL ngrok gives you and paste it into your GroupMe bot’s callback URL.

4.Send a message in GroupMe:
!request apples

5. The bot then replies and logs it into your Excel File.

🧠 Future Improvements

- Host permanently on a cloud server

- Add a command to list all current grocery requests

- Use a database instead of Excel


 
