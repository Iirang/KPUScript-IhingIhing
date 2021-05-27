# -*- coding: cp949 -*-
# ID: kpuscript2021@gmail.com
# PW: 스크립트언어2021

import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"

# 보내는 사람의 메일 주소 / 받는 사람의 메일 주소
senderAddr = "kpuscript2021@gmail.com"     
recipientAddr = "game2raaaang@kpu.ac.kr"

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "[한국마사회] 한국마사회에서 요청하신 정보를 보내드립니다"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME 문서를 생성합니다.
# htmlFD = open(htmlFileName, 'rb')
# HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
# htmlFD.close()

# 만들었던 mime을 MIMEBase에 첨부 시킨다.
# msg.attach(HtmlPart)

# 메일을 발송한다.
s = mysmtplib.MySMTP(host,port)
s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
s.ehlo()
s.starttls()
s.ehlo()
s.login("kpuscript2021@gmail.com","tmzmflqxmdjsdj2021")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()








































