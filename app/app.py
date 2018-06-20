from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080) - don't use the flask development server
    serve(app, host='0.0.0.0', port=8080)
