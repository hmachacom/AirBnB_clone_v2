#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_hbnb():
    """_summary_
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
