"""The Replit Python module."""

from . import flask_tools
from . import termutils
from .audio import Audio
from .database import db

# Backwards compatibility.
from .termutils import clear


audio = Audio()

# TODO: DB convience methods like nuke and a CLI to interact with it?
