"""A basic example of repl auth."""
from replit import flask_tools

app = flask_tools.App(__name__)


@app.route("/")
def index():
    if flask_tools.signed_in:
        return "Hello " + flask_tools.auth.name
    else:
        return flask_tools.signin()  # optionally: simple.sigin(title="My title")


if __name__ == "__main__":
    app.run()
