"""The Replit Python module."""

from .audio import Audio
from .database import db
from .users import User

# Backwards compatibility.
from .termutils import clear


audio = Audio()
