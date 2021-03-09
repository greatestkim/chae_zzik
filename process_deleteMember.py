#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)
#redirection
print("Location: index.py")
print()
