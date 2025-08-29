from flask import Flask
import os
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "server is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)

def start_flask():
    thread = Thread(target=run_flask)
    thread.start()

start_flask()
