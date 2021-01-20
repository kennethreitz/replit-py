.. replit documentation master file, created by
   sphinx-quickstart on Mon Jun 22 18:35:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Replit-py's API Guide!
=================================

.. figure:: https://github.com/kennethreitz42/replit-py/blob/kr-cleanup/ext/readme.gif?raw=true

This repository is the home for the ``replit`` Python package, which
provides:

-  A fully-featured database client for `Repl.it DB`_. `[docs]`_
-  A **work in progress** Repl.it user profile lookup. `[docs]`_
-  A Flask application decorator for ensuring Repl.it Auth required on
   specific routes. `[docs]`_

& other helpful toys and utilities, like…

-  A simple audio library that can play tones and audio files!
-  Some helpful functions for displaying ANSI colors within interactive
   terminal sessions.

It’s worth noting…
~~~~~~~~~~~~~~~~~~

The `Repl.it`_ Python environment does not require any platform-specific
code, however, these optional utilities provide additional platform
features in a simple and accessible way.

*Example*: `Repl.it DB`_ is an HTTP service, but an optional Python
client (here!) is available.

.. _Repl.it DB: https://docs.repl.it/misc/database
.. _[docs]: https://example.com
.. _Repl.it: https://repl.it/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Module contents
---------------

.. automodule:: replit
   :members:
   :undoc-members:
   :show-inheritance:

replit.database module
----------------------

.. automodule:: replit.database
   :members:
   :undoc-members:
   :show-inheritance:

replit.audio module
-------------------

.. automodule:: replit.audio
   :members:
   :undoc-members:
   :show-inheritance:

replit.users module
-------------------

.. automodule:: replit.users
   :members:
   :undoc-members:
   :show-inheritance:

replit.maqpy module
-------------------

.. automodule:: replit.web
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
