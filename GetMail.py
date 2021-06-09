from xml.dom.minidom import getDOMImplementation

def MailText(Result):

    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """

    """
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for item in Result:
        # create 주소 엘리먼트
        where = newdoc.createElement('where')
        # create text node
        whereText = newdoc.createTextNode("   주소 :" + item[0])
        where.appendChild(whereText)

        body.appendChild(where)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # 사고 종류
        what = newdoc.createElement('what')
        # create text node
        whatText = newdoc.createTextNode("   사고 종류:" + item[1])
        what.appendChild(whatText)

        body.appendChild(what)

        # 사고 수
        howMany = newdoc.createElement('howMany')
        # create text node
        howManyText = newdoc.createTextNode("   사고 수:" + str(item[2]))
        howMany.appendChild(howManyText)

        body.appendChild(howMany)

        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()
    """