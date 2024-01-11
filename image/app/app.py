from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def echo(path):
    if request.method == 'POST':
        print("type(request.json):", type(request.json))
        response_dict = {
            "headers": dict(request.headers),
            "request_data": request.json,
            "path": path,
            "method": request.method,
            "url": request.url,
            "host": request.host
        }
        return jsonify(response_dict)
    else:
        response_dict = {
            "headers": dict(request.headers),
            "request_data": None,
            "path": path,
            "method": request.method,
            "url": request.url,
            "host": request.host
        }
        return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True)
