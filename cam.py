# Required to allow reading of jpegData. Flask must be imported after this code.
import colorama
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug import formparser

from debug import request_dump
from formparser_override import parse_multipart_headers_fix

formparser.parse_multipart_headers = parse_multipart_headers_fix

# Now we can continue.
from werkzeug import exceptions
from flask import Flask, request

# Import crucial components
import config
import render

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
import models

# Create schema and migrate accordingly
migrate = Migrate(app, db, compare_type=True)
with app.test_request_context():
    db.init_app(app)
    db.create_all()

# Enable debug printing
debug = app.debug
if debug:
    colorama.init()

# These require database access.
from camlib import response
from routes import action_list, file_action_list


@app.route("/wii_svr/WPOperationServlet", methods=["GET", "POST"])
def op_servlet():
    if debug:
        request_dump(request)

    try:
        action = request.headers["Operation"]
        return action_list[action](request)
    except KeyError:
        # This is not an action or a format we know of.
        return exceptions.NotFound()


@app.route("/wii_svr/WPFileOperationServlet", methods=["GET", "POST"])
@response()
def file_op_servlet():
    if debug:
        request_dump(request)

    try:
        action = request.headers["Operation"]
        return file_action_list[action](request)
    except KeyError:
        return exceptions.NotFound()
