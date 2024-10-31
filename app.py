from flask import Flask, jsonify
import time  # Import the time module

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    time.sleep(15)  # Delay the response by 15 seconds
    return jsonify(message='Hello world'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
