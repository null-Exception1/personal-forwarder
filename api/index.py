from flask import Flask
from flask import request, jsonify
import base64 as b64
app = Flask(__name__)
new_uri = "None"

@app.route('/post')
def home():
    args = request.args
    global new_uri
    new_uri = args['uri']
    new_uri = b64.b64decode(new_uri).decode('utf-8')
    print(new_uri)
    return 'OK', 200

@app.route('/ping')
def ping():
    return 'pong', 200
@app.route('/get')
def about():
    global new_uri
    return new_uri

if __name__ == "__main__":
    app.run(debug=True)