import os

def getMember():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<a href="index.py?id={name}">{name}</a>'.format(name=item)
    return listStr

from datetime import date
today = date.today()
