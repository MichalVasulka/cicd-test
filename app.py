from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/endpoint1')
def endpoint1():
    result = {'message': 'Hello from endpoint1'}
    return jsonify(result)

@app.route('/api/endpoint2')
def endpoint2():
    result = {'message': 'Hello from endpoint2'}
    return jsonify(result)

@app.route('/api/endpoint3')
def endpoint3():
    result = {'message': 'Hello from endpoint3'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
