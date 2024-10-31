from flask import Flask, jsonify
import asyncio  # Import asyncio for asynchronous operations

app = Flask(__name__)

@app.route('/', methods=['GET'])
async def hello_world():
    await asyncio.sleep(15)  # Non-blocking 15-second delay
    return jsonify(message='Hello world'), 200

# Remove or comment out the app.run() block
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
