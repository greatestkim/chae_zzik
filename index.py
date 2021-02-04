#!python
print("content-type: text/html; charset-utf-8\n")

import cgi, os, view

form = cgi.FieldStorage()
line=""
description=""

if 'id' in form:
    pageId = form["id"].value
    f = open('data/'+pageId, 'r')
    while True:
        line = f.readline()
        for i in line:#이 부분 없이 그냥 체크 박스 체크 유무로
            if i == '@@':
                description += '<p class="desc" style="text-decoration: line-through">'
                description += line
                description += '</p><br>'
            else:
                description += '<p class="desc"><input type="checkbox">'
                description += line
                description += '</p><br>'

        if not line: break
    update_link='<a href="updateList.py?id={}">UPDATE LIST</a>'.format(pageId)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="DELETE">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link=''
    delete_action=''
 #jquery 이용
# href="index.py?id=HTML" 에서 HTML

print('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>chae_zzik.com</title>
    <link rel="stylesheet" href="style1.css?beee" />
  </head>
  <body>
    <header>
      <h1><a href="index.py">&lt; chae_zzik &gt;</a></h1>
    </header>

    <div>
      <p>DATE : {today}</p>
    </div>

    <div>
      <p>MEMBER : </p> {listStr}
      <a href="createList.py">NEW MEMBER</a>
    </div>

    <div>
        <div>
            <h3>{title}</h3>
            {update_link}{delete_action}
        </div>
        <div>
            <p>{desc}</p>
        </div>
    </div>

  </body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getMember(),update_link=update_link, delete_action=delete_action,today=view.today))
#hamin's error log
#because of {} in <style>, format function didn't work
#반복문인데 왜 i증가 하지 않음? ;; i=0을 for문 안에 넣었으니까....
