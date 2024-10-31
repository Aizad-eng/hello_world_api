from flask import Flask, jsonify
import time  # Import time for delay

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    time.sleep(15)  # Introduce a 15-second delay
    return jsonify(message='Hello world'), 200

# Remove or comment out any app.run() block
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
