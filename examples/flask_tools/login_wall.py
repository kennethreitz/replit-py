"""An example of the app.login_wall() feature."""
from replit.flask_tools import ReplitApp, Link
from replit.flask_tools import auth_info

app = flask_tools.ReplitApp(__name__)


def login_page() -> str:
    return "Hello, please sign in to access this page!\n" + flask_tools.sign_in_snippet


# this is an example of the arguments, but the exclude kwarg already defaults to this
#  and there is a default handler as well.
app.login_wall(exclude=["/"], handler=login_page)


@app.route("/")
def index() -> str:
    return f"Hello! {flask_tools.Link('check out this page', href='/page')}"


@app.route("/page")
def page() -> str:
    return f"Hello {flask_tools.auth.name}, if you are reading this you signed in."


if __name__ == "__main__":
    app.run()
