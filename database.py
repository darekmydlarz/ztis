import os
from urlparse import urlsplit
from pymongo import Connection

url = os.getenv('MONGOLAB_URI', 'uri plx')
parsed = urlsplit(url)
db_name = parsed.path[1:]

# Get your DB
db = Connection(url)[db_name]

# Authenticate
if '@' in url:
    user, password = parsed.netloc.split('@')[0].split(':')
    db.authenticate(user, password)
