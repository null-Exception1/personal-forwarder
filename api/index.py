from flask import Flask
from flask import request, jsonify
import base64 as b64
import redis
app = Flask(__name__)
new_uri = "None"

kv = redis.from_url(os.environ.get("KV_REDIS_URL").replace("redis://", "rediss://"), decode_responses=True)


@app.route('/post')
def home():
    args = request.args
    global new_uri
    new_uri = args['uri']
    new_uri = b64.b64decode(new_uri).decode('utf-8')
    print(new_uri)
    kv.set('active_url', new_url)
    return 'OK', 200

@app.route('/ping')
def ping():
    return 'pong', 200
@app.route('/get')
def about():

    return kv.get('active_url')

#if __name__ == "__main__":
#    app.run(debug=True)