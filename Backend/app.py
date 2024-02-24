from flask import Flask, jsonify
from routes.sentiment import analyze_sentiment

app = Flask(__name__)

app.add_url_rule('/analyze-sentiment', view_func=analyze_sentiment, methods=['POST'])

# Define a route for the API.
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
