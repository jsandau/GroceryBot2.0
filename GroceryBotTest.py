from flask import Flask, request
import requests
import openpyxl
import os
# creates a flask web app
app = Flask(__name__)

# id of bot
BOT_ID = "a1c844f53a769f6f76063c6e5b"
EXCEL_FILE = "GroceryRequests.xlsx"
if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Timestamp", "Name", "Request"])  # header
    wb.save(EXCEL_FILE)
# this is called everytime group me sends the bot a message
@app.route("/", methods=["POST"])
def webhook():
    #gets the json data sent to the callback url
    data = request.get_json()
    # ignore if the bot say something in the field that prompts a command
    if "bot_id" in data:
        return "ok", 200
    # make sure the json retrivied has a text field aka a message was sent
    if "text" in data:
        msg = data["text"].lower()

        if "hello" in msg:
            send_message("hey")

        elif msg.startswith("!request"):
            info = msg.replace("!request", "").strip()
            sender = data.get("name", "Unknown")
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_to_excel(timestamp, sender, info)
            send_message(f"{info} added to the grocery list.")
    return "ok", 200

def send_message(text):
    url = "https://api.groupme.com/v3/bots/post"
    payload = {"bot_id": BOT_ID, "text": text}
    requests.post(url, json=payload)

def save_to_excel(timestamp, name, info):
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([timestamp, name, info])  # append a new row
    wb.save(EXCEL_FILE)
if __name__ == "__main__":
    app.run(port=5000)