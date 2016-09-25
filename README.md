# Python-web-project---omdb

Now you fetch movie details from the given link:

ps-interview.appspot.com

# Requirements.txt:

> omdb module

> python

> html

> css

> Requests

> toolbelt.requests

> webapp2

> need to manipulate the init function of omdb module as per google app engine, so that whevener the omdb call any functions at that time it also calls the request functions which convert into toolbelt.request function as a adapter, so that the requests uses the urlfetch.

> For more details just go to omdb-0.7.0/omdb/__init__.py - you can find the request and requests_toolbelt.adapters.appengine.

> for more details on toolbelt adapter(it is like a adapter which takes request and converts into urlfetch - basically for google app engine as this whole project is hosted on google app engine.), you can find on this site:
https://cloud.google.com/appengine/docs/python/issue-requests
