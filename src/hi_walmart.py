import os
from datetime import datetime
from http import HTTPStatus

from flask import Flask, jsonify

app = Flask(__name__)

uptime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
print(uptime)
@app.route('/')
def hi_walmart():
    return 'hi_walmart'

@app.route('/healthz')
def healthz():
    return jsonify({"status":  HTTPStatus.OK, "version": "1", "uptime": "up since " + uptime})

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=int(os.environ.get('PORT', 8080)))
