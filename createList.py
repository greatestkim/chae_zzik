#!python
print("content-type: text/html; charset-utf-8\n")

import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

from datetime import date
today = date.today()

print('''<!DOCTYPE html>
<html>

  <head>
    <meta charset="utf-8">
    <title>chae_zzik.com</title>
    <link rel="stylesheet" href="style1.css" />
  </head>

  <body>

    <header>
      <h1><a href="index.py">&lt; chae_zzik &gt;</a></h1>
    </header>

    <div class="today_date">
      <p>DATE : {today}</p>
    </div>

    <div class="mem_list">
      <p style="display: inline">MEMBER : </p> {listStr}
    </div>

    <div class="to_do_list">
        <form action="process_create.py" method="post">
          <p><input type="text" name="title" placeholder="MY NAME HERE!"></p>
          <p><textarea rows="1" cols="100"  name="description" placeholder="LIST"></textarea></p>
          <p><input type="submit" value="SUBMIT"></p>
        </form>
    </div>

  </body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getMember(),today=today))
