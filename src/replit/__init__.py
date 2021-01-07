"""The Replit Python module."""

from . import web
from . import termutils
from .audio import Audio
from .database import db
from .users import ReplitUser

# Backwards compatibility.
from .termutils import clear


audio = Audio()

# TODO: DB convience methods like nuke and a CLI to interact with it?
