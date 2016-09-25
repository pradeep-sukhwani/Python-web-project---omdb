"""OMDb API library.
"""
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

from .__meta__ import (
    __title__,
    __summary__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__,
)

from .api import (
    Client,
    get,
    imdbid,
    request,
    search,
    search_movie,
    search_episode,
    search_series,
    set_default,
    title,
)
