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

    <div class"container">
    <div class="common date">
      <p>DATE : {today}</p>
    </div>

    <div class="common member">
      <p>MEMBER : {listStr}</p>
    </div>

    <div class="common item">
        <form action="process_createNewMember.py" method="post" class="formargin">
          <p><input type="text" name="title" placeholder="MY NAME HERE!"></p>
          <p><textarea rows="10" cols="100"  name="description" placeholder="LIST"></textarea></p>
          <p><input type="submit" value="SUBMIT"></p>
        </form>
    </div>
    </div>
  </body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getMember(),today=view.today))
