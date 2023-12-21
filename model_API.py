from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get():
    data = {'message' : 'Hello, World'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=3300)
