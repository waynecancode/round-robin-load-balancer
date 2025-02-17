from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Response from Server 2"

if __name__ == '__main__':
    app.run(port=5002)
