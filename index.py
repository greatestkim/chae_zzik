#!python
print("content-type: text/html; charset-utf-8\n")

import cgi, os, view

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value

    f = open('data/'+pageId, 'r')
    line=""
    theList=""
    i=0
    while True:
        line = f.readline()
        if line != '\n':
            theList += '<p class="list"><label for="check'+str(i)+'"><input type="checkbox" id="check'+str(i)+'"  onclick="checkboxHandler(this)">'+line+'</label><br></p>'
            i += 1
        if not line:
            break

    update_link='<a href="updateList.py?id={}">+</a>'.format(pageId)
    delete_action='''
        <form action="process_deleteMember.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input id="del" type="submit" value="DELETE MEMBER">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    theList = ' '
    update_link=''
    delete_action=''
 #jquery 이용
# href="index.py?id=HTML" 에서 HTML

print('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>chae_zzik.com</title>
    <link rel="stylesheet" href="style1.css?bee" />
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
      <p>MEMBER :  {listStr}
      <a id="newM" href="createNewMember.py">NEW MEMBER</a>
      </p>
    </div>

    <div class="common item">
        <div class="common item-a">
            <div><h3>{title} </h3></div>
            <div>{delete_action}</div>
        </div>
        <div class="common item-b">
            {list}
            {update_link}
        </div>
    </div>
    </div>
  </body>
  <script src="wide.js"></script>
</html>
'''.format(title=pageId, list=theList, listStr=view.getMember(),update_link=update_link, delete_action=delete_action,today=view.today))
#hamin's error log
#because of {} in <style>, format function didn't work
#반복문인데 왜 i증가 하지 않음? ;; i=0을 for문 안에 넣었으니까....
