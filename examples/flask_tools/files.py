from replit import flask_tools

app = flask_tools.App(__name__)


@app.route("/")
def index():
    # Once a file is loaded once, it is cached in memory unless you pass the no_cache
    # kwarg to the File constructor
    f = flask_tools.File(__file__)
    # Tell the browser its just text, not a webpage
    # we can edit the headers directly because the file is just a flask.Response object
    f.headers["Content-Type"] = "text/plain"
    return f
