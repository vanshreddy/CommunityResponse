from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the API.
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
