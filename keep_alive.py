from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return {'status_bot': 'working'}

def run():
    app.run(host="0.0.0.0", port=800000)

def keep_alive():
    server = Thread(target=run)
    server.start()