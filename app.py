from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Redis connection setup using environment variables
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return "Welcome to the Python Redis app!"

@app.route('/set/<key>/<value>')
def set_key(key, value):
    redis_client.set(key, value)
    return jsonify({"message": f"Key '{key}' set to '{value}'."})

@app.route('/get/<key>')
def get_key(key):
    value = redis_client.get(key)
    if value:
        return jsonify({key: value})
    else:
        return jsonify({"error": f"Key '{key}' not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
