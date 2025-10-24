from flask import Flask, request
import requests
import openpyxl
import os
import psycopg2
from datetime import datetime

# creates a flask web app
app = Flask(__name__)

# id of bot
BOT_ID = "a1c844f53a769f6f76063c6e5b"

# Function to save a request to PostgreSQL database
def save_request_to_db(timestamp, name, request_text):
    with psycopg2.connect(
        dbname="grocerybot",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO grocery_requests (timestamp, name, item_name, quantity) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (timestamp, name, request_text, 1))  # 1 is default quantity
            conn.commit()  # commit is optional here; 'with' usually handles it

# Function to mark something as out on database
def mark_as_out_of(timestamp, name, out_of_text):
    with psycopg2.connect(
        dbname="grocerybot",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO out_of_db (timestamp, name, out_of) VALUES (%s, %s, %s)"
            cur.execute(sql, (timestamp, name, out_of_text))
            conn.commit() 


# Function to get all requests from database
def get_all_requests():
    with psycopg2.connect(
        dbname="grocerybot",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM grocery_requests ORDER BY timestamp")
            return cur.fetchall()

# Flask webhook endpoint
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    
    if "bot_id" in data:
        return "ok", 200

    if "text" in data:
        msg = data["text"].lower()
        sender = data.get("name", "Unknown")
        timestamp = datetime.now()

        if "hello" in msg:
            send_message(f"👋 Hey there {sender}! Use \"!help\" for a list of commands.")

        elif msg.startswith ("!help"):
            send_message(f"!request - sends a request to the grocery list database. Ex: !request apples \n\n!out - Logs that were out of something to the database. Ex: !out apples")

        elif msg.startswith("!out"):
            info = msg.replace("!out", "").strip()

            mark_as_out_of(timestamp, sender, info)

            send_message(f"Got it. Logging that we are out of {info}, to the database.")
        elif msg.startswith("!request"):
            info = msg.replace("!request", "").strip()
            
            # Save to database
            save_request_to_db(timestamp, sender, info)
            send_message(f"{info} added to the grocery list.")
    return "ok", 200

# Function to send a message back to GroupMe
def send_message(text):
    url = "https://api.groupme.com/v3/bots/post"
    payload = {"bot_id": BOT_ID, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(port=5000)
