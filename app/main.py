"""
This Module contain an endpoint of microservice "Hello World".
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    This function return "Hello, World!".
    API main of microservice.
    """
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
