"""The Replit Python module."""

from .audio import Audio
from .database import db, Database
from .users import get_user, User

# Backwards compatibility.
from .termutils import clear


audio = Audio()
