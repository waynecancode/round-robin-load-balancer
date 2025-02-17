import requests
import threading
from flask import Flask, request

app = Flask(__name__)

# List of backend servers
servers = ["http://127.0.0.1:5001", "http://127.0.0.1:5002", "http://127.0.0.1:5003"]
current_server = 0
lock = threading.Lock()  # Prevent race conditions

def get_next_server():
    global current_server
    with lock:
        selected_server = servers[current_server]
        current_server = (current_server + 1) % len(servers)
    return selected_server

@app.route('/')
def load_balance():
    selected_server = get_next_server()

    def forward_request():
        try:
            response = requests.get(selected_server)
            return response.text
        except requests.exceptions.RequestException:
            return "Server is down", 500

    thread = threading.Thread(target=forward_request)
    thread.start()
    return f"Request forwarded to {selected_server}"

if __name__ == '__main__':
    app.run(port=5000, threaded=True)  # Enable multi-threading
