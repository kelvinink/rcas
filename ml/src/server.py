# Providing load balance for sentiment analysis module
import requests
from ml.src import config
from flask import Flask, jsonify, request, Response

idx = 0

app = Flask(__name__)

@app.route('/api/ml/sentiment', methods=['GET'])
def lb_sentiment():
    global idx
    text = request.args.get('text')
    url = "http://{}:{}/api/ml/sentiment?text={}".format(
        config.SERVERS[idx][0],
        config.SERVERS[idx][1],
        text
    )
    resp = requests.get(url)

    idx += 1
    idx = idx if idx < len(config.SERVERS) else 0

    return resp.content.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)