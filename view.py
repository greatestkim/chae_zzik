import os

def getMember():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<a class="img-button" title="{name}" id="{name}" href="index.py?id={name}"><img src="images\{name}.jpg" width="50" height="50"></a>'.format(name=item)
    return listStr

from datetime import date
today = date.today()
